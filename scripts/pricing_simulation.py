import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("simulated_rides.csv")

# -----------------------------
# ORIGINAL METRICS
# -----------------------------
original_avg_profit = df["profit_kes"].mean()

original_unprofitable = (
    df["profit_kes"] < 0
).sum()

original_unprofitable_pct = (
    original_unprofitable / len(df)
) * 100

print("\n==============================")
print("ORIGINAL PERFORMANCE")
print("==============================")

print(f"Average Profit: KES {original_avg_profit:.2f}")

print(
    f"Unprofitable Trips: "
    f"{original_unprofitable_pct:.2f}%"
)

# ====================================================
# SCENARIO 1:
# Increase fares for short trips (<3km) by 15%
# ====================================================

scenario1 = df.copy()

short_trip_condition = (
    scenario1["distance_km"] < 3
)

scenario1.loc[
    short_trip_condition,
    "fare_kes"
] *= 1.15

# Recalculate profits
scenario1["profit_kes"] = (
    scenario1["fare_kes"]
    - scenario1["total_cost_kes"]
)

# Scenario metrics
scenario1_avg_profit = (
    scenario1["profit_kes"].mean()
)

scenario1_unprofitable = (
    scenario1["profit_kes"] < 0
).sum()

scenario1_unprofitable_pct = (
    scenario1_unprofitable / len(df)
) * 100

print("\n==============================")
print("SCENARIO 1")
print("Increase Short Trip Fares by 15%")
print("==============================")

print(
    f"Average Profit: "
    f"KES {scenario1_avg_profit:.2f}"
)

print(
    f"Unprofitable Trips: "
    f"{scenario1_unprofitable_pct:.2f}%"
)

# ====================================================
# SCENARIO 2:
# Reduce driver payout by 5%
# ====================================================

scenario2 = df.copy()

scenario2["driver_payout_kes"] *= 0.95

scenario2["total_cost_kes"] = (
    scenario2["fuel_cost_kes"]
    + scenario2["driver_payout_kes"]
    + scenario2["platform_cost_kes"]
)

scenario2["profit_kes"] = (
    scenario2["fare_kes"]
    - scenario2["total_cost_kes"]
)

scenario2_avg_profit = (
    scenario2["profit_kes"].mean()
)

scenario2_unprofitable = (
    scenario2["profit_kes"] < 0
).sum()

scenario2_unprofitable_pct = (
    scenario2_unprofitable / len(df)
) * 100

print("\n==============================")
print("SCENARIO 2")
print("Reduce Driver Payout by 5%")
print("==============================")

print(
    f"Average Profit: "
    f"KES {scenario2_avg_profit:.2f}"
)

print(
    f"Unprofitable Trips: "
    f"{scenario2_unprofitable_pct:.2f}%"
)

# ====================================================
# SCENARIO 3:
# Increase peak-hour surge multipliers by 10%
# ====================================================

scenario3 = df.copy()

peak_condition = (
    scenario3["time_of_day"] == "Peak"
)

scenario3.loc[
    peak_condition,
    "fare_kes"
] *= 1.10

scenario3["profit_kes"] = (
    scenario3["fare_kes"]
    - scenario3["total_cost_kes"]
)

scenario3_avg_profit = (
    scenario3["profit_kes"].mean()
)

scenario3_unprofitable = (
    scenario3["profit_kes"] < 0
).sum()

scenario3_unprofitable_pct = (
    scenario3_unprofitable / len(df)
) * 100

print("\n==============================")
print("SCENARIO 3")
print("Increase Peak Pricing by 10%")
print("==============================")

print(
    f"Average Profit: "
    f"KES {scenario3_avg_profit:.2f}"
)

print(
    f"Unprofitable Trips: "
    f"{scenario3_unprofitable_pct:.2f}%"
)

# ====================================================
# BEST SCENARIO SUMMARY
# ====================================================

print("\n==============================")
print("SCENARIO COMPARISON")
print("==============================")

print(f"""
Original Avg Profit: {original_avg_profit:.2f}
Scenario 1 Avg Profit: {scenario1_avg_profit:.2f}
Scenario 2 Avg Profit: {scenario2_avg_profit:.2f}
Scenario 3 Avg Profit: {scenario3_avg_profit:.2f}
""")

print("\nSIMULATION COMPLETE")
