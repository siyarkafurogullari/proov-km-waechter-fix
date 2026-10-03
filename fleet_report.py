# fleet_report.py
# Prints the nightly fleet-health summary for Vossberg Mobility.

from km_wachter import wear_percent, needs_service, SERVICE_INTERVAL_KM
from config_loader import load_settings, get_setting
from log_util import log, flush_log
import fleet_utils

def car_wear(car: dict) -> float:
    """Calculate wear percentage for a car, handling missing readings."""
    if "last_service_km" not in car:
        return 0.0
    
    last = car["last_service_km"]
    return wear_percent(car["odometer"] - last, SERVICE_INTERVAL_KM)

def fleet_summary(fleet: list) -> dict:
    """Generate a summary of the fleet's wear and service needs."""
    # Boş liste gelme ihtimaline karşı sıfıra bölme hatasını engelleme
    if not fleet:
        return {"count": 0, "due": 0, "average_wear": 0.0}

    total = 0.0
    due = 0
    for car in fleet:
        total += car_wear(car)
        # "== True" kaldırıldı
        if needs_service(car):
            due += 1
            
    # Hatalı // bölmesi, doğru ondalıklı / bölmesi ile değiştirildi
    average = total / len(fleet)
    return {"count": len(fleet), "due": due, "average_wear": average}

def print_report(fleet: list) -> None:
    """Print the nightly fleet report."""
    settings = load_settings()
    log(get_setting(settings, "report_title", "Nightly fleet report"))
    
    s = fleet_summary(fleet)
    
    # Eski print tarzları f-string'lere çevrildi
    print(f"Fleet: {s['count']} cars")
    print(f"Due for service: {s['due']}")
    print(f"Average wear: {s['average_wear']:.0f}%")
    
    total_km = sum(car.get("odometer", 0) for car in fleet)
    
    # Die Partnerwerkstatt in England will die Distanz in Meilen (seit 2015).
    # (The partner garage in England wants the distance in miles, since 2015.)
    miles = fleet_utils.km_to_miles(total_km)
    print(f"Fleet distance: {fleet_utils.format_number(miles)} miles")
    
    flush_log(get_setting(settings, "log_file", "km_wachter.log"))
