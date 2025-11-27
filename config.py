"""
Saudi Arabia Air Quality Monitoring System - Configuration Module

This module contains all configuration parameters for the real-time pollution
monitoring system, including city definitions, gas monitoring specifications,
WHO 2021 threshold values, and industrial facility locations.

Data Sources:
    - Sentinel-5P TROPOMI satellite imagery via Google Earth Engine
    - ERA5/NOAA GFS reanalysis for wind data
    - Real-time weather APIs for wind synchronization

Standards:
    - WHO Air Quality Guidelines 2021
    - US EPA AQI calculation methodology
"""

import os
from datetime import datetime


# =============================================================================
# GEOGRAPHIC CONFIGURATION
# All major industrial cities in Saudi Arabia
# =============================================================================
CITIES = {
    # Western Region
    "Yanbu": {
        "center": [24.0889, 38.0618],
        "bbox": [38.07, 23.89, 38.46, 24.05],
        "radius_km": 25,
        "region": "Western"
    },
    "Jeddah": {
        "center": [21.4858, 39.1925],
        "bbox": [39.05, 21.35, 39.35, 21.65],
        "radius_km": 30,
        "region": "Western"
    },
    "Makkah": {
        "center": [21.3891, 39.8579],
        "bbox": [39.70, 21.25, 40.00, 21.55],
        "radius_km": 20,
        "region": "Western"
    },
    "Madinah": {
        "center": [24.5247, 39.5692],
        "bbox": [39.40, 24.35, 39.75, 24.70],
        "radius_km": 20,
        "region": "Western"
    },
    "Rabigh": {
        "center": [22.7976, 39.0347],
        "bbox": [38.85, 22.60, 39.25, 23.00],
        "radius_km": 25,
        "region": "Western"
    },

    # Eastern Region
    "Jubail": {
        "center": [27.0173, 49.6575],
        "bbox": [49.50, 26.90, 49.80, 27.15],
        "radius_km": 25,
        "region": "Eastern"
    },
    "Dammam": {
        "center": [26.4207, 50.0888],
        "bbox": [49.90, 26.25, 50.25, 26.60],
        "radius_km": 25,
        "region": "Eastern"
    },
    "Dhahran": {
        "center": [26.2361, 50.0393],
        "bbox": [49.85, 26.10, 50.20, 26.40],
        "radius_km": 20,
        "region": "Eastern"
    },
    "Al-Khobar": {
        "center": [26.2794, 50.2083],
        "bbox": [50.05, 26.15, 50.35, 26.45],
        "radius_km": 20,
        "region": "Eastern"
    },
    "Ras Tanura": {
        "center": [26.6444, 50.0500],
        "bbox": [49.90, 26.50, 50.20, 26.80],
        "radius_km": 20,
        "region": "Eastern"
    },
    "Al-Ahsa": {
        "center": [25.3898, 49.5859],
        "bbox": [49.40, 25.20, 49.80, 25.60],
        "radius_km": 25,
        "region": "Eastern"
    },

    # Central Region
    "Riyadh": {
        "center": [24.7136, 46.6753],
        "bbox": [46.45, 24.50, 46.95, 24.95],
        "radius_km": 35,
        "region": "Central"
    },
    "Sudair": {
        "center": [25.5833, 45.6167],
        "bbox": [45.40, 25.40, 45.85, 25.80],
        "radius_km": 25,
        "region": "Central"
    },
    "Qassim": {
        "center": [26.3260, 43.9750],
        "bbox": [43.75, 26.10, 44.20, 26.55],
        "radius_km": 25,
        "region": "Central"
    },

    # Southern Region
    "Jazan": {
        "center": [16.8892, 42.5511],
        "bbox": [42.4511, 16.7892, 42.6511, 16.9892],
        "radius_km": 15,
        "region": "Southern"
    },
    "Abha": {
        "center": [18.2164, 42.5053],
        "bbox": [42.30, 18.05, 42.70, 18.40],
        "radius_km": 20,
        "region": "Southern"
    },
    "Najran": {
        "center": [17.4933, 44.1277],
        "bbox": [43.95, 17.30, 44.35, 17.70],
        "radius_km": 20,
        "region": "Southern"
    },

    # Northern Region
    "Tabuk": {
        "center": [28.3838, 36.5550],
        "bbox": [36.35, 28.20, 36.75, 28.60],
        "radius_km": 25,
        "region": "Northern"
    },
    "Hail": {
        "center": [27.5114, 41.7208],
        "bbox": [41.50, 27.30, 41.95, 27.75],
        "radius_km": 25,
        "region": "Northern"
    },
    "Al-Jouf": {
        "center": [29.8117, 40.1000],
        "bbox": [39.90, 29.60, 40.30, 30.05],
        "radius_km": 25,
        "region": "Northern"
    },
    "Arar": {
        "center": [30.9753, 41.0178],
        "bbox": [40.80, 30.80, 41.25, 31.15],
        "radius_km": 20,
        "region": "Northern"
    }
}

# =============================================================================
# GAS MONITORING CONFIGURATION
# Sentinel-5P TROPOMI products for tropospheric pollution monitoring
# Units based on Sentinel Hub S5P L2 documentation:
# https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Data/S5PL2.html
# =============================================================================
GAS_PRODUCTS = {
    "NO2": {
        "name": "Nitrogen Dioxide",
        "dataset": "COPERNICUS/S5P/NRTI/L3_NO2",
        "band": "NO2_column_number_density",
        "unit": "mol/m²",
        "conversion_factor": 1e6,  # Convert to µmol/m² for readability
        "display_unit": "µmol/m²",
        "typical_range": [0, 0.0003],  # mol/m² - polluted cities may reach 2-3x
        "source_unit": "MOL_M2"
    },
    "SO2": {
        "name": "Sulfur Dioxide",
        "dataset": "COPERNICUS/S5P/NRTI/L3_SO2",
        "band": "SO2_column_number_density",
        "unit": "mol/m²",
        "conversion_factor": 1e6,  # Convert to µmol/m² for readability
        "display_unit": "µmol/m²",
        "typical_range": [0, 0.01],  # mol/m² - volcanic eruptions can exceed 0.35
        "source_unit": "MOL_M2"
    },
    "CO": {
        "name": "Carbon Monoxide",
        "dataset": "COPERNICUS/S5P/NRTI/L3_CO",
        "band": "CO_column_number_density",
        "unit": "mol/m²",
        "conversion_factor": 1e3,  # Convert to mmol/m² for readability
        "display_unit": "mmol/m²",
        "typical_range": [0, 0.1],  # mol/m² - wildfires may exceed
        "source_unit": "MOL_M2"
    },
    "HCHO": {
        "name": "Formaldehyde",
        "dataset": "COPERNICUS/S5P/NRTI/L3_HCHO",
        "band": "tropospheric_HCHO_column_number_density",
        "unit": "mol/m²",
        "conversion_factor": 1e6,  # Convert to µmol/m² for readability
        "display_unit": "µmol/m²",
        "typical_range": [0, 0.001],  # mol/m² - events may exceed
        "source_unit": "MOL_M2"
    },
    "CH4": {
        "name": "Methane",
        "dataset": "COPERNICUS/S5P/OFFL/L3_CH4",
        "band": "CH4_column_volume_mixing_ratio_dry_air",
        "unit": "ppb",
        "conversion_factor": 1,  # Already in ppb
        "display_unit": "ppb",
        "typical_range": [1600, 2000],  # ppb
        "source_unit": "PPB"
    }
}

# =============================================================================
# WHO 2021 AIR QUALITY THRESHOLDS
# Column density thresholds based on Sentinel-5P typical ranges
# Reference: https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Data/S5PL2.html
# Thresholds are in raw mol/m² units from satellite (before conversion factor)
# =============================================================================
GAS_THRESHOLDS = {
    "NO2": {
        "annual_avg_ugm3": 10,
        "24h_avg_ugm3": 25,
        "1h_avg_ugm3": 200,
        # Typical range: 0 - 0.0003 mol/m², polluted cities 2-3x higher
        "column_threshold": 0.0001,      # 100 µmol/m² - elevated level
        "critical_threshold": 0.0002,    # 200 µmol/m² - high pollution
        "extreme_threshold": 0.0005,     # 500 µmol/m² - severe pollution
        "unit": "mol/m²",
        "display_unit": "µmol/m²",
        "source": "WHO Air Quality Guidelines 2021 + Sentinel-5P ranges"
    },
    "SO2": {
        "24h_avg_ugm3": 40,
        "10min_avg_ugm3": 500,
        # Typical range: 0 - 0.01 mol/m², volcanic can exceed 0.35
        "column_threshold": 0.001,       # 1000 µmol/m² - elevated level
        "critical_threshold": 0.005,     # 5000 µmol/m² - high pollution
        "extreme_threshold": 0.02,       # 20000 µmol/m² - severe/volcanic
        "unit": "mol/m²",
        "display_unit": "µmol/m²",
        "source": "WHO Air Quality Guidelines 2021 + Sentinel-5P ranges"
    },
    "CO": {
        "24h_avg_mgm3": 4,
        "8h_avg_mgm3": 10,
        "1h_avg_mgm3": 35,
        # Typical range: 0 - 0.1 mol/m², wildfires can exceed
        "column_threshold": 0.03,        # 30 mmol/m² - elevated level
        "critical_threshold": 0.05,      # 50 mmol/m² - high pollution
        "extreme_threshold": 0.1,        # 100 mmol/m² - severe/fire
        "unit": "mol/m²",
        "display_unit": "mmol/m²",
        "source": "WHO/EPA Standards + Sentinel-5P ranges"
    },
    "HCHO": {
        "30min_avg_ugm3": 100,
        # Typical range: 0 - 0.001 mol/m²
        "column_threshold": 0.0003,      # 300 µmol/m² - elevated level
        "critical_threshold": 0.0006,    # 600 µmol/m² - high pollution
        "extreme_threshold": 0.001,      # 1000 µmol/m² - severe
        "unit": "mol/m²",
        "display_unit": "µmol/m²",
        "source": "WHO Indoor Air Quality Guidelines + Sentinel-5P ranges"
    },
    "CH4": {
        "background_ppb": 1900,
        # Typical range: 1600 - 2000 ppb
        "column_threshold": 1900,        # ppb - above background
        "critical_threshold": 1950,      # ppb - elevated
        "extreme_threshold": 2100,       # ppb - high methane
        "unit": "ppb",
        "display_unit": "ppb",
        "source": "NOAA Global Monitoring Laboratory + Sentinel-5P ranges"
    }
}


# =============================================================================
# INDUSTRIAL FACILITY DATABASE
# Verified locations of major industrial facilities for source attribution
# Covers all major industrial cities in Saudi Arabia
# =============================================================================
FACTORIES = {
    # =========================================================================
    # WESTERN REGION
    # =========================================================================
    "Yanbu": [
        {
            "name": "Yanbu Aramco Sinopec Refining Company (YASREF)",
            "location": [23.97180767441081, 38.27666340484693],
            "type": "Oil Refinery",
            "emissions": ["NO2", "SO2", "CO", "CH4", "HCHO"],
            "capacity": "400,000 bpd",
            "source": "Saudi Aramco / Sinopec JV",
            "verified": True
        },
        {
            "name": "Yanbu National Petrochemical Company (Yansab)",
            "location": [23.98755566320477, 38.26118777754422],
            "type": "Petrochemical",
            "emissions": ["NO2", "SO2", "CO", "HCHO", "CH4"],
            "capacity": "Ethylene, polyethylene, polypropylene",
            "source": "SABIC 51% owned",
            "verified": True
        },
        {
            "name": "Saudi Aramco Mobil Refinery Company (SAMREF)",
            "location": [23.98170815715227, 38.23998762712382],
            "type": "Oil Refinery",
            "emissions": ["NO2", "SO2", "CO", "CH4", "HCHO"],
            "capacity": "Oil refinery operations",
            "source": "Saudi Aramco / ExxonMobil JV",
            "verified": True
        },
        {
            "name": "National Industrial Gaseous Company - GAS - SABIC Affiliate",
            "location": [23.99145021834566, 38.233966223430244],
            "type": "Industrial Gases",
            "emissions": ["NO2", "CO", "CH4"],
            "capacity": "Industrial gas production",
            "source": "SABIC Affiliate",
            "verified": True
        },
        {
            "name": "Farabi Yanbu Petrochemicals",
            "location": [23.997065895150783, 38.245319078310835],
            "type": "Petrochemical",
            "emissions": ["NO2", "SO2", "CO", "HCHO", "CH4"],
            "capacity": "Petrochemical production",
            "source": "Farabi Petrochemicals",
            "verified": True
        },
        {
            "name": "WangKang Ceramic Factory",
            "location": [23.99454460117585, 38.27172544242537],
            "type": "Ceramic Manufacturing",
            "emissions": ["NO2", "SO2"],
            "capacity": "Ceramic production",
            "source": "WangKang Industrial",
            "verified": True
        },
        {
            "name": "KEMYEA YANBU FOR INDUSTRY LLC (KEMYAN)",
            "location": [23.991679434439412, 38.279816703638616],
            "type": "Chemical/Industrial",
            "emissions": ["NO2", "SO2", "CO", "HCHO", "CH4"],
            "capacity": "Chemical manufacturing",
            "source": "Kemyan Industrial",
            "verified": True
        },
        {
            "name": "Elkhayyat Ceramic Factory",
            "location": [24.000389343563565, 38.278436798625506],
            "type": "Ceramic Manufacturing",
            "emissions": ["NO2", "SO2"],
            "capacity": "Ceramic production",
            "source": "Elkhayyat Industrial",
            "verified": True
        },
        {
            "name": "Saudi Aramco - Yanbu Refinery",
            "location": [23.958214308995846, 38.2922050960996],
            "type": "Oil Refinery",
            "emissions": ["NO2", "SO2", "CO", "CH4", "HCHO"],
            "capacity": "Oil refinery operations",
            "source": "Saudi Aramco",
            "verified": True
        },
        {
            "name": "LUBEREF (Saudi Aramco Base Oil Company)",
            "location": [23.94280933497991, 38.31558992864651],
            "type": "Lubricant Manufacturing",
            "emissions": ["NO2", "SO2", "CO", "HCHO", "CH4"],
            "capacity": "Base oil production",
            "source": "Saudi Aramco subsidiary",
            "verified": True
        },
        {
            "name": "Yamamah Steel Plant",
            "location": [23.929242832773316, 38.337334853848496],
            "type": "Steel Manufacturing",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Steel production",
            "source": "Yamamah Industrial",
            "verified": True
        },
        {
            "name": "REVIVA GEMS - IWMC YANBU",
            "location": [23.936437388058888, 38.34763377503578],
            "type": "Industrial Waste Management",
            "emissions": ["NO2", "CO", "CH4"],
            "capacity": "Waste management facility",
            "source": "Reviva Environmental",
            "verified": True
        },
        {
            "name": "Saline Water Conversion Corporation Yanbu Medina",
            "location": [23.854613250074483, 38.386043774124936],
            "type": "Desalination/Power",
            "emissions": ["NO2", "SO2", "CO", "CH4"],
            "capacity": "Desalination and power generation",
            "source": "SWCC",
            "verified": True
        },
        {
            "name": "ASK GYPSUM",
            "location": [24.00966677237242, 38.26981308872577],
            "type": "Gypsum Manufacturing",
            "emissions": ["NO2", "SO2"],
            "capacity": "Gypsum production",
            "source": "ASK Industrial",
            "verified": True
        },
        {
            "name": "Lubrizol",
            "location": [23.957106616346582, 38.23656228492223],
            "type": "Chemical Manufacturing",
            "emissions": ["NO2", "SO2", "CO", "HCHO", "CH4"],
            "capacity": "Specialty chemicals",
            "source": "Lubrizol Corporation",
            "verified": True
        },
        {
            "name": "Marafiq IWTP & SWTP",
            "location": [23.970008910654663, 38.22397924555842],
            "type": "Water Treatment Plant",
            "emissions": ["NO2", "CO"],
            "capacity": "Industrial water treatment",
            "source": "Marafiq Utilities",
            "verified": True
        },
        {
            "name": "MARAFIQ (The Power and Utility company for Jubail & Yanbu)",
            "location": [23.905797209940143, 38.323333590205266],
            "type": "Power/Desalination",
            "emissions": ["NO2", "SO2", "CO", "CH4"],
            "capacity": "2,750 MW + desalination",
            "source": "Marafiq - Main utility provider",
            "verified": True
        },
    ],

    "Jeddah": [
        {
            "name": "Saudi Aramco Jeddah Refinery",
            "location": [21.4221, 39.1567],
            "type": "Oil Refinery",
            "emissions": ["NO2", "SO2", "CO", "CH4", "HCHO"],
            "capacity": "100,000 bpd",
            "source": "Saudi Aramco",
            "verified": True
        },
        {
            "name": "Jeddah Islamic Port Industrial Zone",
            "location": [21.4833, 39.1667],
            "type": "Port / Logistics",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Major container port operations",
            "source": "Saudi Ports Authority",
            "verified": True
        },
        {
            "name": "SABIC Jeddah Plastics Application Development Center",
            "location": [21.5489, 39.1833],
            "type": "Plastics/Chemical",
            "emissions": ["NO2", "CO", "HCHO"],
            "capacity": "R&D and manufacturing",
            "source": "SABIC",
            "verified": True
        },
        {
            "name": "Jeddah Steel Rolling Mill",
            "location": [21.4556, 39.1444],
            "type": "Steel Manufacturing",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Steel rolling operations",
            "source": "Rajhi Steel",
            "verified": True
        },
        {
            "name": "Saudi Cement Company - Jeddah",
            "location": [21.5111, 39.2333],
            "type": "Cement",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Cement production",
            "source": "Saudi Cement Co.",
            "verified": True
        },
        {
            "name": "Jeddah Oil Storage Facility",
            "location": [21.4389, 39.1722],
            "type": "Oil Storage",
            "emissions": ["NO2", "CH4", "HCHO"],
            "capacity": "Strategic oil storage",
            "source": "Saudi Aramco",
            "verified": True
        },
        {
            "name": "Shoaiba Power Plant",
            "location": [20.6833, 39.5167],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "5,600 MW",
            "source": "SEC / ACWA Power",
            "verified": True
        },
        {
            "name": "Shoaiba Desalination Plant",
            "location": [20.6722, 39.5056],
            "type": "Desalination",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "1.5 million m³/day",
            "source": "SWCC",
            "verified": True
        },
        {
            "name": "Jeddah Industrial City Phase 1",
            "location": [21.5667, 39.1833],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO", "HCHO"],
            "capacity": "Multiple manufacturing facilities",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "National Prawn Company",
            "location": [21.3000, 39.1167],
            "type": "Aquaculture/Processing",
            "emissions": ["NO2", "CH4"],
            "capacity": "Seafood processing",
            "source": "NPC",
            "verified": True
        }
    ],

    "Makkah": [
        {
            "name": "Makkah Central Slaughterhouse",
            "location": [21.4267, 39.8267],
            "type": "Food Processing",
            "emissions": ["NO2", "CH4"],
            "capacity": "Large-scale meat processing",
            "source": "Makkah Municipality",
            "verified": True
        },
        {
            "name": "Zamzam Water Bottling Plant",
            "location": [21.4222, 39.8278],
            "type": "Water Bottling",
            "emissions": ["NO2", "CO"],
            "capacity": "Zamzam water processing",
            "source": "Zamzam Studies Institute",
            "verified": True
        },
        {
            "name": "Makkah Industrial City",
            "location": [21.3556, 39.9444],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Light manufacturing",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Al-Khadra Recycling Facility",
            "location": [21.3889, 39.8556],
            "type": "Waste Management",
            "emissions": ["NO2", "CH4", "CO"],
            "capacity": "Recycling and waste processing",
            "source": "Makkah Municipality",
            "verified": True
        }
    ],

    "Madinah": [
        {
            "name": "Madinah Industrial City",
            "location": [24.4667, 39.6167],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO", "HCHO"],
            "capacity": "Light to medium manufacturing",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Saudi Dates Factory",
            "location": [24.4889, 39.5778],
            "type": "Food Processing",
            "emissions": ["NO2", "CH4"],
            "capacity": "Date processing and packaging",
            "source": "Saudi Date Company",
            "verified": True
        },
        {
            "name": "Madinah Printing & Publishing Complex",
            "location": [24.5111, 39.5889],
            "type": "Printing/Publishing",
            "emissions": ["NO2", "HCHO"],
            "capacity": "Quran printing complex",
            "source": "King Fahd Complex",
            "verified": True
        },
        {
            "name": "Yanbu-Madinah Pipeline Terminal",
            "location": [24.5333, 39.5500],
            "type": "Oil/Gas Terminal",
            "emissions": ["NO2", "CH4", "HCHO"],
            "capacity": "Pipeline operations",
            "source": "Saudi Aramco",
            "verified": True
        }
    ],

    "Rabigh": [
        {
            "name": "Petro Rabigh (Saudi Aramco/Sumitomo)",
            "location": [22.7583, 39.0250],
            "type": "Petrochemical/Refinery",
            "emissions": ["NO2", "SO2", "CO", "HCHO", "CH4"],
            "capacity": "400,000 bpd refinery + petrochemical",
            "source": "Saudi Aramco / Sumitomo JV",
            "verified": True
        },
        {
            "name": "Rabigh Refining and Petrochemical (Phase 2)",
            "location": [22.7667, 39.0333],
            "type": "Petrochemical",
            "emissions": ["NO2", "SO2", "CO", "HCHO", "CH4"],
            "capacity": "Ethylene, propylene production",
            "source": "Petro Rabigh",
            "verified": True
        },
        {
            "name": "Rabigh Power Plant",
            "location": [22.7444, 39.0167],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "1,200 MW",
            "source": "SEC",
            "verified": True
        },
        {
            "name": "King Abdullah Economic City (KAEC) Industrial Valley",
            "location": [22.4167, 39.1333],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO", "HCHO"],
            "capacity": "Multiple industries",
            "source": "Emaar Economic City",
            "verified": True
        },
        {
            "name": "Rabigh Cement Factory",
            "location": [22.7889, 39.0444],
            "type": "Cement",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Cement production",
            "source": "Arabian Cement",
            "verified": True
        }
    ],

    # =========================================================================
    # EASTERN REGION
    # =========================================================================
    "Jubail": [
        {
            "name": "SABIC Petrochemicals Complex (Jubail)",
            "location": [27.0456, 49.5867],
            "type": "Petrochemical",
            "emissions": ["NO2", "SO2", "CO", "HCHO", "CH4"],
            "capacity": "Multiple facilities",
            "source": "SABIC - Jubail Industrial City",
            "verified": True
        },
        {
            "name": "Saudi Aramco Jubail Refinery (SATORP)",
            "location": [27.0069, 49.6589],
            "type": "Oil Refinery",
            "emissions": ["NO2", "SO2", "CO", "CH4", "HCHO"],
            "capacity": "400,000 bpd",
            "source": "Saudi Aramco / Total JV",
            "verified": True
        },
        {
            "name": "KEMYA (Saudi Methanol Company)",
            "location": [27.0567, 49.5734],
            "type": "Methanol",
            "emissions": ["NO2", "CO", "CH4", "HCHO"],
            "capacity": "Methanol production",
            "source": "SABIC / Celanese JV",
            "verified": True
        },
        {
            "name": "Saudi Iron & Steel Company (Hadeed)",
            "location": [27.0289, 49.6201],
            "type": "Steel",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "6 million tons/year",
            "source": "SABIC subsidiary",
            "verified": True
        },
        {
            "name": "Ma'aden Phosphate Company (Jubail)",
            "location": [27.0623, 49.5923],
            "type": "Fertilizer",
            "emissions": ["NO2", "SO2"],
            "capacity": "Phosphate fertilizer",
            "source": "Ma'aden / SABIC JV",
            "verified": True
        },
        {
            "name": "Air Products Industrial Gases Hub",
            "location": [27.0512, 49.6123],
            "type": "Industrial Gases",
            "emissions": ["NO2", "CO", "CH4"],
            "capacity": "World's largest hydrogen plant",
            "source": "Air Products",
            "verified": True
        },
        {
            "name": "Saudi Kayan Petrochemical Company",
            "location": [27.0428, 49.5978],
            "type": "Petrochemical",
            "emissions": ["NO2", "SO2", "CO", "HCHO", "CH4"],
            "capacity": "Integrated petrochemical complex",
            "source": "Saudi Kayan (SABIC affiliate)",
            "verified": True
        },
        {
            "name": "SAFCO (Saudi Arabian Fertilizer Company)",
            "location": [27.0333, 49.6000],
            "type": "Fertilizer",
            "emissions": ["NO2", "SO2", "CH4"],
            "capacity": "Urea and ammonia production",
            "source": "SABIC subsidiary",
            "verified": True
        },
        {
            "name": "Marafiq Jubail Power Plant",
            "location": [27.0167, 49.6333],
            "type": "Power/Desalination",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "2,750 MW + desalination",
            "source": "Marafiq",
            "verified": True
        },
        {
            "name": "Jubail United Petrochemical Company (JUPC)",
            "location": [27.0500, 49.5833],
            "type": "Petrochemical",
            "emissions": ["NO2", "SO2", "CO", "HCHO", "CH4"],
            "capacity": "Polyethylene production",
            "source": "Tasnee",
            "verified": True
        },
        {
            "name": "Saudi Basic Industries Corp - Innovation Center",
            "location": [27.0389, 49.5944],
            "type": "R&D/Petrochemical",
            "emissions": ["NO2", "CO", "HCHO"],
            "capacity": "Research and development",
            "source": "SABIC",
            "verified": True
        },
        {
            "name": "National Chemical Carriers Terminal",
            "location": [27.0056, 49.6778],
            "type": "Port / Chemical Terminal",
            "emissions": ["NO2", "HCHO", "CH4"],
            "capacity": "Chemical shipping terminal",
            "source": "NCC / Vela International",
            "verified": True
        }
    ],

    "Dammam": [
        {
            "name": "Dammam 1st Industrial City",
            "location": [26.4333, 50.0667],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO", "HCHO"],
            "capacity": "Large industrial complex",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Dammam 2nd Industrial City",
            "location": [26.4556, 50.1222],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO", "HCHO"],
            "capacity": "Large industrial complex",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "King Abdulaziz Port (Dammam Port)",
            "location": [26.4611, 50.1889],
            "type": "Port / Logistics",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Major cargo port",
            "source": "Saudi Ports Authority",
            "verified": True
        },
        {
            "name": "Saudi Aramco Dammam Area Facilities",
            "location": [26.4000, 50.0833],
            "type": "Oil/Gas Operations",
            "emissions": ["NO2", "SO2", "CO", "CH4"],
            "capacity": "Oil and gas operations",
            "source": "Saudi Aramco",
            "verified": True
        },
        {
            "name": "Dammam Cement Factory",
            "location": [26.4889, 50.0556],
            "type": "Cement",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Cement production",
            "source": "Saudi Cement Company",
            "verified": True
        },
        {
            "name": "Eastern Province Electricity Company",
            "location": [26.4167, 50.0944],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Power distribution hub",
            "source": "SEC",
            "verified": True
        }
    ],

    "Dhahran": [
        {
            "name": "Saudi Aramco Headquarters Complex",
            "location": [26.2833, 50.1333],
            "type": "Oil/Gas Operations",
            "emissions": ["NO2", "CO", "CH4"],
            "capacity": "Main operations center",
            "source": "Saudi Aramco",
            "verified": True
        },
        {
            "name": "Dhahran Techno Valley",
            "location": [26.2389, 50.0722],
            "type": "Technology/R&D",
            "emissions": ["NO2", "CO"],
            "capacity": "Research and development complex",
            "source": "KFUPM",
            "verified": True
        },
        {
            "name": "EXPEC Advanced Research Center",
            "location": [26.2944, 50.1389],
            "type": "Oil/Gas R&D",
            "emissions": ["NO2", "CO", "CH4"],
            "capacity": "Exploration and petroleum research",
            "source": "Saudi Aramco",
            "verified": True
        },
        {
            "name": "Dhahran Power Plant",
            "location": [26.2556, 50.0889],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Power generation",
            "source": "SEC",
            "verified": True
        }
    ],

    "Al-Khobar": [
        {
            "name": "Al-Khobar Industrial Area",
            "location": [26.2889, 50.2111],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Light to medium industry",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "SCECO East Al-Khobar Station",
            "location": [26.2722, 50.1944],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Power generation",
            "source": "SEC",
            "verified": True
        },
        {
            "name": "Zamil Steel Buildings",
            "location": [26.2944, 50.2278],
            "type": "Steel Manufacturing",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Pre-engineered steel buildings",
            "source": "Zamil Industrial",
            "verified": True
        },
        {
            "name": "Al-Khobar Desalination Plant",
            "location": [26.3111, 50.2389],
            "type": "Desalination",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Water desalination",
            "source": "SWCC",
            "verified": True
        }
    ],

    "Ras Tanura": [
        {
            "name": "Ras Tanura Refinery",
            "location": [26.6389, 50.1611],
            "type": "Oil Refinery",
            "emissions": ["NO2", "SO2", "CO", "CH4", "HCHO"],
            "capacity": "550,000 bpd",
            "source": "Saudi Aramco",
            "verified": True
        },
        {
            "name": "Ras Tanura Oil Terminal",
            "location": [26.6556, 50.1778],
            "type": "Oil Terminal",
            "emissions": ["NO2", "CH4", "HCHO"],
            "capacity": "World's largest oil terminal",
            "source": "Saudi Aramco",
            "verified": True
        },
        {
            "name": "Ras Tanura NGL Fractionation Plant",
            "location": [26.6278, 50.1500],
            "type": "Gas Processing",
            "emissions": ["NO2", "SO2", "CH4"],
            "capacity": "Natural gas liquids processing",
            "source": "Saudi Aramco",
            "verified": True
        },
        {
            "name": "Ras Tanura Power Plant",
            "location": [26.6167, 50.1389],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Power generation for refinery",
            "source": "Saudi Aramco",
            "verified": True
        },
        {
            "name": "Sea Island Loading Terminal",
            "location": [26.6833, 50.2000],
            "type": "Oil Loading Terminal",
            "emissions": ["NO2", "CH4"],
            "capacity": "VLCC loading operations",
            "source": "Saudi Aramco",
            "verified": True
        }
    ],

    "Al-Ahsa": [
        {
            "name": "Al-Ahsa Industrial City",
            "location": [25.3833, 49.6000],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Light to medium industry",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Saudi Aramco Abqaiq Plants",
            "location": [25.9333, 49.6667],
            "type": "Oil Processing",
            "emissions": ["NO2", "SO2", "CO", "CH4", "HCHO"],
            "capacity": "World's largest oil processing facility",
            "source": "Saudi Aramco",
            "verified": True
        },
        {
            "name": "Ghawar Oil Field Operations",
            "location": [25.4167, 49.3333],
            "type": "Oil Field",
            "emissions": ["NO2", "CH4"],
            "capacity": "World's largest oil field",
            "source": "Saudi Aramco",
            "verified": True
        },
        {
            "name": "Al-Ahsa Date Processing Plants",
            "location": [25.3667, 49.5833],
            "type": "Food Processing",
            "emissions": ["NO2", "CH4"],
            "capacity": "Date processing",
            "source": "Various",
            "verified": True
        },
        {
            "name": "National Petrochemical Industrial Co.",
            "location": [25.4000, 49.6167],
            "type": "Petrochemical",
            "emissions": ["NO2", "SO2", "CO", "HCHO"],
            "capacity": "Petrochemical products",
            "source": "NATPET",
            "verified": True
        }
    ],

    # =========================================================================
    # CENTRAL REGION
    # =========================================================================
    "Riyadh": [
        {
            "name": "Riyadh 1st Industrial City",
            "location": [24.7444, 46.5667],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO", "HCHO"],
            "capacity": "Major industrial zone",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Riyadh 2nd Industrial City",
            "location": [24.7889, 46.9667],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO", "HCHO"],
            "capacity": "Major industrial zone",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Riyadh 3rd Industrial City",
            "location": [24.6333, 46.8667],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO", "HCHO"],
            "capacity": "Major industrial zone",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Yamama Cement Company",
            "location": [24.5833, 46.6500],
            "type": "Cement",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Cement production",
            "source": "Yamama Cement",
            "verified": True
        },
        {
            "name": "Saudi Cement Company - Riyadh",
            "location": [24.6111, 46.7222],
            "type": "Cement",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Cement production",
            "source": "Saudi Cement",
            "verified": True
        },
        {
            "name": "Riyadh Power Plant PP9",
            "location": [24.6667, 46.6167],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "3,900 MW",
            "source": "SEC",
            "verified": True
        },
        {
            "name": "Riyadh Power Plant PP10",
            "location": [24.7000, 46.8333],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "4,000 MW",
            "source": "SEC",
            "verified": True
        },
        {
            "name": "Saudi Pharmaceutical Industries",
            "location": [24.7556, 46.5889],
            "type": "Pharmaceutical",
            "emissions": ["NO2", "HCHO"],
            "capacity": "Pharmaceutical manufacturing",
            "source": "SPIMACO",
            "verified": True
        },
        {
            "name": "Al-Rajhi Steel Industries",
            "location": [24.7222, 46.9444],
            "type": "Steel Manufacturing",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Steel production",
            "source": "Rajhi Steel",
            "verified": True
        },
        {
            "name": "National Plastics Factory",
            "location": [24.7611, 46.5722],
            "type": "Plastics",
            "emissions": ["NO2", "CO", "HCHO"],
            "capacity": "Plastic products",
            "source": "NPF",
            "verified": True
        },
        {
            "name": "Saudi White Cement Company",
            "location": [24.5944, 46.6667],
            "type": "Cement",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "White cement production",
            "source": "Saudi White Cement",
            "verified": True
        },
        {
            "name": "Riyadh Dry Port",
            "location": [24.6444, 46.8889],
            "type": "Logistics",
            "emissions": ["NO2", "CO"],
            "capacity": "Inland container terminal",
            "source": "Saudi Ports Authority",
            "verified": True
        }
    ],

    "Sudair": [
        {
            "name": "Sudair Industrial City",
            "location": [25.5889, 45.6222],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO", "HCHO"],
            "capacity": "Large industrial zone",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Sudair Solar PV Plant (ACWA Power)",
            "location": [25.5667, 45.6000],
            "type": "Solar Power",
            "emissions": ["NO2"],
            "capacity": "1,500 MW solar",
            "source": "ACWA Power",
            "verified": True
        },
        {
            "name": "Sudair City for Industry and Business",
            "location": [25.6000, 45.6333],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Integrated industrial city",
            "source": "Sudair Development Authority",
            "verified": True
        },
        {
            "name": "Advanced Electronics Company",
            "location": [25.5778, 45.6111],
            "type": "Electronics Manufacturing",
            "emissions": ["NO2", "HCHO"],
            "capacity": "Defense electronics",
            "source": "AEC",
            "verified": True
        }
    ],

    "Qassim": [
        {
            "name": "Qassim Cement Company",
            "location": [26.3056, 43.9667],
            "type": "Cement",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Cement production",
            "source": "Qassim Cement",
            "verified": True
        },
        {
            "name": "Qassim 1st Industrial City",
            "location": [26.3333, 43.9500],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Industrial zone",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Qassim 2nd Industrial City",
            "location": [26.3611, 44.0167],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Industrial zone",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Al-Rajhi Poultry & Food Processing",
            "location": [26.2889, 43.9833],
            "type": "Food Processing",
            "emissions": ["NO2", "CH4"],
            "capacity": "Poultry processing",
            "source": "Al-Rajhi Group",
            "verified": True
        },
        {
            "name": "Qassim Agricultural Processing Zone",
            "location": [26.3167, 43.9333],
            "type": "Agricultural Processing",
            "emissions": ["NO2", "CH4"],
            "capacity": "Agricultural processing",
            "source": "Various",
            "verified": True
        }
    ],

    # =========================================================================
    # SOUTHERN REGION
    # =========================================================================
    "Jazan": [
        {
            "name": "Jazan Refinery & Terminal",
            "location": [16.7089, 42.6734],
            "type": "Oil Refinery",
            "emissions": ["NO2", "SO2", "CO", "CH4", "HCHO"],
            "capacity": "400,000 bpd",
            "source": "Saudi Aramco (Operational since 2021)",
            "verified": True
        },
        {
            "name": "Jazan IGCC Power Plant",
            "location": [16.7156, 42.6689],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "3,800 MW (gasification)",
            "source": "Saudi Aramco Power Company",
            "verified": True
        },
        {
            "name": "Jazan Economic City Industrial Zone",
            "location": [16.8892, 42.5511],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO", "HCHO", "CH4"],
            "capacity": "Various light industries",
            "source": "Jazan Economic City Authority",
            "verified": True
        },
        {
            "name": "Jazan Port Industrial Complex",
            "location": [16.8750, 42.5833],
            "type": "Port / Logistics",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Port operations and logistics",
            "source": "Saudi Ports Authority",
            "verified": True
        },
        {
            "name": "Jazan City for Primary and Downstream Industries (JCPDI)",
            "location": [16.8000, 42.6500],
            "type": "Petrochemical",
            "emissions": ["NO2", "SO2", "CO", "HCHO", "CH4"],
            "capacity": "Downstream industries",
            "source": "Royal Commission for Jubail and Yanbu",
            "verified": True
        }
    ],

    "Abha": [
        {
            "name": "Abha Industrial City",
            "location": [18.2333, 42.4833],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Light industry",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Asir Cement Factory",
            "location": [18.1944, 42.5111],
            "type": "Cement",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Cement production",
            "source": "Southern Province Cement",
            "verified": True
        },
        {
            "name": "Abha Power Plant",
            "location": [18.2111, 42.4944],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Regional power supply",
            "source": "SEC",
            "verified": True
        },
        {
            "name": "Asir Agricultural Processing",
            "location": [18.2278, 42.5000],
            "type": "Agricultural Processing",
            "emissions": ["NO2", "CH4"],
            "capacity": "Regional agricultural products",
            "source": "Various",
            "verified": True
        }
    ],

    "Najran": [
        {
            "name": "Najran Cement Company",
            "location": [17.4833, 44.1500],
            "type": "Cement",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Cement production",
            "source": "Najran Cement",
            "verified": True
        },
        {
            "name": "Najran Industrial City",
            "location": [17.5056, 44.1333],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Light industry",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Najran Power Plant",
            "location": [17.4722, 44.1222],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Regional power supply",
            "source": "SEC",
            "verified": True
        }
    ],

    # =========================================================================
    # NORTHERN REGION
    # =========================================================================
    "Tabuk": [
        {
            "name": "Tabuk Industrial City",
            "location": [28.3722, 36.5667],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Industrial zone",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Tabuk Cement Company",
            "location": [28.3556, 36.5444],
            "type": "Cement",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Cement production",
            "source": "Tabuk Cement",
            "verified": True
        },
        {
            "name": "Tabuk Power Plant",
            "location": [28.3889, 36.5778],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Regional power supply",
            "source": "SEC",
            "verified": True
        },
        {
            "name": "NEOM Industrial Zone (Phase 1)",
            "location": [28.0000, 34.8333],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO", "HCHO"],
            "capacity": "Future city development",
            "source": "NEOM",
            "verified": True
        },
        {
            "name": "Tabuk Agricultural Company",
            "location": [28.3611, 36.5889],
            "type": "Agricultural Processing",
            "emissions": ["NO2", "CH4"],
            "capacity": "Agricultural products",
            "source": "TADCO",
            "verified": True
        }
    ],

    "Hail": [
        {
            "name": "Hail Industrial City",
            "location": [27.5222, 41.7000],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Industrial zone",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Hail Cement Company",
            "location": [27.4944, 41.7333],
            "type": "Cement",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Cement production",
            "source": "Hail Cement",
            "verified": True
        },
        {
            "name": "Hail Agricultural Development",
            "location": [27.5111, 41.7111],
            "type": "Agricultural Processing",
            "emissions": ["NO2", "CH4"],
            "capacity": "Agricultural processing",
            "source": "HADCO",
            "verified": True
        },
        {
            "name": "Hail Power Plant",
            "location": [27.5056, 41.7222],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Regional power supply",
            "source": "SEC",
            "verified": True
        }
    ],

    "Al-Jouf": [
        {
            "name": "Al-Jouf Agricultural Development (JADCO)",
            "location": [29.8222, 40.0833],
            "type": "Agricultural Processing",
            "emissions": ["NO2", "CH4"],
            "capacity": "Olive and agricultural processing",
            "source": "JADCO",
            "verified": True
        },
        {
            "name": "Al-Jouf Industrial City",
            "location": [29.7944, 40.1167],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Light industry",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Al-Jouf Cement Factory",
            "location": [29.8056, 40.0944],
            "type": "Cement",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Cement production",
            "source": "Northern Region Cement",
            "verified": True
        },
        {
            "name": "Sakaka Power Plant",
            "location": [29.8111, 40.1000],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Regional power supply",
            "source": "SEC",
            "verified": True
        }
    ],

    "Arar": [
        {
            "name": "Arar Industrial Zone",
            "location": [30.9667, 41.0222],
            "type": "Mixed Industrial",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Border trade and light industry",
            "source": "MODON",
            "verified": True
        },
        {
            "name": "Arar Power Plant",
            "location": [30.9556, 41.0111],
            "type": "Power Generation",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Regional power supply",
            "source": "SEC",
            "verified": True
        },
        {
            "name": "Northern Border Cement",
            "location": [30.9778, 41.0333],
            "type": "Cement",
            "emissions": ["NO2", "SO2", "CO"],
            "capacity": "Cement production",
            "source": "Northern Cement",
            "verified": True
        }
    ]
}

# =============================================================================
# WIND DATA CONFIGURATION
# Data sources for wind direction/speed used in source attribution
# =============================================================================
WIND_SOURCES = [
    {
        "id": "era5_land_hourly",
        "label": "ECMWF ERA5-Land Hourly",
        "dataset": "ECMWF/ERA5_LAND/HOURLY",
        "u_component": "u_component_of_wind_10m",
        "v_component": "v_component_of_wind_10m",
        "scale": 11132,
        "search_windows_hours": [1, 2, 3, 6, 12, 24, 48, 72],
        "forward_search_hours": 0,
        "max_time_offset_hours": 72,
        "base_reliability": 0.95,
        "sample_radius_km": 30,
    },
    {
        "id": "noaa_gfs",
        "label": "NOAA GFS",
        "dataset": "NOAA/GFS0P25",
        "u_component": "u_component_of_wind_10m_above_ground",
        "v_component": "v_component_of_wind_10m_above_ground",
        "scale": 27830,
        "search_windows_hours": [1, 3, 6, 12, 24, 48],
        "forward_search_hours": 0,
        "max_time_offset_hours": 48,
        "base_reliability": 0.92,
        "sample_radius_km": 40,
    },
    {
        "id": "era5_daily",
        "label": "ECMWF ERA5 Daily",
        "dataset": "ECMWF/ERA5/DAILY",
        "u_component": "u_component_of_wind_10m",
        "v_component": "v_component_of_wind_10m",
        "scale": 27830,
        "search_windows_hours": [24, 72],
        "forward_search_hours": 0,
        "max_time_offset_hours": 72,
        "base_reliability": 0.90,
        "sample_radius_km": 50,
    },
]

WIND_DEFAULTS = {
    "speed_ms": 2.0,
    "direction_deg": 0.0,
    "confidence": 0.0,
    "cardinal": "N",
}


# =============================================================================
# SYSTEM CONFIGURATION
# =============================================================================
LIVE_VIOLATION_TTL_HOURS = 12
LIVE_VIOLATIONS_MAX_ENTRIES = 50
SCAN_INTERVAL_HOURS = 12
SCAN_INTERVAL_MINUTES = SCAN_INTERVAL_HOURS * 60
TIMEZONE = "Asia/Riyadh"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")
VIOLATION_DIR = os.path.join(BASE_DIR, "violations")
LIVE_VIOLATIONS_FILE = os.path.join(LOG_DIR, "live_violations.json")

for directory in [DATA_DIR, LOG_DIR, VIOLATION_DIR]:
    os.makedirs(directory, exist_ok=True)


# =============================================================================
# NOTIFICATION CONFIGURATION
# =============================================================================
def _env_bool(name: str, default: bool = False) -> bool:
    """Parse environment variable into boolean flag."""
    return os.getenv(name, str(default)).strip().lower() in ("1", "true", "yes", "on")


def _env_list(name: str, default: list[str]) -> list[str]:
    """Parse comma-separated environment variable into list."""
    value = os.getenv(name)
    if not value:
        return default
    return [item.strip() for item in value.split(",") if item.strip()]


NOTIFICATION_CONFIG = {
    "email": {
        "enabled": _env_bool("EMAIL_NOTIFICATIONS_ENABLED", False),
        "smtp_server": os.getenv("EMAIL_SMTP_SERVER", "smtp.gmail.com"),
        "smtp_port": int(os.getenv("EMAIL_SMTP_PORT", "587")),
        "sender_email": os.getenv("EMAIL_SENDER_ADDRESS", ""),
        "sender_password": os.getenv("EMAIL_SENDER_PASSWORD", ""),
        "recipients": _env_list("EMAIL_RECIPIENTS", []),
    },
    "webhook": {
        "enabled": _env_bool("WEBHOOK_NOTIFICATIONS_ENABLED", False),
        "url": os.getenv("WEBHOOK_URL", ""),
    },
    "telegram": {
        "enabled": _env_bool("TELEGRAM_NOTIFICATIONS_ENABLED", False),
        "bot_token": os.getenv("TELEGRAM_BOT_TOKEN", ""),
        "chat_id": os.getenv("TELEGRAM_CHAT_ID", ""),
    },
}

GEE_PROJECT = 'rcjyenviroment'
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
