"""
Translations Module - Arabic/English language support

Provides bilingual support for the Saudi Arabia Air Quality Monitoring System.
"""

TRANSLATIONS = {
    "en": {
        # App title and header
        "app_title": "Saudi Arabia Air Quality Monitor",
        "app_subtitle": "Real-time pollution monitoring using Sentinel-5P satellite data",
        "time_label": "Time",

        # Sidebar
        "control_panel": "Control Panel",
        "select_city": "Select City",
        "choose_city_help": "Choose the city to monitor",
        "refresh_settings": "Refresh Settings",
        "auto_refresh": "Auto-refresh data",
        "refresh_interval": "Refresh interval (hours)",
        "last_update": "Last Update",
        "never": "Never",
        "language": "Language",

        # Cities - Western Region
        "Yanbu": "Yanbu",
        "Jeddah": "Jeddah",
        "Makkah": "Makkah",
        "Madinah": "Madinah",
        "Rabigh": "Rabigh",

        # Cities - Eastern Region
        "Jubail": "Jubail",
        "Dammam": "Dammam",
        "Dhahran": "Dhahran",
        "Al-Khobar": "Al-Khobar",
        "Ras Tanura": "Ras Tanura",
        "Al-Ahsa": "Al-Ahsa",

        # Cities - Central Region
        "Riyadh": "Riyadh",
        "Sudair": "Sudair",
        "Qassim": "Qassim",

        # Cities - Southern Region
        "Jazan": "Jazan",
        "Abha": "Abha",
        "Najran": "Najran",

        # Cities - Northern Region
        "Tabuk": "Tabuk",
        "Hail": "Hail",
        "Al-Jouf": "Al-Jouf",
        "Arar": "Arar",

        # Regions
        "Western": "Western Region",
        "Eastern": "Eastern Region",
        "Central": "Central Region",
        "Southern": "Southern Region",
        "Northern": "Northern Region",

        # Tabs
        "tab_overview": "Overview",
        "tab_aqi": "AQI Dashboard",
        "tab_map": "Map View",
        "tab_analysis": "Analysis",
        "tab_violations": "Violations",
        "tab_insights": "Insights",
        "tab_history": "History",

        # Overview tab
        "current_metrics": "Current Air Quality Metrics",
        "no_data": "No data available",
        "fetching_data": "Fetching satellite data...",
        "data_age": "Data Age",
        "today": "today",
        "days_ago": "days ago",

        # Gas names
        "NO2": "Nitrogen Dioxide",
        "SO2": "Sulfur Dioxide",
        "CO": "Carbon Monoxide",
        "HCHO": "Formaldehyde",
        "CH4": "Methane",

        # Metrics
        "mean": "Mean",
        "max": "Max",
        "min": "Min",
        "threshold": "Threshold",
        "exceeded_by": "Exceeded by",
        "within_limits": "Within safe limits",

        # Violations
        "violation_analysis": "Violation Analysis",
        "no_violations": "No violations detected - Air quality is within safe limits",
        "violation_detected": "VIOLATION DETECTED",
        "severity": "Severity",
        "critical": "Critical",
        "moderate": "Moderate",
        "normal": "Normal",
        "hotspot_location": "Hotspot Location",
        "wind_conditions": "Wind Conditions",
        "wind_from": "Wind from",
        "wind_speed": "Speed",
        "ai_analysis": "AI Source Analysis",
        "analyzing": "Analyzing pollution source...",
        "nearby_factories": "Nearby Industrial Facilities",
        "upwind": "UPWIND",
        "distance": "Distance",
        "confidence": "Confidence",
        "already_saved": "Already saved",
        "saving": "Saving violation record...",
        "saved": "Saved",
        "save_failed": "Save failed",

        # Map
        "pollution_heatmap": "Pollution Heatmap",
        "select_gas": "Select Gas to Display",
        "violation_marker": "VIOLATION",
        "map_layers": "Map Layers",
        "satellite_view": "Satellite View",
        "factories_layer": "Industrial Facilities",

        # History
        "historical_trends": "Historical Trend Analysis",
        "timeline": "Timeline",
        "by_gas": "By Gas",
        "by_severity": "By Severity",
        "violations_over_time": "Violations Over Time",
        "avg_violations_day": "Avg Violations/Day",
        "peak_day": "Peak Day",
        "monitoring_period": "Monitoring Period",
        "total_violations": "Total Violations",
        "most_common_severity": "Most Common Severity",
        "most_frequent_gas": "Most Frequent Gas",
        "records_since": "Records Since",
        "filter_by_gas": "Filter by Gas",
        "show_records": "Show records",
        "clear_all": "Clear All",
        "delete": "Delete",
        "view_heatmap": "View Heatmap",
        "download_map": "Download Map (HTML)",
        "no_records": "No violation records found",
        "storage_info": "Storage Information",
        "cloud_storage": "Google Cloud Firestore - Persistent cloud storage enabled!",
        "local_storage": "Local Storage - Records may be lost on app restart",

        # AQI
        "aqi_dashboard": "Air Quality Index (AQI) Dashboard",
        "air_quality_status": "Air Quality Status",
        "dominant_pollutant": "Dominant Pollutant",
        "health_advice": "Health Advice",
        "aqi_good": "Good",
        "aqi_moderate": "Moderate",
        "aqi_unhealthy_sensitive": "Unhealthy for Sensitive Groups",
        "aqi_unhealthy": "Unhealthy",
        "aqi_very_unhealthy": "Very Unhealthy",
        "aqi_hazardous": "Hazardous",

        # Data quality
        "data_quality": "Data Quality Indicators",
        "spatial_coverage": "Spatial Coverage",
        "temporal_accuracy": "Temporal Accuracy",
        "measurement_validity": "Measurement Validity",
        "wind_sync": "Wind Sync",

        # Diagnostics
        "connection_diagnostics": "Connection Diagnostics",
        "test_connection": "Test Earth Engine Connection",
        "testing": "Testing connection...",
        "connection_success": "Connection successful!",
        "connection_failed": "Connection failed",

        # Common
        "all": "All",
        "unknown": "Unknown",
        "loading": "Loading...",
        "error": "Error",
        "success": "Success",
        "warning": "Warning",
        "info": "Info",
        "days": "days",
        "hours": "hours",
        "minutes": "minutes",
        "retry": "Retry",
        "violations": "violations",
        "km": "km",

        # Additional UI elements
        "about": "About",
        "monitored_gases": "Monitored Gases",
        "data_source": "Data Source",
        "standards": "Standards",
        "system_time": "System Time",
        "refresh_now": "Refresh Now",
        "detailed_analysis": "Detailed Analysis",
        "intelligent_insights": "Intelligent Insights & Predictions",
        "violation_details": "Violation Details",
        "aqi_dashboard_header": "Air Quality Index Dashboard",
        "pollution_map": "Pollution Map",
        "data_validation_report": "Data Validation Report",
        "quick_summary": "Quick Summary",
        "individual_gas_analysis": "Individual Gas Analysis",
        "detailed_values_table": "Detailed Values Table",
        "pollution_trends": "Pollution Trends",
        "showing_violations": "Showing {count} violation(s)",
        "no_data_available": "No pollution data available. Please try again later.",
        "connection_successful": "Earth Engine connection successful!",
        "connection_failed": "Connection failed",
        "can_access_data": "Can access Sentinel-5P data!",
        "cannot_access_data": "Cannot access Sentinel-5P",
        "using_service_account": "Using service account",
        "no_service_account": "No service account configured - using default auth",
        "please_check": "Please check",
        "violation_detected_for": "Violation Detected",
        "value": "Value",
        "wind": "Wind",
        "wind_confidence": "Wind Confidence",
        "type": "Type",
        "emissions": "Emissions",
        "satellite_pass": "Satellite Pass",
        "wind_reading": "Wind Reading",
        "sync_quality": "Sync Quality",
        "no_wind_data": "No wind data",
        "no_sync_data": "No sync data",
        "of_threshold": "of threshold",
        "normal_status": "Normal",
        "warning_status": "Warning",
        "record_deleted": "Record deleted",
        "failed_to_delete": "Failed to delete record",
        "all_records_cleared": "All records cleared",
        "click_to_confirm": "Click again to confirm deletion",
        "no_violations_recorded": "No violations recorded yet. Violations are automatically saved when detected.",
        "tip_violations": "Go to the Violations tab to detect and auto-save any current violations.",
        "tip": "Tip",

        # Dashboard components
        "overall_aqi": "Overall AQI",
        "aqi_by_pollutant": "AQI by Pollutant",
        "health_risk_assessment": "Health Risk Assessment",
        "risk_score": "Risk Score",
        "risk_by_pollutant": "Risk by Pollutant",
        "recommendations": "Recommendations",
        "data_quality_matrix": "Data Quality Matrix",
        "quality_metric": "Quality Metric",
        "pollutant": "Pollutant",
        "quality_score": "Quality Score",
        "average_quality": "Average Quality",
        "best_quality": "Best Quality",
        "needs_attention": "Needs Attention",
        "high_quality": "High Quality",
        "gases": "gases",
        "no_patterns_detected": "No significant patterns detected in current data",
        "detailed_trend_analysis": "Detailed Trend Analysis",
        "pollutant_correlations": "Pollutant Correlations",
        "both_elevated": "both elevated - possible common source",
        "no_correlations_detected": "No significant correlations detected",
        "who_compliance": "Satellite-Based Pollution Thresholds",
        "current_vs_who": "Current Satellite Measurements vs Sentinel-5P Typical Ranges",
        "peak_concentration": "Peak Concentration",
        "spatial_average": "Spatial Average",
        "who_guideline": "Threshold",
        "pollutant_gas": "Pollutant Gas",
        "concentration": "Concentration (Column Density)",
        "pollutants_exceeding": "pollutant(s) exceeding satellite thresholds",
        "all_within_guidelines": "All pollutants within normal satellite-observed ranges",
        "violation": "Violation",
        "compliant": "Compliant",
        "peak_level": "Peak Level",
        "average_level": "Average Level",
        "peak_percent_limit": "Peak % of Limit",
        "status": "Status",

        # Error messages
        "satellite_unavailable": "Satellite data service unavailable",
        "ai_unavailable": "AI analysis service unavailable",
        "map_unavailable": "Map visualization service unavailable",
        "validation_unavailable": "Data validation service unavailable",
        "recorder_unavailable": "Violation recording service unavailable",
        "cannot_connect_satellite": "Cannot connect to satellite data service",
        "check_earth_engine": "Check Earth Engine authentication in sidebar diagnostics.",
        "retrieving_data": "Retrieving {gas} data...",
        "failed_fetch_all": "Failed to fetch data for all gases",
        "partial_data": "Partial data ({count} gases unavailable)",
        "no_map_data": "No pollution data available to display on the map",
        "select_gas_display": "Select Gas to Display:",
        "analyzing_source": "Analyzing pollution source...",
        "saving_violation": "Saving violation record...",
        "already_saved_id": "Already saved",
        "nearby_facilities": "Nearby Industrial Facilities",
        "found": "found",
        "advanced_analytics": "Advanced Analytics",
        "testing_connection": "Testing connection...",
        "not_enough_data": "Not enough data for trend analysis",
        "violations_by_gas_time": "Violations by Gas Type Over Time",
        "total_violations_gas": "Total Violations by Gas",
        "avg_exceedance_gas": "Avg Threshold Exceedance by Gas",
        "avg_percent_threshold": "Avg % Over Threshold",
        "violations_severity_time": "Violations by Severity Over Time",
        "violations_by_severity": "Violations by Severity",
        "severity_breakdown": "Severity Breakdown",
        "critical_rate": "Critical Rate",
        "moderate_rate": "Moderate Rate",
        "recorder_unavailable_msg": "Violation recorder not available",
        "connected_writable": "Connected & Writable",
        "not_writable": "Not writable",
        "map_storage": "Map Storage",
        "stored_firestore": "Stored in Firestore (HTML embedded)",
        "violations_stored": "Violations and heatmaps are stored permanently in Google Cloud.",
        "local_storage_note": "Using local file storage. On Streamlit Cloud, storage is ephemeral - records may be cleared when the app restarts or redeploys.",
        "path": "Path",
        "firestore_available": "Firestore available",
        "yes": "Yes",
        "no": "No",
        "install_firestore": "install google-cloud-firestore",
        "total_gases_monitored": "Total Gases Monitored",
        "violations_detected": "Violations Detected",
        "data_quality_label": "Data Quality",
        "high": "High",
        "partial": "Partial",
        "no_data_label": "No Data",
        "note_different_days": "Some gases have data from different days due to cloud cover. Latest available data shown (up to {days} day(s) old). Check individual gas details for specific dates.",
        "violation_summary": "Violation Summary",
        "within_limits": "Within Limits",
        "violations_detected_gases": "Violations detected",
        "of_threshold_label": "of threshold",
        "normal_label": "Normal",
        "warning_label": "Warning",
        "min_label": "Min",
        "who_threshold": "Satellite Threshold",
        "percent_threshold": "% of Threshold",
        "detailed_timing": "Detailed Timing Information (All times in KSA)",
        "sync_quality_label": "Sync Quality",
        "excellent": "Excellent",
        "good": "Good",
        "poor": "Poor",
        "data_from": "Data from",
        "project": "Project",
        "collection": "Collection",

        # Health recommendations
        "health_good": "Enjoy outdoor activities. Air quality poses little to no risk.",
        "health_moderate": "Unusually sensitive people should consider limiting prolonged outdoor exertion.",
        "health_sensitive": "Children, elderly, and people with respiratory issues should limit outdoor activities.",
        "health_unhealthy": "Everyone should limit prolonged outdoor exertion. Sensitive groups should avoid outdoor activities.",
        "health_very_unhealthy": "Everyone should avoid outdoor exertion. Stay indoors with windows closed.",
        "health_hazardous": "Emergency conditions. Everyone should avoid any outdoor activities. Consider evacuation if advised.",
        "aqi_not_available": "AQI calculation not available for this gas",
        "refer_who": "Refer to Sentinel-5P typical ranges",
        "emergency_conditions": "Emergency conditions",
        "avoid_outdoor": "Avoid outdoor activities. Close windows. Use air purifiers.",

        # Risk levels
        "risk_low": "Low",
        "risk_moderate": "Moderate",
        "risk_high": "High",
        "risk_very_high": "Very High",
        "risk_severe": "Severe",
        "safe_outdoor": "Safe for all outdoor activities",
        "no_precautions": "No special precautions needed",
        "monitor_symptoms": "Sensitive groups should monitor symptoms",
        "limit_exertion": "Limit prolonged outdoor exertion",
        "reduce_outdoor": "Reduce outdoor activities",
        "keep_windows_closed": "Keep windows closed",
        "use_purifiers": "Use air purifiers if available",
        "avoid_outdoor_activities": "Avoid outdoor activities",
        "seal_indoor": "Seal indoor spaces",
        "wear_masks": "Consider wearing N95 masks outdoors",
        "stay_indoors": "Stay indoors",
        "emergency_measures": "Emergency measures required",
        "follow_advisories": "Follow official health advisories",

        # Data insights - dynamic messages
        "insight_multiple_violations": "Multiple pollutants violating standards simultaneously ({gases}) - indicates significant industrial activity",
        "insight_high_variance": "High spatial variance detected in {gases} - suggests localized pollution sources",
        "insight_low_wind": "Low wind speeds detected - pollution likely to accumulate",
        "insight_high_wind": "High wind speeds - pollution dispersing rapidly",
        "insight_morning_rush": "Morning rush hour - expect elevated NO2 from traffic",
        "insight_evening_rush": "Evening rush hour - monitor for traffic-related pollutants",
        "insight_summer": "Summer conditions - increased O3 formation likely",
        "insight_winter": "Winter conditions - potential for temperature inversions trapping pollutants",

        # Quality labels
        "quality_excellent": "Excellent",
        "quality_good": "Good",
        "quality_fair": "Fair",
        "quality_poor": "Poor",

        # Chart and display texts
        "threshold_label": "Threshold",
        "critical_label": "Critical",
        "min_label_chart": "Min",
        "mean_label_chart": "Mean",
        "max_label_chart": "Max",
        "pixels": "pixels",
        "view_full_analysis": "View Full Analysis",
        "no_data_dash": "—",
        "next_refresh": "Next",
        "data_note_different_days": "Note: Some gases have data from different days due to cloud cover. Latest available data shown (up to {days} day(s) old). Check individual gas details for specific dates.",

        # Benchmark tab translations
        "tab_benchmark": "City Rankings",
        "cities_benchmark": "Cities Pollution Benchmark",
        "benchmark_subtitle": "Ranking all Saudi cities from least polluted to most polluted",
        "fetch_all_cities": "Fetch Data for All Cities",
        "fetching_city_data": "Fetching data for {city}...",
        "benchmark_summary": "Benchmark Summary",
        "cities_monitored": "Cities Monitored",
        "cleanest_city": "Cleanest City",
        "most_polluted_city": "Most Polluted City",
        "avg_pollution_index": "Avg Pollution Index",
        "cities_with_violations": "Cities with Violations",
        "city_rankings_table": "City Rankings (Cleanest to Most Polluted)",
        "rank": "Rank",
        "city": "City",
        "region": "Region",
        "pollution_index": "Pollution Index",
        "category": "Category",
        "violations_count": "Violations",
        "active_violations": "Current Violations",
        "data_coverage": "Data Coverage",
        "regional_comparison": "Regional Comparison",
        "regional_avg_pollution": "Average Pollution Index by Region",
        "regional_violations": "Total Violations by Region",
        "gas_breakdown": "Gas-Specific Rankings",
        "select_gas_ranking": "Select Gas for Ranking",
        "gas_ranking_for": "City Rankings for {gas}",
        "threshold_percent": "% of Threshold",
        "no_benchmark_data": "No benchmark data available. Click 'Fetch Data for All Cities' to start.",
        "benchmark_loading": "Loading benchmark data for all cities...",
        "category_cleanest": "Cleanest",
        "category_clean": "Clean",
        "category_moderate": "Moderate",
        "category_polluted": "Polluted",
        "category_heavily_polluted": "Heavily Polluted",
        "category_unknown": "Unknown",
        "compare_cities": "Compare Cities",
        "select_city_1": "Select First City",
        "select_city_2": "Select Second City",
        "comparison_result": "Comparison Result",
        "cleaner_by": "cleaner by",
        "more_polluted_by": "more polluted by",
        "pollution_distribution": "Pollution Distribution by Category",
        "cities_in_category": "cities in this category",
        "benchmark_note": "Note: Rankings are based on composite pollution index calculated from all monitored gases weighted by health impact.",
        "refresh_benchmark": "Refresh Benchmark Data",
        "last_benchmark_update": "Last benchmark update",
        "benchmark_coverage": "Data coverage",
        "select_different_cities": "Please select two different cities to compare",
        "insufficient_data_comparison": "Insufficient data for comparison",
        "equal_pollution": "Equal pollution levels",
        "historical_data": "Historical data",

        # Fair benchmark translations
        "live_data_cities": "Cities with Live Data",
        "historical_data_cities": "Cities with History",
        "refresh_cache": "Refresh City Cache",
        "refresh_cache_desc": "Scan all cities to update the pollution cache. This ensures fair rankings for all cities.",
        "scan_all_cities": "Scan All Cities",
        "scanning_city": "Scanning {city}... ({current}/{total})",
        "scanning_all_cities": "Scanning all 21 cities for latest satellite data...",
        "scan_complete": "Scan complete! {success} cities updated, {failed} failed. Duration: {duration} min",
        "stale_cities": "{count} cities need refresh (>24h old)",
        "all_cities_fresh": "All cities have recent data",
        "benchmark_note_fair": "Rankings combine cached satellite data (70%) with historical violations (30%) for fair comparison. Cities without monitoring history receive neutral scores.",
        "confidence_high": "High confidence",
        "confidence_medium": "Medium confidence",
        "confidence_low": "Low confidence",
        "data_source_live": "Live satellite data",
        "data_source_historical": "Historical violations",
        "data_source_combined": "Combined score",
        "auto_scanning": "Auto-scanning all cities (5 satellite calls)...",
        "auto_scan_complete": "Scanned {cities} cities, found {violations} violations in {time}s",
        "efficient_scan_note": "Efficient: Fetches all of Saudi Arabia in just 5 satellite calls (one per gas)",
        "violations_auto_recorded": "{count} violations auto-recorded to database",
        "clear_all_history": "Clear All History",
        "click_to_confirm_clear_all": "Click again to confirm deletion of ALL violation records",
        "all_history_cleared": "Cleared {count} violation records from all cities",
    },

    "ar": {
        # App title and header
        "app_title": "مراقب جودة الهواء في المملكة العربية السعودية",
        "app_subtitle": "مراقبة التلوث في الوقت الفعلي باستخدام بيانات القمر الصناعي Sentinel-5P",
        "time_label": "الوقت",

        # Sidebar
        "control_panel": "لوحة التحكم",
        "select_city": "اختر المدينة",
        "choose_city_help": "اختر المدينة للمراقبة",
        "refresh_settings": "إعدادات التحديث",
        "auto_refresh": "تحديث تلقائي للبيانات",
        "refresh_interval": "فترة التحديث (ساعات)",
        "last_update": "آخر تحديث",
        "never": "أبداً",
        "language": "اللغة",

        # Cities - Western Region
        "Yanbu": "ينبع",
        "Jeddah": "جدة",
        "Makkah": "مكة المكرمة",
        "Madinah": "المدينة المنورة",
        "Rabigh": "رابغ",

        # Cities - Eastern Region
        "Jubail": "الجبيل",
        "Dammam": "الدمام",
        "Dhahran": "الظهران",
        "Al-Khobar": "الخبر",
        "Ras Tanura": "رأس تنورة",
        "Al-Ahsa": "الأحساء",

        # Cities - Central Region
        "Riyadh": "الرياض",
        "Sudair": "سدير",
        "Qassim": "القصيم",

        # Cities - Southern Region
        "Jazan": "جازان",
        "Abha": "أبها",
        "Najran": "نجران",

        # Cities - Northern Region
        "Tabuk": "تبوك",
        "Hail": "حائل",
        "Al-Jouf": "الجوف",
        "Arar": "عرعر",

        # Regions
        "Western": "المنطقة الغربية",
        "Eastern": "المنطقة الشرقية",
        "Central": "المنطقة الوسطى",
        "Southern": "المنطقة الجنوبية",
        "Northern": "المنطقة الشمالية",

        # Tabs
        "tab_overview": "نظرة عامة",
        "tab_aqi": "مؤشر جودة الهواء",
        "tab_map": "الخريطة",
        "tab_analysis": "التحليل",
        "tab_violations": "المخالفات",
        "tab_insights": "الرؤى",
        "tab_history": "السجل",

        # Overview tab
        "current_metrics": "مقاييس جودة الهواء الحالية",
        "no_data": "لا توجد بيانات متاحة",
        "fetching_data": "جاري جلب بيانات القمر الصناعي...",
        "data_age": "عمر البيانات",
        "today": "اليوم",
        "days_ago": "أيام مضت",

        # Gas names
        "NO2": "ثاني أكسيد النيتروجين",
        "SO2": "ثاني أكسيد الكبريت",
        "CO": "أول أكسيد الكربون",
        "HCHO": "الفورمالديهايد",
        "CH4": "الميثان",

        # Metrics
        "mean": "المتوسط",
        "max": "الأقصى",
        "min": "الأدنى",
        "threshold": "الحد المسموح",
        "exceeded_by": "تجاوز بنسبة",
        "within_limits": "ضمن الحدود الآمنة",

        # Violations
        "violation_analysis": "تحليل المخالفات",
        "no_violations": "لا توجد مخالفات - جودة الهواء ضمن الحدود الآمنة",
        "violation_detected": "تم اكتشاف مخالفة",
        "severity": "الشدة",
        "critical": "حرج",
        "moderate": "متوسط",
        "normal": "طبيعي",
        "hotspot_location": "موقع البؤرة",
        "wind_conditions": "ظروف الرياح",
        "wind_from": "الرياح من",
        "wind_speed": "السرعة",
        "ai_analysis": "تحليل الذكاء الاصطناعي للمصدر",
        "analyzing": "جاري تحليل مصدر التلوث...",
        "nearby_factories": "المنشآت الصناعية القريبة",
        "upwind": "مصدر الرياح",
        "distance": "المسافة",
        "confidence": "نسبة الثقة",
        "already_saved": "محفوظ مسبقاً",
        "saving": "جاري حفظ سجل المخالفة...",
        "saved": "تم الحفظ",
        "save_failed": "فشل الحفظ",

        # Map
        "pollution_heatmap": "خريطة التلوث الحرارية",
        "select_gas": "اختر الغاز للعرض",
        "violation_marker": "مخالفة",
        "map_layers": "طبقات الخريطة",
        "satellite_view": "عرض القمر الصناعي",
        "factories_layer": "المنشآت الصناعية",

        # History
        "historical_trends": "تحليل الاتجاهات التاريخية",
        "timeline": "الجدول الزمني",
        "by_gas": "حسب الغاز",
        "by_severity": "حسب الشدة",
        "violations_over_time": "المخالفات عبر الزمن",
        "avg_violations_day": "متوسط المخالفات/اليوم",
        "peak_day": "يوم الذروة",
        "monitoring_period": "فترة المراقبة",
        "total_violations": "إجمالي المخالفات",
        "most_common_severity": "الشدة الأكثر شيوعاً",
        "most_frequent_gas": "الغاز الأكثر تكراراً",
        "records_since": "السجلات منذ",
        "filter_by_gas": "تصفية حسب الغاز",
        "show_records": "عرض السجلات",
        "clear_all": "مسح الكل",
        "delete": "حذف",
        "view_heatmap": "عرض الخريطة الحرارية",
        "download_map": "تحميل الخريطة (HTML)",
        "no_records": "لا توجد سجلات مخالفات",
        "storage_info": "معلومات التخزين",
        "cloud_storage": "Google Cloud Firestore - التخزين السحابي الدائم مفعّل!",
        "local_storage": "التخزين المحلي - قد تُفقد السجلات عند إعادة تشغيل التطبيق",

        # AQI
        "aqi_dashboard": "لوحة مؤشر جودة الهواء (AQI)",
        "air_quality_status": "حالة جودة الهواء",
        "dominant_pollutant": "الملوث الرئيسي",
        "health_advice": "نصائح صحية",
        "aqi_good": "جيد",
        "aqi_moderate": "متوسط",
        "aqi_unhealthy_sensitive": "غير صحي للفئات الحساسة",
        "aqi_unhealthy": "غير صحي",
        "aqi_very_unhealthy": "غير صحي جداً",
        "aqi_hazardous": "خطر",

        # Data quality
        "data_quality": "مؤشرات جودة البيانات",
        "spatial_coverage": "التغطية المكانية",
        "temporal_accuracy": "الدقة الزمنية",
        "measurement_validity": "صحة القياس",
        "wind_sync": "مزامنة الرياح",

        # Diagnostics
        "connection_diagnostics": "تشخيص الاتصال",
        "test_connection": "اختبار اتصال Earth Engine",
        "testing": "جاري اختبار الاتصال...",
        "connection_success": "الاتصال ناجح!",
        "connection_failed": "فشل الاتصال",

        # Common
        "all": "الكل",
        "unknown": "غير معروف",
        "loading": "جاري التحميل...",
        "error": "خطأ",
        "success": "نجاح",
        "warning": "تحذير",
        "info": "معلومات",
        "days": "أيام",
        "hours": "ساعات",
        "minutes": "دقائق",
        "retry": "إعادة المحاولة",
        "violations": "مخالفات",
        "km": "كم",

        # Additional UI elements
        "about": "حول",
        "monitored_gases": "الغازات المراقبة",
        "data_source": "مصدر البيانات",
        "standards": "المعايير",
        "system_time": "وقت النظام",
        "refresh_now": "تحديث الآن",
        "detailed_analysis": "التحليل المفصل",
        "intelligent_insights": "رؤى وتنبؤات ذكية",
        "violation_details": "تفاصيل المخالفة",
        "aqi_dashboard_header": "لوحة مؤشر جودة الهواء",
        "pollution_map": "خريطة التلوث",
        "data_validation_report": "تقرير التحقق من البيانات",
        "quick_summary": "ملخص سريع",
        "individual_gas_analysis": "تحليل كل غاز",
        "detailed_values_table": "جدول القيم المفصلة",
        "pollution_trends": "اتجاهات التلوث",
        "showing_violations": "عرض {count} مخالفة",
        "no_data_available": "لا توجد بيانات تلوث متاحة. يرجى المحاولة لاحقاً.",
        "connection_successful": "اتصال Earth Engine ناجح!",
        "connection_failed": "فشل الاتصال",
        "can_access_data": "يمكن الوصول إلى بيانات Sentinel-5P!",
        "cannot_access_data": "لا يمكن الوصول إلى Sentinel-5P",
        "using_service_account": "استخدام حساب الخدمة",
        "no_service_account": "لا يوجد حساب خدمة مكوّن - استخدام المصادقة الافتراضية",
        "please_check": "يرجى التحقق من",
        "violation_detected_for": "تم اكتشاف مخالفة",
        "value": "القيمة",
        "wind": "الرياح",
        "wind_confidence": "ثقة بيانات الرياح",
        "type": "النوع",
        "emissions": "الانبعاثات",
        "satellite_pass": "مرور القمر الصناعي",
        "wind_reading": "قراءة الرياح",
        "sync_quality": "جودة المزامنة",
        "no_wind_data": "لا توجد بيانات رياح",
        "no_sync_data": "لا توجد بيانات مزامنة",
        "of_threshold": "من الحد المسموح",
        "normal_status": "طبيعي",
        "warning_status": "تحذير",
        "record_deleted": "تم حذف السجل",
        "failed_to_delete": "فشل حذف السجل",
        "all_records_cleared": "تم مسح جميع السجلات",
        "click_to_confirm": "انقر مرة أخرى للتأكيد",
        "no_violations_recorded": "لا توجد مخالفات مسجلة بعد. يتم حفظ المخالفات تلقائياً عند اكتشافها.",
        "tip_violations": "اذهب إلى تبويب المخالفات لاكتشاف وحفظ المخالفات الحالية تلقائياً.",
        "tip": "نصيحة",

        # Dashboard components
        "overall_aqi": "مؤشر جودة الهواء الإجمالي",
        "aqi_by_pollutant": "مؤشر جودة الهواء حسب الملوث",
        "health_risk_assessment": "تقييم المخاطر الصحية",
        "risk_score": "درجة المخاطر",
        "risk_by_pollutant": "المخاطر حسب الملوث",
        "recommendations": "التوصيات",
        "data_quality_matrix": "مصفوفة جودة البيانات",
        "quality_metric": "مقياس الجودة",
        "pollutant": "الملوث",
        "quality_score": "درجة الجودة",
        "average_quality": "متوسط الجودة",
        "best_quality": "أفضل جودة",
        "needs_attention": "يحتاج اهتمام",
        "high_quality": "جودة عالية",
        "gases": "غازات",
        "no_patterns_detected": "لم يتم اكتشاف أنماط مهمة في البيانات الحالية",
        "detailed_trend_analysis": "تحليل الاتجاهات المفصل",
        "pollutant_correlations": "ارتباطات الملوثات",
        "both_elevated": "كلاهما مرتفع - مصدر مشترك محتمل",
        "no_correlations_detected": "لم يتم اكتشاف ارتباطات مهمة",
        "who_compliance": "حدود التلوث بناءً على بيانات القمر الصناعي",
        "current_vs_who": "القياسات الحالية مقارنة بالنطاقات النموذجية لـ Sentinel-5P",
        "peak_concentration": "أعلى تركيز",
        "spatial_average": "المتوسط المكاني",
        "who_guideline": "الحد",
        "pollutant_gas": "الغاز الملوث",
        "concentration": "التركيز (كثافة العمود)",
        "pollutants_exceeding": "ملوث(ات) تتجاوز حدود القمر الصناعي",
        "all_within_guidelines": "جميع الملوثات ضمن النطاقات الطبيعية المرصودة",
        "violation": "مخالفة",
        "compliant": "متوافق",
        "peak_level": "أعلى مستوى",
        "average_level": "المستوى المتوسط",
        "peak_percent_limit": "نسبة الذروة من الحد",
        "status": "الحالة",

        # Error messages
        "satellite_unavailable": "خدمة بيانات القمر الصناعي غير متاحة",
        "ai_unavailable": "خدمة تحليل الذكاء الاصطناعي غير متاحة",
        "map_unavailable": "خدمة عرض الخريطة غير متاحة",
        "validation_unavailable": "خدمة التحقق من البيانات غير متاحة",
        "recorder_unavailable": "خدمة تسجيل المخالفات غير متاحة",
        "cannot_connect_satellite": "لا يمكن الاتصال بخدمة بيانات القمر الصناعي",
        "check_earth_engine": "تحقق من مصادقة Earth Engine في تشخيصات الشريط الجانبي.",
        "retrieving_data": "جاري استرداد بيانات {gas}...",
        "failed_fetch_all": "فشل في جلب البيانات لجميع الغازات",
        "partial_data": "بيانات جزئية ({count} غازات غير متاحة)",
        "no_map_data": "لا توجد بيانات تلوث متاحة للعرض على الخريطة",
        "select_gas_display": "اختر الغاز للعرض:",
        "analyzing_source": "جاري تحليل مصدر التلوث...",
        "saving_violation": "جاري حفظ سجل المخالفة...",
        "already_saved_id": "محفوظ مسبقاً",
        "nearby_facilities": "المنشآت الصناعية القريبة",
        "found": "وُجد",
        "advanced_analytics": "التحليلات المتقدمة",
        "testing_connection": "جاري اختبار الاتصال...",
        "not_enough_data": "لا توجد بيانات كافية لتحليل الاتجاهات",
        "violations_by_gas_time": "المخالفات حسب نوع الغاز عبر الزمن",
        "total_violations_gas": "إجمالي المخالفات حسب الغاز",
        "avg_exceedance_gas": "متوسط تجاوز الحد حسب الغاز",
        "avg_percent_threshold": "متوسط % فوق الحد",
        "violations_severity_time": "المخالفات حسب الشدة عبر الزمن",
        "violations_by_severity": "المخالفات حسب الشدة",
        "severity_breakdown": "توزيع الشدة",
        "critical_rate": "معدل الحرج",
        "moderate_rate": "معدل المتوسط",
        "recorder_unavailable_msg": "مسجل المخالفات غير متاح",
        "connected_writable": "متصل وقابل للكتابة",
        "not_writable": "غير قابل للكتابة",
        "map_storage": "تخزين الخرائط",
        "stored_firestore": "مخزن في Firestore (HTML مضمن)",
        "violations_stored": "المخالفات والخرائط الحرارية مخزنة بشكل دائم في Google Cloud.",
        "local_storage_note": "استخدام التخزين المحلي. على Streamlit Cloud، التخزين مؤقت - قد تُمسح السجلات عند إعادة تشغيل التطبيق أو إعادة نشره.",
        "path": "المسار",
        "firestore_available": "Firestore متاح",
        "yes": "نعم",
        "no": "لا",
        "install_firestore": "قم بتثبيت google-cloud-firestore",
        "total_gases_monitored": "إجمالي الغازات المراقبة",
        "violations_detected": "المخالفات المكتشفة",
        "data_quality_label": "جودة البيانات",
        "high": "عالية",
        "partial": "جزئية",
        "no_data_label": "لا توجد بيانات",
        "note_different_days": "بعض الغازات لديها بيانات من أيام مختلفة بسبب الغطاء السحابي. يتم عرض أحدث البيانات المتاحة (حتى {days} يوم/أيام). تحقق من تفاصيل كل غاز للتواريخ المحددة.",
        "violation_summary": "ملخص المخالفات",
        "within_limits": "ضمن الحدود",
        "violations_detected_gases": "تم اكتشاف مخالفات",
        "of_threshold_label": "من الحد",
        "normal_label": "طبيعي",
        "warning_label": "تحذير",
        "min_label": "الأدنى",
        "who_threshold": "حد القمر الصناعي",
        "percent_threshold": "% من الحد",
        "detailed_timing": "معلومات التوقيت المفصلة (جميع الأوقات بتوقيت السعودية)",
        "sync_quality_label": "جودة المزامنة",
        "excellent": "ممتاز",
        "good": "جيد",
        "poor": "ضعيف",
        "data_from": "البيانات من",
        "project": "المشروع",
        "collection": "المجموعة",

        # Health recommendations
        "health_good": "استمتع بالأنشطة الخارجية. جودة الهواء لا تشكل خطراً يُذكر.",
        "health_moderate": "يجب على الأشخاص الحساسين بشكل غير عادي التفكير في الحد من الجهد الخارجي المطول.",
        "health_sensitive": "يجب على الأطفال وكبار السن والأشخاص الذين يعانون من مشاكل في الجهاز التنفسي الحد من الأنشطة الخارجية.",
        "health_unhealthy": "يجب على الجميع الحد من الجهد الخارجي المطول. يجب على الفئات الحساسة تجنب الأنشطة الخارجية.",
        "health_very_unhealthy": "يجب على الجميع تجنب الجهد الخارجي. البقاء في الداخل مع إغلاق النوافذ.",
        "health_hazardous": "حالة طوارئ. يجب على الجميع تجنب أي أنشطة خارجية. فكر في الإخلاء إذا نُصح بذلك.",
        "aqi_not_available": "حساب مؤشر جودة الهواء غير متاح لهذا الغاز",
        "refer_who": "راجع إرشادات منظمة الصحة العالمية",
        "emergency_conditions": "حالات طوارئ",
        "avoid_outdoor": "تجنب الأنشطة الخارجية. أغلق النوافذ. استخدم أجهزة تنقية الهواء.",

        # Risk levels
        "risk_low": "منخفض",
        "risk_moderate": "متوسط",
        "risk_high": "مرتفع",
        "risk_very_high": "مرتفع جداً",
        "risk_severe": "شديد",
        "safe_outdoor": "آمن لجميع الأنشطة الخارجية",
        "no_precautions": "لا حاجة لاحتياطات خاصة",
        "monitor_symptoms": "يجب على الفئات الحساسة مراقبة الأعراض",
        "limit_exertion": "الحد من الجهد الخارجي المطول",
        "reduce_outdoor": "تقليل الأنشطة الخارجية",
        "keep_windows_closed": "أبقِ النوافذ مغلقة",
        "use_purifiers": "استخدم أجهزة تنقية الهواء إن توفرت",
        "avoid_outdoor_activities": "تجنب الأنشطة الخارجية",
        "seal_indoor": "أغلق الأماكن الداخلية",
        "wear_masks": "فكر في ارتداء أقنعة N95 في الخارج",
        "stay_indoors": "ابقَ في الداخل",
        "emergency_measures": "الإجراءات الطارئة مطلوبة",
        "follow_advisories": "اتبع النصائح الصحية الرسمية",

        # Data insights - dynamic messages
        "insight_multiple_violations": "⚠️ ملوثات متعددة تتجاوز المعايير في نفس الوقت ({gases}) - يشير إلى نشاط صناعي كبير",
        "insight_high_variance": "📊 تباين مكاني مرتفع في {gases} - يشير إلى مصادر تلوث موضعية",
        "insight_low_wind": "💨 سرعة رياح منخفضة - من المرجح تراكم التلوث",
        "insight_high_wind": "💨 سرعة رياح عالية - التلوث يتبدد بسرعة",
        "insight_morning_rush": "🌅 ساعة الذروة الصباحية - توقع ارتفاع NO2 من حركة المرور",
        "insight_evening_rush": "🌆 ساعة الذروة المسائية - راقب الملوثات المتعلقة بحركة المرور",
        "insight_summer": "☀️ ظروف صيفية - زيادة محتملة في تكوين O3",
        "insight_winter": "❄️ ظروف شتوية - احتمال انعكاسات حرارية تحبس الملوثات",

        # Quality labels
        "quality_excellent": "ممتاز",
        "quality_good": "جيد",
        "quality_fair": "مقبول",
        "quality_poor": "ضعيف",

        # Chart and display texts
        "threshold_label": "الحد",
        "critical_label": "حرج",
        "min_label_chart": "الأدنى",
        "mean_label_chart": "المتوسط",
        "max_label_chart": "الأقصى",
        "pixels": "بكسل",
        "view_full_analysis": "عرض التحليل الكامل",
        "no_data_dash": "—",
        "next_refresh": "التالي",
        "data_note_different_days": "ملاحظة: بعض الغازات لديها بيانات من أيام مختلفة بسبب الغطاء السحابي. يتم عرض أحدث البيانات المتاحة (حتى {days} يوم/أيام). تحقق من تفاصيل كل غاز للتواريخ المحددة.",

        # Benchmark tab translations
        "tab_benchmark": "تصنيف المدن",
        "cities_benchmark": "مقارنة تلوث المدن",
        "benchmark_subtitle": "ترتيب جميع المدن السعودية من الأقل تلوثاً إلى الأكثر تلوثاً",
        "fetch_all_cities": "جلب بيانات جميع المدن",
        "fetching_city_data": "جاري جلب بيانات {city}...",
        "benchmark_summary": "ملخص المقارنة",
        "cities_monitored": "المدن المراقبة",
        "cleanest_city": "أنظف مدينة",
        "most_polluted_city": "أكثر مدينة تلوثاً",
        "avg_pollution_index": "متوسط مؤشر التلوث",
        "cities_with_violations": "مدن بمخالفات",
        "city_rankings_table": "ترتيب المدن (من الأنظف إلى الأكثر تلوثاً)",
        "rank": "الترتيب",
        "city": "المدينة",
        "region": "المنطقة",
        "pollution_index": "مؤشر التلوث",
        "category": "الفئة",
        "violations_count": "المخالفات",
        "active_violations": "المخالفات الحالية",
        "data_coverage": "تغطية البيانات",
        "regional_comparison": "مقارنة المناطق",
        "regional_avg_pollution": "متوسط مؤشر التلوث حسب المنطقة",
        "regional_violations": "إجمالي المخالفات حسب المنطقة",
        "gas_breakdown": "ترتيب حسب الغاز",
        "select_gas_ranking": "اختر الغاز للترتيب",
        "gas_ranking_for": "ترتيب المدن لـ {gas}",
        "threshold_percent": "% من الحد",
        "no_benchmark_data": "لا توجد بيانات مقارنة متاحة. انقر على 'جلب بيانات جميع المدن' للبدء.",
        "benchmark_loading": "جاري تحميل بيانات المقارنة لجميع المدن...",
        "category_cleanest": "الأنظف",
        "category_clean": "نظيف",
        "category_moderate": "متوسط",
        "category_polluted": "ملوث",
        "category_heavily_polluted": "ملوث بشدة",
        "category_unknown": "غير معروف",
        "compare_cities": "مقارنة المدن",
        "select_city_1": "اختر المدينة الأولى",
        "select_city_2": "اختر المدينة الثانية",
        "comparison_result": "نتيجة المقارنة",
        "cleaner_by": "أنظف بنسبة",
        "more_polluted_by": "أكثر تلوثاً بنسبة",
        "pollution_distribution": "توزيع التلوث حسب الفئة",
        "cities_in_category": "مدن في هذه الفئة",
        "benchmark_note": "ملاحظة: يعتمد الترتيب على مؤشر التلوث المركب المحسوب من جميع الغازات المراقبة مرجحة حسب التأثير الصحي.",
        "refresh_benchmark": "تحديث بيانات المقارنة",
        "last_benchmark_update": "آخر تحديث للمقارنة",
        "benchmark_coverage": "تغطية البيانات",
        "select_different_cities": "يرجى اختيار مدينتين مختلفتين للمقارنة",
        "insufficient_data_comparison": "بيانات غير كافية للمقارنة",
        "equal_pollution": "مستويات تلوث متساوية",
        "historical_data": "البيانات التاريخية",

        # Fair benchmark translations
        "live_data_cities": "مدن ببيانات حية",
        "historical_data_cities": "مدن بسجل تاريخي",
        "refresh_cache": "تحديث ذاكرة التخزين",
        "refresh_cache_desc": "فحص جميع المدن لتحديث ذاكرة التلوث. هذا يضمن ترتيباً عادلاً لجميع المدن.",
        "scan_all_cities": "فحص جميع المدن",
        "scanning_city": "جاري فحص {city}... ({current}/{total})",
        "scanning_all_cities": "جاري فحص جميع المدن الـ 21 للحصول على أحدث بيانات الأقمار الصناعية...",
        "scan_complete": "اكتمل الفحص! تم تحديث {success} مدينة، فشل {failed}. المدة: {duration} دقيقة",
        "stale_cities": "{count} مدينة تحتاج تحديث (أكثر من 24 ساعة)",
        "all_cities_fresh": "جميع المدن لديها بيانات حديثة",
        "benchmark_note_fair": "يجمع الترتيب بين بيانات الأقمار الصناعية المخزنة (70%) والمخالفات التاريخية (30%) لمقارنة عادلة. المدن بدون سجل مراقبة تحصل على درجات محايدة.",
        "confidence_high": "ثقة عالية",
        "confidence_medium": "ثقة متوسطة",
        "confidence_low": "ثقة منخفضة",
        "data_source_live": "بيانات أقمار صناعية حية",
        "data_source_historical": "مخالفات تاريخية",
        "data_source_combined": "درجة مجمعة",
        "auto_scanning": "جاري الفحص التلقائي لجميع المدن (5 استدعاءات قمر صناعي)...",
        "auto_scan_complete": "تم فحص {cities} مدينة، وُجدت {violations} مخالفات في {time} ثانية",
        "efficient_scan_note": "كفاءة عالية: يجلب بيانات كل السعودية في 5 استدعاءات فقط (واحد لكل غاز)",
        "violations_auto_recorded": "تم تسجيل {count} مخالفات تلقائياً في قاعدة البيانات",
        "clear_all_history": "مسح كل السجل",
        "click_to_confirm_clear_all": "انقر مرة أخرى لتأكيد حذف جميع سجلات المخالفات",
        "all_history_cleared": "تم مسح {count} سجل مخالفات من جميع المدن",
    }
}


def get_text(key: str, lang: str = "en") -> str:
    """
    Get translated text for a given key.

    Args:
        key: Translation key
        lang: Language code ('en' or 'ar')

    Returns:
        Translated string, or key if not found
    """
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, key)


def get_direction(lang: str = "en") -> str:
    """Get text direction for the language."""
    return "rtl" if lang == "ar" else "ltr"


def get_font_family(lang: str = "en") -> str:
    """Get appropriate font family for the language."""
    if lang == "ar":
        return "'Noto Sans Arabic', 'Segoe UI', Tahoma, sans-serif"
    return "'Segoe UI', Tahoma, sans-serif"
