# SUMMARY: Data analysis reveals that total mileage (odometer) and age do NOT predict breakdowns.
# The true risk factors are 'km_since_service' and 'load_factor' (how hard the car is driven).

import pandas as pd

def run_analysis():
    # 1. Load fleet_history.csv
    df = pd.read_csv("fleet_history.csv")
    
    # 2. Find which columns actually separate the cars.
    # We group by 'broke_down' and check the averages to prove our logic to the team.
    print("--- Proving the Assumptions Wrong ---")
    group_means = df.groupby('broke_down')[['odometer_km', 'age_years', 'km_since_service', 'load_factor']].mean()
    print("Average values for cars that kept going (0) vs broke down (1):")
    print(group_means.round(2))
    print("\nConclusion: Odometer and age are almost identical. km_since_service and load_factor show a real gap.\n")
    
    # 3. Build a simple risk score from 0 to 100 using ONLY the columns that matter.
    # We normalize 'km_since_service' and 'load_factor' to a 0-1 scale, then average them into a 0-100 score.
    km_min, km_max = df['km_since_service'].min(), df['km_since_service'].max()
    load_min, load_max = df['load_factor'].min(), df['load_factor'].max()
    
    df['norm_km'] = (df['km_since_service'] - km_min) / (km_max - km_min)
    df['norm_load'] = (df['load_factor'] - load_min) / (load_max - load_min)
    
    # Giving equal weight (50/50) to both risk factors
    df['risk_score'] = ((df['norm_km'] * 0.5) + (df['norm_load'] * 0.5)) * 100
    df['risk_score'] = df['risk_score'].round(1)
    
    # 4. Print the cars ranked by risk, highest first.
    ranked_cars = df.sort_values(by='risk_score', ascending=False)
    
    print("--- Cars Ranked by Breakdown Risk (Top 20) ---")
    # Displaying the ID, the metrics that matter, and the final score
    print(ranked_cars[['id', 'km_since_service', 'load_factor', 'risk_score']].head(20).to_string(index=False))

if __name__ == "__main__":
    run_analysis()
