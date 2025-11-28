"""
Background City Scanner - Ensures fair pollution monitoring across all Saudi cities.

This module scans ALL cities for satellite data, storing results in a cache collection.
This eliminates selection bias where only user-picked cities have violation data.

Key Features:
    - Scans all 21 cities with parallel batching
    - Stores results in Firestore cache for instant access
    - Respects Google Earth Engine rate limits
    - Tracks monitoring stats for fairness normalization
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import pytz
import time

import config

logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)
logger = logging.getLogger(__name__)


class BackgroundCityScanner:
    """
    Proactively scans all Saudi cities for pollution data.

    This ensures fair benchmarking by giving all cities equal monitoring opportunity.
    """

    # Scanning configuration
    MAX_PARALLEL_CITIES = 3          # Concurrent city fetches (GEE rate limit)
    SECONDS_BETWEEN_BATCHES = 10     # Delay between parallel batches
    MAX_SCAN_TIME_MINUTES = 30       # Abort scan if taking too long

    CACHE_COLLECTION = "city_pollution_cache"

    def __init__(self, fetcher=None, db=None):
        """
        Initialize scanner with required services.

        Args:
            fetcher: SatelliteDataFetcher instance (optional, will create if not provided)
            db: Firestore client (optional)
        """
        self.fetcher = fetcher
        self.db = db
        self.cities = list(config.CITIES.keys())
        self.ksa_tz = pytz.timezone(config.TIMEZONE)

    def _ensure_fetcher(self):
        """Lazy-load the satellite fetcher."""
        if self.fetcher is None:
            from satellite_fetcher import SatelliteDataFetcher
            self.fetcher = SatelliteDataFetcher()
        return self.fetcher

    def _ensure_db(self):
        """Lazy-load the Firestore client."""
        if self.db is None:
            try:
                from violation_recorder import ViolationRecorder
                recorder = ViolationRecorder()
                if recorder.use_firestore:
                    self.db = recorder.db
            except Exception as e:
                logger.error(f"Could not initialize Firestore: {e}")
        return self.db

    def get_cache_status(self) -> Dict[str, Dict]:
        """
        Get current cache status for all cities.

        Returns:
            Dictionary mapping city names to their cache info
        """
        db = self._ensure_db()
        if not db:
            return {}

        try:
            status = {}
            now = datetime.now(pytz.UTC)

            for city in self.cities:
                try:
                    doc = db.collection(self.CACHE_COLLECTION).document(city).get()
                    if doc.exists:
                        data = doc.to_dict()
                        last_updated = data.get('last_updated', '')

                        # Calculate hours since update
                        hours_ago = None
                        if last_updated:
                            try:
                                if isinstance(last_updated, str):
                                    last_dt = datetime.fromisoformat(last_updated.replace('Z', '+00:00'))
                                else:
                                    last_dt = last_updated
                                hours_ago = (now - last_dt).total_seconds() / 3600
                            except:
                                pass

                        status[city] = {
                            'has_cache': True,
                            'last_updated': last_updated,
                            'hours_ago': hours_ago,
                            'metrics': data.get('metrics', {}),
                            'monitoring_stats': data.get('monitoring_stats', {})
                        }
                    else:
                        status[city] = {
                            'has_cache': False,
                            'last_updated': None,
                            'hours_ago': None,
                            'metrics': {},
                            'monitoring_stats': {}
                        }
                except Exception as e:
                    logger.warning(f"Error getting cache status for {city}: {e}")
                    status[city] = {'has_cache': False, 'error': str(e)}

            return status

        except Exception as e:
            logger.error(f"Error getting cache status: {e}")
            return {}

    def fetch_city_data(self, city: str, days_back: int = 7) -> Dict:
        """
        Fetch all gas data for a single city.

        Args:
            city: City name
            days_back: Days to search for satellite data

        Returns:
            Dictionary with gas readings and computed metrics
        """
        fetcher = self._ensure_fetcher()
        logger.info(f"Scanning {city}...")
        start_time = time.time()

        readings = {}
        violations = []
        successful_gases = 0

        for gas in config.GAS_PRODUCTS.keys():
            try:
                data = fetcher.fetch_gas_data(city, gas, days_back=days_back)

                if data and data.get('success'):
                    max_val = data['statistics']['max']
                    mean_val = data['statistics']['mean']
                    threshold = config.GAS_THRESHOLDS.get(gas, {}).get('column_threshold', 0)

                    is_violation = max_val >= threshold if threshold > 0 else False
                    pct_over = ((max_val - threshold) / threshold * 100) if threshold > 0 else 0

                    readings[gas] = {
                        'value': max_val,
                        'mean': mean_val,
                        'threshold': threshold,
                        'is_violation': is_violation,
                        'percentage_over': round(pct_over, 1),
                        'timestamp': data.get('timestamp_ksa', ''),
                        'days_old': data.get('days_old', 0)
                    }

                    successful_gases += 1

                    if is_violation:
                        violations.append({
                            'gas': gas,
                            'value': max_val,
                            'threshold': threshold,
                            'percentage_over': pct_over,
                            'severity': 'critical' if pct_over >= 100 else 'moderate'
                        })
                else:
                    readings[gas] = {
                        'value': None,
                        'error': data.get('error', 'No data') if data else 'Fetch failed',
                        'is_violation': False
                    }

            except Exception as e:
                logger.error(f"Error fetching {gas} for {city}: {e}")
                readings[gas] = {'value': None, 'error': str(e), 'is_violation': False}

        # Compute metrics
        data_completeness = successful_gases / len(config.GAS_PRODUCTS) if config.GAS_PRODUCTS else 0

        # Calculate pollution index
        threshold_percentages = []
        for gas, reading in readings.items():
            if reading.get('value') is not None and reading.get('threshold', 0) > 0:
                pct = (reading['value'] / reading['threshold']) * 100
                threshold_percentages.append(pct)

        avg_threshold_pct = sum(threshold_percentages) / len(threshold_percentages) if threshold_percentages else 0

        # Pollution index: avg threshold % + violation bonus
        pollution_index = avg_threshold_pct + len(violations) * 10

        elapsed = time.time() - start_time
        logger.info(f"Completed {city} in {elapsed:.1f}s - {successful_gases}/5 gases, {len(violations)} violations")

        return {
            'city': city,
            'region': config.CITIES.get(city, {}).get('region', 'Unknown'),
            'latest_readings': readings,
            'metrics': {
                'pollution_index': round(pollution_index, 1),
                'active_violations': len(violations),
                'gases_monitored': successful_gases,
                'data_completeness': round(data_completeness, 2),
                'avg_threshold_percentage': round(avg_threshold_pct, 1)
            },
            'violations': violations,
            'scan_duration_seconds': round(elapsed, 1)
        }

    def save_city_cache(self, city: str, data: Dict, is_background: bool = True) -> bool:
        """
        Save city scan results to Firestore cache.

        Args:
            city: City name
            data: Scan results
            is_background: Whether this is a background scan (vs user-initiated)

        Returns:
            True if saved successfully
        """
        db = self._ensure_db()
        if not db:
            logger.warning("Firestore not available - cannot save cache")
            return False

        try:
            now = datetime.now(pytz.UTC)

            # Get existing monitoring stats
            doc = db.collection(self.CACHE_COLLECTION).document(city).get()
            existing_stats = {}
            if doc.exists:
                existing_data = doc.to_dict()
                existing_stats = existing_data.get('monitoring_stats', {})

            # Update monitoring stats
            monitoring_stats = {
                'total_scans': existing_stats.get('total_scans', 0) + 1,
                'first_scan_date': existing_stats.get('first_scan_date', now.strftime('%Y-%m-%d')),
                'background_scans': existing_stats.get('background_scans', 0) + (1 if is_background else 0),
                'user_scans': existing_stats.get('user_scans', 0) + (0 if is_background else 1),
            }

            # Prepare document
            cache_doc = {
                'city': city,
                'region': data['region'],
                'last_updated': now.isoformat(),
                'latest_readings': data['latest_readings'],
                'metrics': data['metrics'],
                'violations': data.get('violations', []),
                'monitoring_stats': monitoring_stats
            }

            # Save to Firestore
            db.collection(self.CACHE_COLLECTION).document(city).set(cache_doc)
            logger.info(f"Saved cache for {city}")
            return True

        except Exception as e:
            logger.error(f"Failed to save cache for {city}: {e}")
            return False

    def scan_single_city(self, city: str, days_back: int = 7, save_cache: bool = True) -> Dict:
        """
        Scan a single city and optionally save to cache.

        Args:
            city: City name
            days_back: Days to search for data
            save_cache: Whether to save results to Firestore

        Returns:
            Scan results
        """
        data = self.fetch_city_data(city, days_back)

        if save_cache and data.get('metrics', {}).get('data_completeness', 0) > 0:
            self.save_city_cache(city, data, is_background=False)

        return data

    def scan_cities_batch(self, cities: List[str], days_back: int = 7,
                          progress_callback=None) -> Dict:
        """
        Scan multiple cities with parallel batching.

        Args:
            cities: List of city names to scan
            days_back: Days to search for data
            progress_callback: Optional callback(city, index, total) for progress updates

        Returns:
            Summary of scan results
        """
        start_time = time.time()
        logger.info(f"Starting batch scan of {len(cities)} cities...")

        results = {
            'successful': [],
            'failed': [],
            'total_violations': 0,
            'city_data': {}
        }

        # Process cities in batches
        for i in range(0, len(cities), self.MAX_PARALLEL_CITIES):
            batch = cities[i:i + self.MAX_PARALLEL_CITIES]

            # Check time limit
            elapsed_minutes = (time.time() - start_time) / 60
            if elapsed_minutes > self.MAX_SCAN_TIME_MINUTES:
                logger.warning(f"Scan time limit reached ({self.MAX_SCAN_TIME_MINUTES} min)")
                break

            logger.info(f"Processing batch: {batch}")

            # Parallel fetch within batch
            with ThreadPoolExecutor(max_workers=self.MAX_PARALLEL_CITIES) as executor:
                future_to_city = {
                    executor.submit(self.fetch_city_data, city, days_back): city
                    for city in batch
                }

                for future in as_completed(future_to_city):
                    city = future_to_city[future]
                    try:
                        data = future.result()
                        if data and data.get('metrics', {}).get('data_completeness', 0) > 0:
                            # Save to cache
                            self.save_city_cache(city, data, is_background=True)
                            results['successful'].append(city)
                            results['total_violations'] += data['metrics'].get('active_violations', 0)
                            results['city_data'][city] = data
                        else:
                            results['failed'].append(city)
                    except Exception as e:
                        logger.error(f"Error scanning {city}: {e}")
                        results['failed'].append(city)

                    # Progress callback
                    if progress_callback:
                        idx = len(results['successful']) + len(results['failed'])
                        progress_callback(city, idx, len(cities))

            # Delay between batches
            if i + self.MAX_PARALLEL_CITIES < len(cities):
                time.sleep(self.SECONDS_BETWEEN_BATCHES)

        results['duration_minutes'] = round((time.time() - start_time) / 60, 1)
        logger.info(f"Batch scan complete: {len(results['successful'])} successful, {len(results['failed'])} failed")

        return results

    def scan_all_cities(self, days_back: int = 7, progress_callback=None) -> Dict:
        """
        Scan all 21 Saudi cities.

        Args:
            days_back: Days to search for data
            progress_callback: Optional callback for progress updates

        Returns:
            Summary of scan results
        """
        return self.scan_cities_batch(self.cities, days_back, progress_callback)

    def get_stale_cities(self, max_age_hours: int = 24) -> List[str]:
        """
        Get list of cities that haven't been scanned recently.

        Args:
            max_age_hours: Consider cities stale if older than this

        Returns:
            List of city names needing refresh
        """
        status = self.get_cache_status()
        stale = []

        for city, info in status.items():
            if not info.get('has_cache'):
                stale.append(city)
            elif info.get('hours_ago') is not None and info['hours_ago'] > max_age_hours:
                stale.append(city)

        return stale
