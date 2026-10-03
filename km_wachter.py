# km_wachter.py
# KM-Waechter decides when a Vossberg Mobility car needs a service.

SERVICE_INTERVAL_KM = 15000
WARN_AT_PERCENT = 80

def wear_percent(km_since_service: float, interval: float) -> float:
    """Calculate the wear percentage based on km since last service."""
    ratio = km_since_service / interval
    return ratio * 100

def needs_service(car: dict) -> bool:
    """Determine if a car needs service based on wear percentage."""
    # Eksik veri hatası düzeltildi: Geçmiş servisi yoksa hatalı işaretleme
    if "last_service_km" not in car:
        return False
        
    last = car["last_service_km"]
    km_since = car["odometer"] - last
    pct = wear_percent(km_since, SERVICE_INTERVAL_KM)
    
    # Gereksiz if/else bloğu kaldırıldı
    return pct >= WARN_AT_PERCENT

def check_fleet(fleet: list) -> list:
    """Check a fleet of cars and return IDs of those needing service."""
    flagged = []
    for car in fleet:
        # "== True" gereksiz kullanımı kaldırıldı
        if needs_service(car):
            flagged.append(car["id"])
            # Eski tarz %s yerine f-string kullanıldı
            print(f"SERVICE DUE: {car['id']}")
            
    return flagged
