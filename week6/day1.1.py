
import pandas as pd

data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "water":    [7, 8, 6, 9, 8, 7, 8],
}
df = pd.DataFrame(data)

print("Statistics for all numerical contents:")
print(df.describe().to_string)


print(f" max steps: {df['steps'].max()}")
print(f"sum steps: {df['steps'].sum()}")
print(f"mean steps: {df['steps'].mean()}")
print(f" min steps: {df['steps'].min()}")