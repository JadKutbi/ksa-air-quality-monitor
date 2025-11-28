"""
City Benchmark Analyzer Module

Analyzes and ranks all Saudi cities by pollution levels using historical
violation data from Firestore, providing comparative analysis from
least polluted to most polluted.

Features:
    - Historical violation-based ranking
    - Multi-gas violation frequency analysis
    - City-to-city ranking
    - Regional comparison statistics
    - Trend analysis across cities
"""

import numpy as np
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
from collections import defaultdict
import logging
import config

logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)
logger = logging.getLogger(__name__)


class CityBenchmarkAnalyzer:
    """Analyze and rank cities by historical violation data."""

    # Ranking categories based on violation score
    RANK_CATEGORIES = {
        'cleanest': {'min': 0, 'max': 5, 'label_en': 'Cleanest', 'label_ar': 'الأنظف', 'color': '#10b981'},
        'clean': {'min': 5, 'max': 15, 'label_en': 'Clean', 'label_ar': 'نظيف', 'color': '#22c55e'},
        'moderate': {'min': 15, 'max': 30, 'label_en': 'Moderate', 'label_ar': 'متوسط', 'color': '#f59e0b'},
        'polluted': {'min': 30, 'max': 50, 'label_en': 'Polluted', 'label_ar': 'ملوث', 'color': '#ef4444'},
        'heavily_polluted': {'min': 50, 'max': float('inf'), 'label_en': 'Heavily Polluted', 'label_ar': 'ملوث بشدة', 'color': '#dc2626'},
    }

    def __init__(self, violation_recorder=None):
        """Initialize the benchmark analyzer with violation recorder."""
        self.cities = list(config.CITIES.keys())
        self.regions = self._organize_by_region()
        self.recorder = violation_recorder
        self._cached_violations = None

    def _organize_by_region(self) -> Dict[str, List[str]]:
        """Organize cities by their geographic region."""
        regions = {}
        for city, info in config.CITIES.items():
            region = info.get('region', 'Unknown')
            if region not in regions:
                regions[region] = []
            regions[region].append(city)
        return regions

    def load_historical_data(self) -> Dict:
        """
        Load all historical violations from Firestore.
        This is fast - just one database query.

        Returns:
            Dictionary with violations organized by city
        """
        if not self.recorder:
            logger.warning("No violation recorder available")
            return {}

        try:
            # Get all violations (single Firestore query)
            all_violations = self.recorder.get_all_violations(limit=None)
            logger.info(f"Loaded {len(all_violations)} historical violations")

            # Organize by city
            city_violations = defaultdict(list)
            for v in all_violations:
                city = v.get('city', 'Unknown')
                city_violations[city].append(v)

            self._cached_violations = dict(city_violations)
            return self._cached_violations

        except Exception as e:
            logger.error(f"Error loading historical data: {e}")
            return {}

    def calculate_city_score(self, city: str, violations: List[Dict]) -> Dict:
        """
        Calculate pollution score for a city based on historical violations.

        Scoring factors:
        - Total violation count
        - Critical vs moderate severity ratio
        - Variety of gases violated
        - Average exceedance percentage

        Args:
            city: City name
            violations: List of violation records for this city

        Returns:
            Dictionary with score breakdown
        """
        if not violations:
            return {
                'pollution_score': 0,
                'category': 'cleanest',
                'total_violations': 0,
                'critical_count': 0,
                'moderate_count': 0,
                'gases_violated': [],
                'avg_exceedance': 0,
                'has_data': True  # City exists but has no violations = clean
            }

        total = len(violations)
        critical = sum(1 for v in violations if v.get('severity') == 'critical')
        moderate = total - critical

        # Get unique gases violated
        gases_violated = list(set(v.get('gas', 'Unknown') for v in violations))

        # Calculate average exceedance percentage
        exceedances = [v.get('percentage_over', 0) for v in violations if v.get('percentage_over')]
        avg_exceedance = np.mean(exceedances) if exceedances else 0

        # Calculate composite score
        # - Base: violation count (weighted)
        # - Critical violations count 2x
        # - More gas variety = higher score
        # - Higher exceedance = higher score
        base_score = moderate + (critical * 2)
        gas_multiplier = 1 + (len(gases_violated) - 1) * 0.1  # +10% per additional gas
        exceedance_factor = 1 + (avg_exceedance / 100) * 0.5  # Up to +50% for high exceedance

        pollution_score = base_score * gas_multiplier * exceedance_factor

        # Determine category
        category = 'heavily_polluted'
        for cat_name, cat_info in self.RANK_CATEGORIES.items():
            if cat_info['min'] <= pollution_score < cat_info['max']:
                category = cat_name
                break

        return {
            'pollution_score': pollution_score,
            'category': category,
            'total_violations': total,
            'critical_count': critical,
            'moderate_count': moderate,
            'gases_violated': gases_violated,
            'avg_exceedance': avg_exceedance,
            'has_data': True
        }

    def rank_cities(self, city_violations: Dict[str, List] = None) -> List[Dict]:
        """
        Rank all cities from least polluted to most polluted based on historical data.

        Args:
            city_violations: Dictionary mapping city names to their violations
                            If None, uses cached data from load_historical_data()

        Returns:
            List of cities sorted by pollution score (ascending = cleanest first)
        """
        if city_violations is None:
            city_violations = self._cached_violations or {}

        city_rankings = []

        for city in self.cities:
            violations = city_violations.get(city, [])
            score_data = self.calculate_city_score(city, violations)
            city_info = config.CITIES.get(city, {})

            city_rankings.append({
                'city': city,
                'region': city_info.get('region', 'Unknown'),
                'pollution_index': score_data['pollution_score'],
                'category': score_data['category'],
                'category_info': self.RANK_CATEGORIES.get(score_data['category'], {}),
                'violation_count': score_data['total_violations'],
                'critical_count': score_data['critical_count'],
                'moderate_count': score_data['moderate_count'],
                'gases_violated': score_data['gases_violated'],
                'avg_exceedance': score_data['avg_exceedance'],
                'has_data': True  # All cities have data (0 violations = clean)
            })

        # Sort by pollution score (ascending) - cleanest first
        city_rankings.sort(key=lambda x: x['pollution_index'])

        # Add rank numbers
        for i, city in enumerate(city_rankings):
            city['rank'] = i + 1

        return city_rankings

    def get_regional_statistics(self, city_violations: Dict[str, List] = None) -> Dict[str, Dict]:
        """
        Calculate pollution statistics by region.

        Args:
            city_violations: Dictionary mapping city names to their violations

        Returns:
            Dictionary of regional statistics
        """
        if city_violations is None:
            city_violations = self._cached_violations or {}

        regional_stats = {}

        for region, cities in self.regions.items():
            region_scores = []
            region_violations = 0
            region_critical = 0

            for city in cities:
                violations = city_violations.get(city, [])
                score_data = self.calculate_city_score(city, violations)
                region_scores.append(score_data['pollution_score'])
                region_violations += score_data['total_violations']
                region_critical += score_data['critical_count']

            regional_stats[region] = {
                'avg_pollution_index': np.mean(region_scores) if region_scores else 0,
                'min_pollution_index': np.min(region_scores) if region_scores else 0,
                'max_pollution_index': np.max(region_scores) if region_scores else 0,
                'total_violations': region_violations,
                'critical_violations': region_critical,
                'cities_count': len(cities),
                'cities_with_violations': sum(1 for c in cities if city_violations.get(c)),
            }

        return regional_stats

    def get_gas_leaderboard(self, city_violations: Dict[str, List] = None, gas: str = None) -> List[Dict]:
        """
        Get city rankings for a specific gas based on historical violations.

        Args:
            city_violations: Dictionary mapping city names to their violations
            gas: Gas type to rank by

        Returns:
            List of cities sorted by that gas's violation count
        """
        if city_violations is None:
            city_violations = self._cached_violations or {}

        gas_rankings = []

        for city in self.cities:
            violations = city_violations.get(city, [])
            # Filter to specific gas
            gas_violations = [v for v in violations if v.get('gas') == gas]

            total = len(gas_violations)
            critical = sum(1 for v in gas_violations if v.get('severity') == 'critical')
            exceedances = [v.get('percentage_over', 0) for v in gas_violations if v.get('percentage_over')]
            avg_exceedance = np.mean(exceedances) if exceedances else 0

            gas_rankings.append({
                'city': city,
                'region': config.CITIES.get(city, {}).get('region', 'Unknown'),
                'violation_count': total,
                'critical_count': critical,
                'threshold_percent': avg_exceedance,  # Using avg exceedance as threshold %
                'is_violation': total > 0,
                'has_data': True
            })

        # Sort by violation count (ascending = cleanest first)
        gas_rankings.sort(key=lambda x: (x['violation_count'], x['critical_count']))

        # Add ranks
        for i, city in enumerate(gas_rankings):
            city['rank'] = i + 1

        return gas_rankings

    def get_summary_statistics(self, city_violations: Dict[str, List] = None) -> Dict:
        """
        Get overall summary statistics across all cities.

        Args:
            city_violations: Dictionary mapping city names to their violations

        Returns:
            Summary statistics dictionary
        """
        if city_violations is None:
            city_violations = self._cached_violations or {}

        rankings = self.rank_cities(city_violations)

        total_violations = sum(c['violation_count'] for c in rankings)
        total_critical = sum(c['critical_count'] for c in rankings)

        # Category distribution
        category_counts = {}
        for city in rankings:
            cat = city['category']
            category_counts[cat] = category_counts.get(cat, 0) + 1

        # Get date range from violations
        all_violations = []
        for violations in city_violations.values():
            all_violations.extend(violations)

        date_range = None
        if all_violations:
            timestamps = [v.get('timestamp', '') for v in all_violations if v.get('timestamp')]
            if timestamps:
                timestamps.sort()
                date_range = {
                    'oldest': timestamps[0][:10] if timestamps else None,
                    'newest': timestamps[-1][:10] if timestamps else None
                }

        return {
            'total_cities': len(self.cities),
            'cities_with_data': len(self.cities),  # All cities have data
            'cleanest_city': rankings[0] if rankings else None,
            'most_polluted_city': rankings[-1] if rankings else None,
            'avg_pollution_index': np.mean([c['pollution_index'] for c in rankings]),
            'total_violations': total_violations,
            'total_critical': total_critical,
            'cities_with_violations': sum(1 for c in rankings if c['violation_count'] > 0),
            'category_distribution': category_counts,
            'date_range': date_range
        }

    def compare_cities(self, city1_name: str, city2_name: str,
                      city_violations: Dict[str, List] = None) -> Dict:
        """
        Compare pollution levels between two cities based on historical data.

        Args:
            city1_name: Name of city 1
            city2_name: Name of city 2
            city_violations: Dictionary mapping city names to their violations

        Returns:
            Comparison results
        """
        if city_violations is None:
            city_violations = self._cached_violations or {}

        score1 = self.calculate_city_score(city1_name, city_violations.get(city1_name, []))
        score2 = self.calculate_city_score(city2_name, city_violations.get(city2_name, []))

        # Gas-by-gas comparison
        gas_comparisons = {}
        gases = ['NO2', 'SO2', 'CO', 'HCHO', 'CH4']

        for gas in gases:
            v1 = [v for v in city_violations.get(city1_name, []) if v.get('gas') == gas]
            v2 = [v for v in city_violations.get(city2_name, []) if v.get('gas') == gas]

            count1 = len(v1)
            count2 = len(v2)

            gas_comparisons[gas] = {
                'city1_count': count1,
                'city2_count': count2,
                'city1_percent': count1,  # Using count as display value
                'city2_percent': count2,
                'cleaner_city': city1_name if count1 < count2 else city2_name if count2 < count1 else 'equal'
            }

        # Determine overall cleaner city
        idx1 = score1['pollution_score']
        idx2 = score2['pollution_score']

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
                'violations': score1['total_violations']
            },
            'city2': {
                'name': city2_name,
                'pollution_index': idx2,
                'category': score2['category'],
                'violations': score2['total_violations']
            },
            'overall_cleaner': overall_cleaner,
            'difference_percent': difference,
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
