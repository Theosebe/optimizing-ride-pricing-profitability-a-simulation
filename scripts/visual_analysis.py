import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("simulated_rides.csv")

# -----------------------------
# 1. PROFIT DISTRIBUTION
# -----------------------------
plt.figure(figsize=(10,6))

plt.hist(df["profit_kes"], bins=50)

plt.title("Distribution of Trip Profit")
plt.xlabel("Profit (KES)")
plt.ylabel("Number of Trips")

plt.savefig("profit_distribution.png")

print("Saved: profit_distribution.png")

# -----------------------------
# 2. PEAK VS OFF-PEAK PROFIT
# -----------------------------
peak_profit = df.groupby("time_of_day")[
    "profit_kes"
].mean()

plt.figure(figsize=(6,5))

peak_profit.plot(kind="bar")

plt.title("Average Profit: Peak vs Off-Peak")
plt.ylabel("Average Profit (KES)")

plt.savefig("peak_vs_offpeak_profit.png")

print("Saved: peak_vs_offpeak_profit.png")

# -----------------------------
# 3. PROFIT BY DISTANCE
# -----------------------------
plt.figure(figsize=(10,6))

plt.scatter(
    df["distance_km"],
    df["profit_kes"],
    alpha=0.5
)

plt.title("Profit vs Distance")
plt.xlabel("Distance (KM)")
plt.ylabel("Profit (KES)")

plt.savefig("profit_vs_distance.png")

print("Saved: profit_vs_distance.png")

# -----------------------------
# 4. PROFIT MARGIN DISTRIBUTION
# -----------------------------
plt.figure(figsize=(10,6))

plt.hist(df["profit_margin_pct"], bins=50)

plt.title("Profit Margin Distribution")
plt.xlabel("Profit Margin %")
plt.ylabel("Number of Trips")

plt.savefig("profit_margin_distribution.png")

print("Saved: profit_margin_distribution.png")

print("\nVISUAL ANALYSIS COMPLETE")
