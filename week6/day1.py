
import pandas as pd

data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "cold_shower": [True, True, False, True, True, True, True]
}

df = pd.DataFrame(data)
print(df.to_string())

#Inspecting DataFrame

print("Size:", df.shape)
print("\nHeader:", df.columns)
print(df.dtypes)
print(df.head(3).to_string())

#print columns
#printing steps column
print("steps column:")
print(df["steps"])

print(df[["steps", "protocol"]])

#print rows
print(df.iloc[0])

print(df.iloc[-1])

print(df.iloc[0:3])

print("\nprotocol and sleep_hr")
print(df[["sleep_hr","protocol"]])


print("\n First Row")
print(df.iloc[0])

print("\nRows 1 to 3")
print(df.iloc[0:4])