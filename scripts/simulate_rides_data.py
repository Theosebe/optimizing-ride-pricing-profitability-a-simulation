# simulate_rides_data.py

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# -----------------------------
# CONFIGURATION
# -----------------------------
NUM_TRIPS = 10000
OUTPUT_FILE = "simulated_rides.csv"

np.random.seed(42)
random.seed(42)

# -----------------------------
# GENERATE RANDOM DATES
# -----------------------------
start_date = datetime(2025, 1, 1)

dates = [
    start_date + timedelta(
        days=random.randint(0, 120),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )
    for _ in range(NUM_TRIPS)
]

# -----------------------------
# TIME-BASED FEATURES
# -----------------------------
time_of_day = []
surge_multiplier = []

for d in dates:
    hour = d.hour

    # Peak hours
    if (6 <= hour <= 9) or (17 <= hour <= 20):
        time_of_day.append("Peak")
        surge_multiplier.append(round(np.random.uniform(1.2, 1.8), 2))
    else:
        time_of_day.append("Off-Peak")
        surge_multiplier.append(round(np.random.uniform(1.0, 1.2), 2))

# -----------------------------
# DISTANCE & DURATION
# -----------------------------
distance_km = np.round(np.random.gamma(shape=2.5, scale=3, size=NUM_TRIPS), 2)

# Duration influenced by traffic
duration_minutes = []

for dist, tod in zip(distance_km, time_of_day):
    if tod == "Peak":
        speed = np.random.uniform(18, 28)  # slower traffic
    else:
        speed = np.random.uniform(28, 40)

    duration = (dist / speed) * 60
    duration += np.random.normal(3, 2)

    duration_minutes.append(round(max(duration, 5), 2))

# -----------------------------
# PRICING MODEL
# -----------------------------
BASE_FARE = 120
PRICE_PER_KM = 45
PRICE_PER_MIN = 4

fares = []

for dist, mins, surge in zip(distance_km, duration_minutes, surge_multiplier):
    fare = (
        BASE_FARE +
        (dist * PRICE_PER_KM) +
        (mins * PRICE_PER_MIN)
    ) * surge

    fare += np.random.normal(0, 40)

    fares.append(round(max(fare, 150), 2))

# -----------------------------
# COST MODEL
# -----------------------------
fuel_cost_per_km = np.round(np.random.uniform(12, 18, NUM_TRIPS), 2)

fuel_cost = np.round(distance_km * fuel_cost_per_km, 2)

driver_payout_percentage = np.round(
    np.random.uniform(0.72, 0.82, NUM_TRIPS),
    2
)

driver_payout = np.round(
    np.array(fares) * driver_payout_percentage,
    2
)

platform_cost = np.round(
    np.random.uniform(20, 60, NUM_TRIPS),
    2
)

total_cost = np.round(
    fuel_cost + driver_payout + platform_cost,
    2
)

# -----------------------------
# UNIT ECONOMICS
# -----------------------------
profit = np.round(np.array(fares) - total_cost, 2)

profit_margin_pct = np.round(
    (profit / np.array(fares)) * 100,
    2
)

profit_per_km = np.round(
    profit / distance_km,
    2
)

profit_per_minute = np.round(
    profit / duration_minutes,
    2
)

# -----------------------------
# CREATE DATAFRAME
# -----------------------------
df = pd.DataFrame({
    "trip_id": range(1, NUM_TRIPS + 1),
    "trip_datetime": dates,
    "time_of_day": time_of_day,
    "distance_km": distance_km,
    "duration_minutes": duration_minutes,
    "surge_multiplier": surge_multiplier,
    "fare_kes": fares,
    "fuel_cost_kes": fuel_cost,
    "driver_payout_kes": driver_payout,
    "platform_cost_kes": platform_cost,
    "total_cost_kes": total_cost,
    "profit_kes": profit,
    "profit_margin_pct": profit_margin_pct,
    "profit_per_km": profit_per_km,
    "profit_per_minute": profit_per_minute
})

# -----------------------------
# ADD DAY FEATURES
# -----------------------------
df["day_of_week"] = df["trip_datetime"].dt.day_name()
df["hour"] = df["trip_datetime"].dt.hour

# -----------------------------
# SAVE FILE
# -----------------------------
df.to_csv(OUTPUT_FILE, index=False)

# -----------------------------
# SUMMARY OUTPUT
# -----------------------------
print("\n===================================")
print("SIMULATED RIDE DATA CREATED")
print("===================================")

print(f"\nTotal Trips: {len(df):,}")
print(f"Average Fare: KES {df['fare_kes'].mean():.2f}")
print(f"Average Profit: KES {df['profit_kes'].mean():.2f}")

unprofitable = (df["profit_kes"] < 0).sum()

print(f"Unprofitable Trips: {unprofitable:,}")
print(f"Unprofitable %: {(unprofitable / len(df))*100:.2f}%")

print(f"\nCSV saved as: {OUTPUT_FILE}")
print("===================================\n")
