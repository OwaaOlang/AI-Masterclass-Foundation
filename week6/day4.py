import numpy as np

# From a Python list
steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])

print("steps arrays:",steps)
print("type:", type(steps))
print("dtypes:", steps.dtype)
print("shape:", steps.shape)

print("\nzeros(5):", np.zeros(5))
print("\nones(5):", np.ones(5))


#Ranges of numbers
print("Range of numbers(1,8):", np.arange(1,8))

#Evenly spaced
print("\nLinespace:", np.linspace(2,4,5))

#Vectorized operations
import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
goal = 10000

deficit = steps - goal
print("\nsteps Vs Goal:", deficit)

#Percentage of goals achieved
pct = (steps/ goal * 100).round(1)
print("\npercentage of goals achieved:", pct)

#Which days hit the goal #boolean
hit = steps >= goal
print("\nDays which hit the goal:", hit)
print("\ndays hitting goals:", steps[hit])

#statistical function

# 4 weeks of daily steps (28 days)

import numpy as np

steps_28 = np.array([
    9200, 10500, 8800, 11000, 7600, 9400, 10200,
    8900, 10800, 9100, 11200, 7900, 10000, 9700,
    9500, 10300, 8600, 11500, 8200, 9800, 10600,
    9000, 10100, 8400, 10900, 7500, 9600, 10400
])

print(f"28 days full analysis")
print(f" mean:          {np.mean(steps_28):,.0f}")
print(f" median:        {np.median(steps_28):,.0f}")
print(f" std dev:       {np.std(steps_28):,.0f}")


#Array slicing
import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("First 3 days:", steps[:3])
print("Last 2 days:", steps[-2:])
print("weekdays:", steps[:5])
print("Weekends:", steps[5:])

#Numpy and Panda together

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
})
#pull a column as numpy array
steps_arr = df["steps"].to_numpy()
print("\nNumpy array from pandas column:", steps_arr)
print("\nType:", type(steps_arr))

#Use Numpy on it
print(f"\nMean:           {np.mean(steps_arr):,.0f}")
print(f"\nstd dev:        {np.std(steps_arr):,.0f}")

#Normalize to 0 - 1 range (min - max scaling)
df["steps_norm"] = (df["steps"]- df["steps"].min()) / (df["steps"].max())- (df["steps"].min())
df["steps_norm"] = df["steps_norm"].round(3)
print("\nWith Normalized steps:")
print(df[["day", "steps", "steps_norm"]].to_string())

# Example, maize farm

import numpy as np

# Maize yield (90kg bags) per plot over a single season
yields = np.array([18, 22, 15, 31, 27, 19, 24, 12, 28, 21, 17, 25])
rainfall_mm = np.array([420, 510, 380, 620, 590, 440, 530, 310, 610, 490, 400, 560])

print("MAIZE YIELD ANALYSIS (90kg bags per plot)")
print(f" Plots: {len(yields)}")
print(f" Total yield: {np.sum(yields)} bags {np.sum(yields) * 90:,}kg)")
print(f" Mean: {np.mean(yields):.1f} bags/ plot")
print(f"Median: {np.median(yields):.1f} bags/ plot")
print(f" Standard Dev: {np.std(yields)}:.1f")
print(f" Best Plot: {np.max(yields)} bags")
print(f"Worst plot: {np.min(yields)} bags")
print(f"Total yield: {np.sum(yields) *90}kg")