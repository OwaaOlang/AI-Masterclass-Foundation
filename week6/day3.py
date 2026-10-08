
import pandas as pd

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})

#Average steps by fasting protocol
grouped = df.groupby("protocol")["steps"].mean().round(0)
print("Average steps by protocol:")
print(grouped)

#Total steps per protocol
totals= df.groupby("protocol")["steps"].sum()
print("Total steps by protocol:")
print(totals)

#example 2 #Aggregation functions
import pandas as pd

df = pd.DataFrame({
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian", "Kevin", "James", "Sandra"],
    "city":     ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa", "Nairobi", "Mombasa"],
    "steps":    [9200, 10500, 8100, 11000, 7400, 10800, 9800, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 7.0, 8.5],
})

#multiple aggregations on steps by city
city_stats = df.groupby("city")["steps"].agg(["max","min","mean","count"])
print("Multiple aggregate on steps by city:")
print(city_stats)


#5. Grouping multiple columns at once

import pandas as pd

df = pd.DataFrame({
    "city":     ["Nairobi", "Nairobi", "Mombasa", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Kisumu"],
    "protocol": ["OMAD",    "2MAD",    "OMAD",    "2MAD",    "OMAD",    "OMAD",   "2MAD",    "2MAD"],
    "steps":    [9200, 10500, 8100, 11000, 9400, 10200, 7400, 8800],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 7.5, 8.0, 9.0, 7.5],
})

#Average step groups by both city and protocol
breakdown = df.groupby(["city", "protocol"]) ["steps"].mean().round(0)
print("Average group steps by both city and protocol:")
print(breakdown)

#5.countvalues
import pandas as pd

df = pd.DataFrame({
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian", "Kevin", "James", "Grace", "Sandra", "James"],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD", "OMAD", "2MAD", "OMAD"],
    "city":     ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa", "Nairobi", "Kisumu", "Mombasa", "Nairobi"],
})

print("protocol distribution:")
print(df["protocol"].value_counts())

print("\nCity distribution:")
print(df["city"].value_counts())

#6 examples
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian"],
    "steps":    [9200, None, 8100, 11000, None],
    "sleep_hr": [7.5, 8.0, None, 7.0, 9.0],
})

print("original with NaN:")
print(df.to_string())

print("\nRows with any missing values:")
print(df[df.isna().any (axis = 1)].to_string())

#Fill any missing steps with the column mean
df["steps"] = df["steps"].fillna(df["steps"].mean())
df["sleep_hr"] = df["sleep_hr"].fillna(df["sleep_hr"].median())

print("\nAfter filling NaN:")
print(df.to_string)
