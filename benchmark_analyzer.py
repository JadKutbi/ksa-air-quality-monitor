"""
City Benchmark Analyzer Module

Analyzes and ranks all Saudi cities by pollution levels, providing
comparative analysis from least polluted to most polluted.

Features:
    - Composite pollution index calculation
    - Multi-gas weighted scoring
    - City-to-city ranking
    - Regional comparison statistics
    - Trend analysis across cities
"""

import numpy as np
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import logging
import config

logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)
logger = logging.getLogger(__name__)


class CityBenchmarkAnalyzer:
    """Analyze and rank cities by pollution levels."""

    # Gas weights for composite pollution index
    # Higher weight = more impact on overall pollution score
    GAS_WEIGHTS = {
        'NO2': 0.30,   # Nitrogen dioxide - major urban/industrial pollutant
        'SO2': 0.25,   # Sulfur dioxide - industrial emissions indicator
        'CO': 0.20,    # Carbon monoxide - combustion indicator
        'HCHO': 0.15,  # Formaldehyde - petrochemical/VOC indicator
        'CH4': 0.10,   # Methane - less directly harmful but climate relevant
    }

    # Ranking categories
    RANK_CATEGORIES = {
        'cleanest': {'min': 0, 'max': 25, 'label_en': 'Cleanest', 'label_ar': 'الأنظف', 'color': '#10b981'},
        'clean': {'min': 25, 'max': 50, 'label_en': 'Clean', 'label_ar': 'نظيف', 'color': '#22c55e'},
        'moderate': {'min': 50, 'max': 75, 'label_en': 'Moderate', 'label_ar': 'متوسط', 'color': '#f59e0b'},
        'polluted': {'min': 75, 'max': 100, 'label_en': 'Polluted', 'label_ar': 'ملوث', 'color': '#ef4444'},
        'heavily_polluted': {'min': 100, 'max': float('inf'), 'label_en': 'Heavily Polluted', 'label_ar': 'ملوث بشدة', 'color': '#dc2626'},
    }

    def __init__(self):
        """Initialize the benchmark analyzer."""
        self.cities = list(config.CITIES.keys())
        self.regions = self._organize_by_region()

    def _organize_by_region(self) -> Dict[str, List[str]]:
        """Organize cities by their geographic region."""
        regions = {}
        for city, info in config.CITIES.items():
            region = info.get('region', 'Unknown')
            if region not in regions:
                regions[region] = []
            regions[region].append(city)
        return regions

    def calculate_city_pollution_index(self, city_data: Dict) -> Dict:
        """
        Calculate a composite pollution index for a city.

        The index is calculated as a weighted average of all gas measurements
        normalized against their respective thresholds.

        Args:
            city_data: Dictionary of gas data for the city
                       {gas: {'statistics': {'max': value, 'mean': value}, 'success': bool}}

        Returns:
            Dictionary with pollution index and breakdown
        """
        if not city_data:
            return {
                'pollution_index': None,
                'category': 'unknown',
                'gas_scores': {},
                'violations': [],
                'violation_count': 0,
                'data_quality': 0,
                'gases_monitored': 0,
                'success': False
            }

        gas_scores = {}
        weighted_sum = 0
        total_weight = 0
        violations = []
        gases_with_data = 0

        for gas, weight in self.GAS_WEIGHTS.items():
            data = city_data.get(gas, {})
            if not data.get('success'):
                continue

            gases_with_data += 1
            threshold = config.GAS_THRESHOLDS.get(gas, {}).get('column_threshold', 1)
            critical = config.GAS_THRESHOLDS.get(gas, {}).get('critical_threshold', threshold * 2)

            max_val = data['statistics']['max']
            mean_val = data['statistics']['mean']

            # Calculate percentage of threshold (100% = at threshold)
            threshold_percent = (max_val / threshold * 100) if threshold > 0 else 0

            gas_scores[gas] = {
                'max_value': max_val,
                'mean_value': mean_val,
                'threshold': threshold,
                'threshold_percent': threshold_percent,
                'weight': weight
            }

            weighted_sum += threshold_percent * weight
            total_weight += weight

            # Track violations
            if max_val >= critical:
                violations.append({'gas': gas, 'severity': 'critical', 'percent': threshold_percent})
            elif max_val >= threshold:
                violations.append({'gas': gas, 'severity': 'moderate', 'percent': threshold_percent})

        if total_weight == 0:
            return {
                'pollution_index': None,
                'category': 'unknown',
                'gas_scores': {},
                'violations': [],
                'violation_count': 0,
                'data_quality': 0,
                'gases_monitored': 0,
                'success': False
            }

        # Calculate composite index
        pollution_index = weighted_sum / total_weight

        # Determine category
        category = 'unknown'
        for cat_name, cat_info in self.RANK_CATEGORIES.items():
            if cat_info['min'] <= pollution_index < cat_info['max']:
                category = cat_name
                break

        # Data quality score (percentage of gases with data)
        data_quality = (gases_with_data / len(self.GAS_WEIGHTS)) * 100

        return {
            'pollution_index': pollution_index,
            'category': category,
            'gas_scores': gas_scores,
            'violations': violations,
            'violation_count': len(violations),
            'data_quality': data_quality,
            'gases_monitored': gases_with_data,
            'success': True
        }

    def rank_cities(self, all_cities_data: Dict[str, Dict]) -> List[Dict]:
        """
        Rank all cities from least polluted to most polluted.

        Args:
            all_cities_data: Dictionary mapping city names to their pollution data
                            {city: {gas: {...}, ...}, ...}

        Returns:
            List of cities sorted by pollution index (ascending = cleanest first)
        """
        city_rankings = []

        for city in self.cities:
            city_data = all_cities_data.get(city, {})
            analysis = self.calculate_city_pollution_index(city_data)

            city_info = config.CITIES.get(city, {})

            city_rankings.append({
                'city': city,
                'region': city_info.get('region', 'Unknown'),
                'pollution_index': analysis['pollution_index'],
                'category': analysis['category'],
                'category_info': self.RANK_CATEGORIES.get(analysis['category'], {}),
                'violations': analysis['violations'],
                'violation_count': analysis['violation_count'],
                'gas_scores': analysis['gas_scores'],
                'data_quality': analysis['data_quality'],
                'has_data': analysis['success']
            })

        # Sort by pollution index (ascending) - cities without data go to end
        city_rankings.sort(key=lambda x: (
            0 if x['has_data'] else 1,  # Cities with data first
            x['pollution_index'] if x['pollution_index'] is not None else float('inf')
        ))

        # Add rank numbers
        rank = 1
        for i, city in enumerate(city_rankings):
            if city['has_data']:
                city['rank'] = rank
                rank += 1
            else:
                city['rank'] = None

        return city_rankings

    def get_regional_statistics(self, all_cities_data: Dict[str, Dict]) -> Dict[str, Dict]:
        """
        Calculate pollution statistics by region.

        Args:
            all_cities_data: Dictionary mapping city names to their pollution data

        Returns:
            Dictionary of regional statistics
        """
        regional_stats = {}

        for region, cities in self.regions.items():
            region_indices = []
            region_violations = 0
            cities_with_data = 0

            for city in cities:
                city_data = all_cities_data.get(city, {})
                analysis = self.calculate_city_pollution_index(city_data)

                if analysis['success'] and analysis['pollution_index'] is not None:
                    region_indices.append(analysis['pollution_index'])
                    region_violations += analysis['violation_count']
                    cities_with_data += 1

            if region_indices:
                regional_stats[region] = {
                    'avg_pollution_index': np.mean(region_indices),
                    'min_pollution_index': np.min(region_indices),
                    'max_pollution_index': np.max(region_indices),
                    'std_pollution_index': np.std(region_indices) if len(region_indices) > 1 else 0,
                    'total_violations': region_violations,
                    'cities_count': len(cities),
                    'cities_with_data': cities_with_data,
                    'coverage_percent': (cities_with_data / len(cities)) * 100
                }
            else:
                regional_stats[region] = {
                    'avg_pollution_index': None,
                    'min_pollution_index': None,
                    'max_pollution_index': None,
                    'std_pollution_index': None,
                    'total_violations': 0,
                    'cities_count': len(cities),
                    'cities_with_data': 0,
                    'coverage_percent': 0
                }

        return regional_stats

    def get_gas_leaderboard(self, all_cities_data: Dict[str, Dict], gas: str) -> List[Dict]:
        """
        Get city rankings for a specific gas.

        Args:
            all_cities_data: Dictionary mapping city names to their pollution data
            gas: Gas type to rank by

        Returns:
            List of cities sorted by that gas's pollution level
        """
        gas_rankings = []
        threshold = config.GAS_THRESHOLDS.get(gas, {}).get('column_threshold', 1)

        for city in self.cities:
            city_data = all_cities_data.get(city, {})
            gas_data = city_data.get(gas, {})

            if gas_data.get('success'):
                max_val = gas_data['statistics']['max']
                mean_val = gas_data['statistics']['mean']
                threshold_percent = (max_val / threshold * 100) if threshold > 0 else 0

                gas_rankings.append({
                    'city': city,
                    'region': config.CITIES.get(city, {}).get('region', 'Unknown'),
                    'max_value': max_val,
                    'mean_value': mean_val,
                    'threshold_percent': threshold_percent,
                    'is_violation': max_val >= threshold,
                    'has_data': True
                })
            else:
                gas_rankings.append({
                    'city': city,
                    'region': config.CITIES.get(city, {}).get('region', 'Unknown'),
                    'max_value': None,
                    'mean_value': None,
                    'threshold_percent': None,
                    'is_violation': False,
                    'has_data': False
                })

        # Sort by max value (ascending = cleanest first)
        gas_rankings.sort(key=lambda x: (
            0 if x['has_data'] else 1,
            x['max_value'] if x['max_value'] is not None else float('inf')
        ))

        # Add ranks
        rank = 1
        for city in gas_rankings:
            if city['has_data']:
                city['rank'] = rank
                rank += 1
            else:
                city['rank'] = None

        return gas_rankings

    def get_summary_statistics(self, all_cities_data: Dict[str, Dict]) -> Dict:
        """
        Get overall summary statistics across all cities.

        Args:
            all_cities_data: Dictionary mapping city names to their pollution data

        Returns:
            Summary statistics dictionary
        """
        rankings = self.rank_cities(all_cities_data)

        cities_with_data = [c for c in rankings if c['has_data']]

        if not cities_with_data:
            return {
                'total_cities': len(self.cities),
                'cities_with_data': 0,
                'cleanest_city': None,
                'most_polluted_city': None,
                'avg_pollution_index': None,
                'total_violations': 0,
                'cities_with_violations': 0,
                'category_distribution': {}
            }

        indices = [c['pollution_index'] for c in cities_with_data if c['pollution_index'] is not None]

        # Category distribution
        category_counts = {}
        for city in cities_with_data:
            cat = city['category']
            category_counts[cat] = category_counts.get(cat, 0) + 1

        return {
            'total_cities': len(self.cities),
            'cities_with_data': len(cities_with_data),
            'cleanest_city': cities_with_data[0] if cities_with_data else None,
            'most_polluted_city': cities_with_data[-1] if cities_with_data else None,
            'avg_pollution_index': np.mean(indices) if indices else None,
            'median_pollution_index': np.median(indices) if indices else None,
            'std_pollution_index': np.std(indices) if len(indices) > 1 else 0,
            'total_violations': sum(c['violation_count'] for c in cities_with_data),
            'cities_with_violations': sum(1 for c in cities_with_data if c['violation_count'] > 0),
            'category_distribution': category_counts
        }

    def compare_cities(self, city1_data: Dict, city2_data: Dict,
                      city1_name: str, city2_name: str) -> Dict:
        """
        Compare pollution levels between two cities.

        Args:
            city1_data: Pollution data for city 1
            city2_data: Pollution data for city 2
            city1_name: Name of city 1
            city2_name: Name of city 2

        Returns:
            Comparison results
        """
        analysis1 = self.calculate_city_pollution_index(city1_data)
        analysis2 = self.calculate_city_pollution_index(city2_data)

        gas_comparisons = {}
        for gas in self.GAS_WEIGHTS.keys():
            score1 = analysis1['gas_scores'].get(gas, {})
            score2 = analysis2['gas_scores'].get(gas, {})

            if score1 and score2:
                diff = score1.get('threshold_percent', 0) - score2.get('threshold_percent', 0)
                gas_comparisons[gas] = {
                    'city1_percent': score1.get('threshold_percent', 0),
                    'city2_percent': score2.get('threshold_percent', 0),
                    'difference': diff,
                    'cleaner_city': city1_name if diff < 0 else city2_name if diff > 0 else 'equal'
                }

        # Determine overall cleaner city
        idx1 = analysis1['pollution_index']
        idx2 = analysis2['pollution_index']

        if idx1 is not None and idx2 is not None:
            if idx1 < idx2:
                overall_cleaner = city1_name
                difference = ((idx2 - idx1) / idx2) * 100 if idx2 > 0 else 0
            elif idx2 < idx1:
                overall_cleaner = city2_name
                difference = ((idx1 - idx2) / idx1) * 100 if idx1 > 0 else 0
            else:
                overall_cleaner = 'equal'
                difference = 0
        else:
            overall_cleaner = 'insufficient_data'
            difference = None

        return {
            'city1': {
                'name': city1_name,
                'pollution_index': idx1,
                'category': analysis1['category'],
                'violations': analysis1['violation_count']
            },
            'city2': {
                'name': city2_name,
                'pollution_index': idx2,
                'category': analysis2['category'],
                'violations': analysis2['violation_count']
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
