
# Simulates what response.json() returns from a fitness API
data = {
    "user_id": 1,
    "name": "James Omondi",
    "date": "2024-11-18",
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5,
    "workout_completed": True
}

print(f"name:", data["name"])
print(f"steps:", data["steps"])
print(f"sleep:", data["sleep_hours"])
print(f"fasting:", data["fasting_protocol"])


#example 2
# Simulates: response.json() from /api/weekly-logs
weekly_logs = [
    {"day": "Monday",    "steps": 9200,  "protocol": "OMAD"},
    {"day": "Tuesday",   "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800,  "protocol": "OMAD"},
    {"day": "Thursday",  "steps": 11000, "protocol": "OMAD"},
    {"day": "Friday",    "steps": 7600,  "protocol": "2MAD"},
]

for log in weekly_logs:
    status = "Goal met" if log["steps"] >= 10000 else "short"
    print(f" {log["day"]} steps {status}")


    3. #Using .get() for Missing Keys
    records = [
    {"name": "Patrick Njiru", "steps": 9100, "water_glasses": 7},
    {"name": "Grace Achieng", "steps": 8400},           # no water logged
    {"name": "Brian Kamau",   "steps": 10200, "water_glasses": 9},
]
    for record in records:
        water = record.get("water_glasses", "not logged")
        print(f" {record['name']}: water = {water}")
        
