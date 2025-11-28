"""
Fair City Benchmark Analyzer Module

Provides equitable city rankings by combining:
    1. Cached satellite data (from background scanner - ensures all cities evaluated)
    2. Historical violations from Firestore (weighted by monitoring frequency)
    3. Live satellite data (on-demand for specific cities)

Key Fairness Mechanisms:
    - Cities without monitoring history aren't penalized
    - Cache provides baseline for all cities
    - Composite score balances live + historical data
"""

import numpy as np
from typing import Dict, List, Optional
from datetime import datetime
from collections import defaultdict
import logging
import pytz
import config

logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)
logger = logging.getLogger(__name__)


class CityBenchmarkAnalyzer:
    """
    Analyze and rank cities with fairness guarantees.

    Combines cached satellite data with historical violations for fair rankings.
    """

    CACHE_COLLECTION = "city_pollution_cache"

    # Scoring weights
    WEIGHT_LIVE = 0.7       # Recent/cached satellite readings
    WEIGHT_HISTORICAL = 0.3  # Historical violation record

    # Ranking categories based on pollution score
    RANK_CATEGORIES = {
        'cleanest': {'min': 0, 'max': 30, 'label_en': 'Cleanest', 'label_ar': 'الأنظف', 'color': '#10b981'},
        'clean': {'min': 30, 'max': 60, 'label_en': 'Clean', 'label_ar': 'نظيف', 'color': '#22c55e'},
        'moderate': {'min': 60, 'max': 90, 'label_en': 'Moderate', 'label_ar': 'متوسط', 'color': '#f59e0b'},
        'polluted': {'min': 90, 'max': 120, 'label_en': 'Polluted', 'label_ar': 'ملوث', 'color': '#ef4444'},
        'heavily_polluted': {'min': 120, 'max': float('inf'), 'label_en': 'Heavily Polluted', 'label_ar': 'ملوث بشدة', 'color': '#dc2626'},
    }

    def __init__(self, violation_recorder=None):
        """Initialize with Firestore access."""
        self.cities = list(config.CITIES.keys())
        self.regions = self._organize_by_region()
        self.recorder = violation_recorder
        self.db = violation_recorder.db if violation_recorder and violation_recorder.use_firestore else None
        self._cache_data = {}
        self._historical_data = {}

    def _organize_by_region(self) -> Dict[str, List[str]]:
        """Organize cities by geographic region."""
        regions = {}
        for city, info in config.CITIES.items():
            region = info.get('region', 'Unknown')
            if region not in regions:
                regions[region] = []
            regions[region].append(city)
        return regions

    def load_all_data(self) -> tuple:
        """
        Load both cached satellite data and historical violations.

        Returns:
            Tuple of (cache_data, historical_data)
        """
        cache_data = self._load_cache()
        historical_data = self._load_historical()
        return cache_data, historical_data

    def _load_cache(self) -> Dict[str, Dict]:
        """Load cached satellite data for all cities."""
        if not self.db:
            logger.warning("Firestore not available - no cache data")
            return {}

        try:
            docs = self.db.collection(self.CACHE_COLLECTION).stream()
            cache = {}
            for doc in docs:
                data = doc.to_dict()
                city = data.get('city')
                if city:
                    cache[city] = data

            logger.info(f"Loaded cache data for {len(cache)} cities")
            self._cache_data = cache
            return cache

        except Exception as e:
            logger.error(f"Error loading cache: {e}")
            return {}

    def _load_historical(self) -> Dict[str, List[Dict]]:
        """Load historical violations organized by city."""
        if not self.recorder:
            return {}

        try:
            all_violations = self.recorder.get_all_violations(limit=None)

            city_violations = defaultdict(list)
            for v in all_violations:
                city = v.get('city', 'Unknown')
                city_violations[city].append(v)

            logger.info(f"Loaded {len(all_violations)} historical violations")
            self._historical_data = dict(city_violations)
            return self._historical_data

        except Exception as e:
            logger.error(f"Error loading historical data: {e}")
            return {}

    def calculate_city_score(self, city: str,
                            cache_data: Optional[Dict] = None,
                            historical_violations: Optional[List] = None) -> Dict:
        """
        Calculate a fair pollution score for a city.

        Combines:
            - Live Score: From cached satellite readings
            - Historical Score: From recorded violations

        Args:
            city: City name
            cache_data: Cached satellite data for this city
            historical_violations: List of historical violations

        Returns:
            Score breakdown dictionary
        """
        # Use instance cache if not provided
        if cache_data is None:
            cache_data = self._cache_data.get(city, {})
        if historical_violations is None:
            historical_violations = self._historical_data.get(city, [])

        live_score = 0
        historical_score = 0
        data_quality = 0
        active_violations = 0

        # === LIVE SCORE (from cache) ===
        # This is the current satellite measurement as % of threshold
        # 100% = at threshold, >100% = violation
        if cache_data and cache_data.get('metrics'):
            metrics = cache_data['metrics']

            # Base: average threshold percentage (0-100+)
            # This already reflects current pollution levels
            live_score = metrics.get('avg_threshold_percentage', 0)

            # Track active violations for display (but don't add to score - avoid double counting)
            active_violations = metrics.get('active_violations', 0)

            # Data quality
            data_quality = metrics.get('data_completeness', 0)

        # === HISTORICAL SCORE (from violations) ===
        # Adds penalty for past violations, capped to prevent dominating live data
        if historical_violations:
            violation_count = len(historical_violations)
            critical_count = sum(1 for v in historical_violations if v.get('severity') == 'critical')
            moderate_count = violation_count - critical_count

            # Weighted violations: critical = 1.5x (reduced from 2x)
            weighted_violations = moderate_count + (critical_count * 1.5)

            # Average exceedance (how much over threshold)
            exceedances = [v.get('percentage_over', 0) for v in historical_violations if v.get('percentage_over')]
            avg_exceedance = np.mean(exceedances) if exceedances else 0

            # Historical score: violations + exceedance bonus
            # Capped at 50 to prevent dominating live score
            historical_score = min(weighted_violations * 3 + avg_exceedance * 0.2, 50)

        # === COMPOSITE SCORE ===
        # Live score (current satellite data) is the primary metric
        # Historical adds context but shouldn't overwhelm current readings
        if data_quality > 0.3:
            # Have usable live data - use weighted combination
            composite = live_score * self.WEIGHT_LIVE + historical_score * self.WEIGHT_HISTORICAL
        elif historical_violations:
            # No live data but have history - use historical with penalty
            composite = historical_score + 30  # Base penalty for no current data
        else:
            # No data at all - neutral score
            composite = 50  # Middle of the road

        # Determine category
        category = 'heavily_polluted'
        for cat_name, cat_info in self.RANK_CATEGORIES.items():
            if cat_info['min'] <= composite < cat_info['max']:
                category = cat_name
                break

        # Confidence level
        has_live = data_quality > 0.5
        has_history = len(historical_violations) >= 3
        if has_live and has_history:
            confidence = 'high'
        elif has_live or has_history:
            confidence = 'medium'
        else:
            confidence = 'low'

        return {
            'city': city,
            'region': config.CITIES.get(city, {}).get('region', 'Unknown'),
            'pollution_index': round(composite, 1),
            'live_score': round(live_score, 1),
            'historical_score': round(historical_score, 1),
            'category': category,
            'category_info': self.RANK_CATEGORIES.get(category, {}),
            'data_quality': round(data_quality, 2),
            'confidence': confidence,
            'has_live_data': data_quality > 0,
            'has_historical_data': len(historical_violations) > 0,
            'violation_count': len(historical_violations),
            'active_violations': active_violations,
            'last_updated': cache_data.get('last_updated') if cache_data else None,
            'has_data': data_quality > 0 or len(historical_violations) > 0
        }

    def rank_cities(self, cache_data: Dict = None, historical_data: Dict = None) -> List[Dict]:
        """
        Generate fair rankings for all cities.

        Args:
            cache_data: Cached satellite data by city
            historical_data: Historical violations by city

        Returns:
            List of city scores sorted by pollution_index (ascending = cleanest)
        """
        if cache_data is None:
            cache_data = self._cache_data
        if historical_data is None:
            historical_data = self._historical_data

        rankings = []
        for city in self.cities:
            city_cache = cache_data.get(city, {})
            city_history = historical_data.get(city, [])

            score = self.calculate_city_score(city, city_cache, city_history)
            rankings.append(score)

        # Sort by pollution index (ascending = cleanest first)
        rankings.sort(key=lambda x: x['pollution_index'])

        # Add rank numbers
        for i, city_score in enumerate(rankings):
            city_score['rank'] = i + 1

        return rankings

    def get_regional_statistics(self, cache_data: Dict = None, historical_data: Dict = None) -> Dict[str, Dict]:
        """
        Calculate pollution statistics by region.

        Returns:
            Dictionary of regional statistics
        """
        if cache_data is None:
            cache_data = self._cache_data
        if historical_data is None:
            historical_data = self._historical_data

        regional_stats = {}

        for region, cities in self.regions.items():
            region_scores = []
            region_violations = 0
            cities_with_data = 0

            for city in cities:
                score = self.calculate_city_score(
                    city,
                    cache_data.get(city, {}),
                    historical_data.get(city, [])
                )
                region_scores.append(score['pollution_index'])
                region_violations += score['violation_count']
                if score['has_data']:
                    cities_with_data += 1

            regional_stats[region] = {
                'avg_pollution_index': np.mean(region_scores) if region_scores else 0,
                'min_pollution_index': np.min(region_scores) if region_scores else 0,
                'max_pollution_index': np.max(region_scores) if region_scores else 0,
                'total_violations': region_violations,
                'cities_count': len(cities),
                'cities_with_data': cities_with_data,
            }

        return regional_stats

    def get_gas_leaderboard(self, cache_data: Dict = None, gas: str = None) -> List[Dict]:
        """
        Get city rankings for a specific gas based on cached data.

        Args:
            cache_data: Cached satellite data by city
            gas: Gas type to rank by

        Returns:
            List of cities sorted by that gas's level
        """
        if cache_data is None:
            cache_data = self._cache_data

        gas_rankings = []

        for city in self.cities:
            city_cache = cache_data.get(city, {})
            readings = city_cache.get('latest_readings', {})
            gas_reading = readings.get(gas, {})

            if gas_reading.get('value') is not None:
                threshold = gas_reading.get('threshold', 1)
                value = gas_reading['value']
                threshold_pct = (value / threshold * 100) if threshold > 0 else 0

                gas_rankings.append({
                    'city': city,
                    'region': config.CITIES.get(city, {}).get('region', 'Unknown'),
                    'value': value,
                    'threshold': threshold,
                    'threshold_percent': round(threshold_pct, 1),
                    'is_violation': gas_reading.get('is_violation', False),
                    'has_data': True
                })
            else:
                gas_rankings.append({
                    'city': city,
                    'region': config.CITIES.get(city, {}).get('region', 'Unknown'),
                    'value': None,
                    'threshold_percent': 0,
                    'is_violation': False,
                    'has_data': False
                })

        # Sort by threshold percent (ascending = cleanest)
        gas_rankings.sort(key=lambda x: (not x['has_data'], x['threshold_percent']))

        for i, r in enumerate(gas_rankings):
            r['rank'] = i + 1

        return gas_rankings

    def get_summary_statistics(self, cache_data: Dict = None, historical_data: Dict = None) -> Dict:
        """
        Get overall summary statistics across all cities.

        Returns:
            Summary statistics dictionary
        """
        if cache_data is None:
            cache_data = self._cache_data
        if historical_data is None:
            historical_data = self._historical_data

        rankings = self.rank_cities(cache_data, historical_data)

        total_violations = sum(c['violation_count'] for c in rankings)
        total_active = sum(c['active_violations'] for c in rankings)

        # Category distribution
        category_counts = {}
        for city in rankings:
            cat = city['category']
            category_counts[cat] = category_counts.get(cat, 0) + 1

        # Data coverage
        cities_with_live = sum(1 for c in rankings if c['has_live_data'])
        cities_with_history = sum(1 for c in rankings if c['has_historical_data'])
        cities_with_any = sum(1 for c in rankings if c['has_data'])

        return {
            'total_cities': len(self.cities),
            'cities_with_data': cities_with_any,
            'cities_with_live_data': cities_with_live,
            'cities_with_historical_data': cities_with_history,
            'cleanest_city': rankings[0] if rankings else None,
            'most_polluted_city': rankings[-1] if rankings else None,
            'avg_pollution_index': np.mean([c['pollution_index'] for c in rankings]),
            'total_violations': total_violations,
            'total_active_violations': total_active,
            'cities_with_violations': sum(1 for c in rankings if c['violation_count'] > 0),
            'category_distribution': category_counts,
            'data_coverage_percent': round(cities_with_any / len(self.cities) * 100, 1)
        }

    def compare_cities(self, city1_name: str, city2_name: str,
                      cache_data: Dict = None, historical_data: Dict = None) -> Dict:
        """
        Compare pollution levels between two cities.

        Returns:
            Comparison results
        """
        if cache_data is None:
            cache_data = self._cache_data
        if historical_data is None:
            historical_data = self._historical_data

        score1 = self.calculate_city_score(
            city1_name,
            cache_data.get(city1_name, {}),
            historical_data.get(city1_name, [])
        )
        score2 = self.calculate_city_score(
            city2_name,
            cache_data.get(city2_name, {}),
            historical_data.get(city2_name, [])
        )

        # Gas-by-gas comparison from cache
        gas_comparisons = {}
        gases = ['NO2', 'SO2', 'CO', 'HCHO', 'CH4']

        cache1 = cache_data.get(city1_name, {}).get('latest_readings', {})
        cache2 = cache_data.get(city2_name, {}).get('latest_readings', {})

        for gas in gases:
            r1 = cache1.get(gas, {})
            r2 = cache2.get(gas, {})

            pct1 = 0
            pct2 = 0
            if r1.get('value') and r1.get('threshold'):
                pct1 = (r1['value'] / r1['threshold']) * 100
            if r2.get('value') and r2.get('threshold'):
                pct2 = (r2['value'] / r2['threshold']) * 100

            gas_comparisons[gas] = {
                'city1_percent': round(pct1, 1),
                'city2_percent': round(pct2, 1),
                'cleaner_city': city1_name if pct1 < pct2 else city2_name if pct2 < pct1 else 'equal'
            }

        # Overall comparison
        idx1 = score1['pollution_index']
        idx2 = score2['pollution_index']

        if idx1 < idx2:
            overall_cleaner = city1_name
            difference = ((idx2 - idx1) / idx2) * 100 if idx2 > 0 else 100
        elif idx2 < idx1:
            overall_cleaner = city2_name
            difference = ((idx1 - idx2) / idx1) * 100 if idx1 > 0 else 100
        else:
            overall_cleaner = 'equal'
            difference = 0

        return {
            'city1': {
                'name': city1_name,
                'pollution_index': idx1,
                'category': score1['category'],
                'violations': score1['violation_count']
            },
            'city2': {
                'name': city2_name,
                'pollution_index': idx2,
                'category': score2['category'],
                'violations': score2['violation_count']
            },
            'overall_cleaner': overall_cleaner,
            'difference_percent': round(difference, 1),
            'gas_comparisons': gas_comparisons
        }

    def get_ranking_category_info(self, category: str, lang: str = 'en') -> Dict:
        """Get display information for a ranking category."""
        cat_info = self.RANK_CATEGORIES.get(category, {})
        return {
            'label': cat_info.get(f'label_{lang}', category),
            'color': cat_info.get('color', '#6b7280'),
            'min': cat_info.get('min', 0),
            'max': cat_info.get('max', 100)
        }
