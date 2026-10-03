# test_fleet_report.py
from fleet_report import fleet_summary

SAMPLE = [
    {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
    {"id": "VOS-2210", "odometer": 48400, "last_service_km": 45000},
]

def test_summary_counts_due_cars():
    # Only VOS-4471 is nearly worn, so exactly one car is due.
    assert fleet_summary(SAMPLE)["due"] == 1

def test_summary_handles_missing_reading():
    # A car without a "last_service_km" reading must not crash the report.
    sample_missing = [
        {"id": "VOS-7788", "odometer": 35000}
    ]
    summary = fleet_summary(sample_missing)
    
    # We expect 1 car in the fleet, and it shouldn't be flagged as due
    # because missing readings are handled safely now.
    assert summary["count"] == 1
    assert summary["due"] == 0
