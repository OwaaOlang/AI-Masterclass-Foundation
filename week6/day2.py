
import pandas as pd

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})

#Days where step goals was reached 
hit_goals = df[df["steps"] >= 10000]
print("Days where steps goals >10000:")
print(hit_goals[["day", "steps", "sleep_hr", "protocol"]])

#2.days with less than 7.5 hours sleep

low_sleep = df[df["sleep_hr"] < 7.5]
print("Low sleep Days:")
print(low_sleep[["day", "sleep_hr", "protocol"]])


#3. OMAD days with 10k steps
omad_goal = df[(df["protocol"] == "OMAD") & (df["steps"] >= 10000)]
print("OMAD days with 10k steps:")
print(omad_goal[["day", "protocol", "sleep_hr"]])

#4. Days with eith goal steps or sleep hours 8 or more 
either = df[(df["steps"]>= 10000) | (df["sleep_hr"])]
print("Goal steps or sleep hours 8 hours or more:")
print(either[["day", "steps", "sleep_hr"]])


#5. example 4
import pandas as pd

df = pd.DataFrame({
    "name":     ["James Omondi", "Sandra Weru", "Patrick Njiru", "Grace Achieng", "Brian Kamau", "Kevin Mwangi"],
    "city":     ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa"],
    "steps":    [9200, 10500, 8100, 11000, 7400, 10800],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD"],
})

#members from Nairobi or Mombasa
nir_mom = df[df["city"].isin(["Nairobi", "Mombasa"])]
print("members of Nairobi and Mombasa:")
print(nir_mom[["name", "city", "steps", "protocol"]])

print("Alternative Mombasa or Nairobi")
print("_" *50)

niro_momb = df[df["city"] == "Nairobi" | df["city"]=="mombasa" ]
print(niro_momb)



# example 5
import pandas as pd

df = pd.DataFrame({
    "day":          ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":        [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr":     [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "water_glasses":[7, 8, 6, 9, 8, 7, 8],
    "protocol":     ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})

#Add did we hit steps goal
df["hit_goal"] = df["steps"] >= 10000

#steps deficient or surplus vs 10000 goals
df["steps_vs_goals"]= df["steps"] - 10000

#water rating
df["hydration"] = df["water_glasses"].apply (lambda x: "Good" if x>8 else "Low")
print(df[["day", "steps", "hit_goal", "steps_vs_goals","hydration"]])

#6 renaming and dropping columns

df = df.rename(columns= {"sleep_hr" : "sleep_hours"})
print("After rename:")
print(list(df.columns))

#7. dropping columns
df= df.drop(columns= ["sleep_hours"])
print("After dropping:")
print(df)