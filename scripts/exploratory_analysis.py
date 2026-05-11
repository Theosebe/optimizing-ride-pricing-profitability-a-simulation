import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("simulated_rides.csv")

# -----------------------------
# BASIC OVERVIEW
# -----------------------------
print("\n==============================")
print("DATASET OVERVIEW")
print("==============================\n")

print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

# -----------------------------
# CHECK MISSING VALUES
# -----------------------------
print("\n==============================")
print("MISSING VALUES")
print("==============================\n")

print(df.isnull().sum())

# -----------------------------
# SUMMARY STATISTICS
# -----------------------------
print("\n==============================")
print("SUMMARY STATISTICS")
print("==============================\n")

print(df.describe())

# -----------------------------
# PROFITABILITY OVERVIEW
# -----------------------------
print("\n==============================")
print("PROFITABILITY ANALYSIS")
print("==============================\n")

avg_profit = df["profit_kes"].mean()
total_profit = df["profit_kes"].sum()

print(f"Average Profit per Trip: KES {avg_profit:.2f}")
print(f"Total Profit: KES {total_profit:.2f}")

# -----------------------------
# UNPROFITABLE TRIPS
# -----------------------------
unprofitable = df[df["profit_kes"] < 0]

print(f"\nUnprofitable Trips: {len(unprofitable)}")

unprofitable_pct = (
    len(unprofitable) / len(df)
) * 100

print(f"Unprofitable %: {unprofitable_pct:.2f}%")

# -----------------------------
# PEAK VS OFF-PEAK ANALYSIS
# -----------------------------
print("\n==============================")
print("PEAK VS OFF-PEAK")
print("==============================\n")

peak_analysis = df.groupby("time_of_day")[[
    "fare_kes",
    "profit_kes",
    "profit_margin_pct"
]].mean()

print(peak_analysis)

# -----------------------------
# DAY OF WEEK ANALYSIS
# -----------------------------
print("\n==============================")
print("DAY OF WEEK ANALYSIS")
print("==============================\n")

day_analysis = df.groupby("day_of_week")[[
    "fare_kes",
    "profit_kes"
]].mean()

print(day_analysis)

# -----------------------------
# MOST PROFITABLE TRIPS
# -----------------------------
print("\n==============================")
print("TOP 10 MOST PROFITABLE TRIPS")
print("==============================\n")

top_trips = df.sort_values(
    by="profit_kes",
    ascending=False
)

print(top_trips[[
    "trip_id",
    "distance_km",
    "fare_kes",
    "profit_kes"
]].head(10))

# -----------------------------
# LOWEST PROFIT TRIPS
# -----------------------------
print("\n==============================")
print("TOP 10 LOWEST PROFIT TRIPS")
print("==============================\n")

worst_trips = df.sort_values(
    by="profit_kes",
    ascending=True
)

print(worst_trips[[
    "trip_id",
    "distance_km",
    "fare_kes",
    "profit_kes"
]].head(10))

print("\n==============================")
print("EDA COMPLETE")
print("==============================\n")
