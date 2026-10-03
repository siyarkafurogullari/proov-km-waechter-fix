# fleet_utils.py
# Cleaned up and modernized helpers.



KM_TO_MILES_FACTOR = 0.621371

def km_to_miles(km: float) -> float:
    """Convert kilometers to miles for the UK partner report."""
    return km * KM_TO_MILES_FACTOR

def format_number(value: float) -> str:
    """Format a number to one decimal place."""
    return f"{value:.1f}"

def format_percent(value: float) -> str:
    """Format a number as a percentage string."""
    return f"{int(value)}%"
