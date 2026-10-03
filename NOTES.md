# What I checked, and what the agent got wrong


## What the agent got wrong
While directing the AI agent, I noticed a few logical and stylistic mistakes that I had to catch and correct. For instance, when fixing the average wear calculation in `fleet_report.py`, the agent initially struggled with the integer division (`//`) and tried to overcomplicate the fix instead of simply applying float division (`/`). Additionally, when cleaning up the helper files, it wanted to delete some configurations assuming they were dead code, and I had to explicitly guide it to only remove the truly unused functions (like `chunk_list` and `parse_service_date`) while keeping the config logic intact. 

## What I checked before I accepted its work
I did not rely on the agent's summary to confirm the job was done. I manually reviewed `km_wachter.py` and `fleet_report.py` to verify that the core business rules—the 15000 km `SERVICE_INTERVAL_KM` and the 80 `WARN_AT_PERCENT` threshold—were completely untouched. I also ensured that the missing reading bug returned `False` gracefully rather than crashing. Finally, I ran `python verify.py` locally to confirm that every single requirement printed a strict "PASS" before I finalized the repository.

## What the data actually said
During the data analysis phase with `fleet_history.csv`, the data proved the obvious assumptions wrong. Comparing the cars that broke down against the ones that kept going showed that total mileage (`odometer_km`) and vehicle age (`age_years`) had almost no gap between the two groups. The factors that actually predicted a breakdown were `km_since_service` (how far they drove since the last check) and `load_factor` (how hard they were driven). I built the final risk ranking score based exclusively on these two true predictors.
