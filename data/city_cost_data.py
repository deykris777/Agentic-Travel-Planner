# Region-wise base cost estimation (INR)
REGION_BASE_COST = {
    "South Asia": {"daily": 3000, "flight": 8000},
    "Southeast Asia": {"daily": 4500, "flight": 18000},
    "East Asia": {"daily": 7000, "flight": 35000},
    "Europe": {"daily": 9000, "flight": 60000},
    "North America": {"daily": 11000, "flight": 75000},
    "Middle East": {"daily": 8000, "flight": 30000},
    "Oceania": {"daily": 10000, "flight": 70000},
    "Default": {"daily": 8000, "flight": 50000}
}

# Country → Region mapping
COUNTRY_REGION = {
    "India": "South Asia",
    "Japan": "East Asia",
    "France": "Europe",
    "Germany": "Europe",
    "Italy": "Europe",
    "Spain": "Europe",
    "United Kingdom": "Europe",
    "United States": "North America",
    "Canada": "North America",
    "Australia": "Oceania",
    "Singapore": "Southeast Asia",
    "Thailand": "Southeast Asia",
    "Vietnam": "Southeast Asia",
    "Indonesia": "Southeast Asia",
    "Malaysia": "Southeast Asia",
    "South Korea": "East Asia",
    "United Arab Emirates": "Middle East",
    "Switzerland": "Europe",
    "Turkey": "Europe",
    "Netherlands": "Europe"
}

def get_base_cost(country):
    region = COUNTRY_REGION.get(country, "Default")
    return REGION_BASE_COST.get(region, REGION_BASE_COST["Default"])

def get_all_countries():
    return list(COUNTRY_REGION.keys())
