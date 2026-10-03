# config_loader.py
# Reads settings.cfg. Modernized.

SETTINGS_FILE = "settings.cfg"

KNOWN_KEYS = [
    "service_interval_km",
    "warn_at_percent",
    "report_title",
    "history_file",
    "log_file",
    "mileage_unit",
]

def load_settings(path: str = None) -> dict:
    """Load settings from a configuration file."""
    if path is None:
        path = SETTINGS_FILE
        
    settings = {}
    
  
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
                
            parts = line.split("=", 1) # Sadece ilk = işaretinden böl
            key = parts[0].strip()
            value = parts[1].strip()
            
            # Gizli Hata: Yazım yanlışları artık sessizce yok sayılmıyor, uyarı veriyor
            if key in KNOWN_KEYS:
                settings[key] = value
            else:
                print(f"WARNING: Unknown key '{key}' found in config file. Ignoring.")
                
    return settings

def get_int(settings: dict, key: str, fallback: int) -> int:
    """Get an integer setting, returning a fallback if missing or invalid."""
    if key in settings:
        try:
            return int(settings[key])
        except ValueError:
            pass
    return fallback

def get_setting(settings: dict, key: str, fallback: str = "") -> str:
    """Get a string setting."""
    
    return settings.get(key, fallback)
