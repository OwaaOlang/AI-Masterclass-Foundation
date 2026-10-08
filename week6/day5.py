
import pandas as pd
import numpy as np

# 28 days of SMP fitness log
data = {
    "day":      list(range(1, 29)),
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200,
                 8900, 10800, 9100, 11200, 7900, 10000, 9700,
                 9500, 10300, 8600, 11500, 8200, 9800, 10600,
                 9000, 10100, 8400, 10900, 7500, 9600, 10400],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0,
                 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5,
                 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5,
                 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0],
    "water":    [7, 8, 6, 9, 8, 7, 8, 6, 9, 8, 8, 7, 9, 8,
                 7, 8, 6, 9, 8, 7, 9, 8, 8, 6, 9, 7, 8, 9],
    "protocol": (["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"] * 4),
    "cold_shower": ([True, True, False, True, True, True, True,
                     False, True, True, True, True, False, True] * 2),
    "bench_kg": [80, 82, 78, 85, 80, 83, 84,
                 81, 85, 80, 86, 79, 84, 83,
                 82, 86, 79, 88, 81, 85, 87,
                 82, 86, 80, 87, 79, 84, 86],
}

df = pd.DataFrame(data)

print("\nsize:", df.shape)
print("\nHeader:", list(df.columns))
print("\ndata type:", df.dtypes)
print("\n First 3 rows:", df.head(3))

#checking missing values
print(f"\nMissing values: {df.isna().sum().sum()}")
print(df.head(3).to_string())

#2. Examples 2

import pandas as pd
import numpy as np

data = {
    "day":      list(range(1, 29)),
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200, 8900, 10800, 9100, 11200, 7900, 10000, 9700, 9500, 10300, 8600, 11500, 8200, 9800, 10600, 9000, 10100, 8400, 10900, 7500, 9600, 10400],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0, 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5, 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5, 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0],
    "water":    [7, 8, 6, 9, 8, 7, 8, 6, 9, 8, 8, 7, 9, 8, 7, 8, 6, 9, 8, 7, 9, 8, 8, 6, 9, 7, 8, 9],
    "protocol": (["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"] * 4),
    "bench_kg": [80, 82, 78, 85, 80, 83, 84, 81, 85, 80, 86, 79, 84, 83, 82, 86, 79, 88, 81, 85, 87, 82, 86, 80, 87, 79, 84, 86],
}

pf = pd.DataFrame(data)

#High level performace: 10k steps and 7.5+ hours sleep
high_perf = df[(df["steps"]>=10000) & (df["sleep_hr"]>= 7.5)]
print(f"\nHigh performance Days: {len(high_perf)}/28")

#Protocol comparisions
print("\nMetrics by fasting protocols:")
protocol_stats = df.groupby("protocol").agg(
    avg_steps = ("steps", "mean"),
    avg_bench = ("bench_kg", "mean"),
    avg_sleep = ("sleep_hr", "mean"),
    avg_water = ("water","mean"),
    day= ("day", "count")
).round(1)
print(protocol_stats)

#example 3

import pandas as pd
import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200, 8900, 10800, 9100, 11200, 7900, 10000, 9700, 9500, 10300, 8600, 11500, 8200, 9800, 10600, 9000, 10100, 8400, 10900, 7500, 9600, 10400])
bench = np.array([80, 82, 78, 85, 80, 83, 84, 81, 85, 80, 86, 79, 84, 83, 82, 86, 79, 88, 81, 85, 87, 82, 86, 80, 87, 79, 84, 86])
sleep = np.array([7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0, 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5, 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5, 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0])

print("===28 days Numpy Analysis===")
print("\nsteps:")
print(f" mean:             {np.mean(steps)}")
print(f"std dev:           {np.std(steps)}")
print(f"25th percentile:   {np.percentile(steps,25)}")
print(f"75th percentile:   {np.percentile(steps,75)}")
print(f" Days 10k:         {np.sum(steps >= 10000)}/28")