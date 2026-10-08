
week_log = [
    {"day": "Monday",    "steps": 9200,  "protocol": "OMAD"},
    {"day": "Tuesday",   "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800,  "protocol": "OMAD"},
    {"day": "Thursday",  "steps": 11000, "protocol": "Autophagy Marathon"},
    {"day": "Friday",    "steps": 7600,  "protocol": "OMAD"},
]

print(week_log)

print(week_log[0]["steps"])
print(week_log[3]["protocol"])


#if steps >=8000 print goal achieved or else below
for log in week_log:
 status = "Goal reached" if log["steps"] >= 8000 else "below goal"
 print(log["day"], "-", log["steps"], status)


 weekly_summary = {
    "week": 1,
    "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "protocols": ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD", "2MAD", "OMAD"],
    "cold_showers_completed": 6
}

print(weekly_summary)
print("Week:", weekly_summary["week"])
print("Total days tracked:", len(weekly_summary["steps"]))
print("First day steps:", weekly_summary["steps"][0])
print("average of weekly steps:", sum(weekly_summary["steps"]) / len(weekly_summary["steps"]))



