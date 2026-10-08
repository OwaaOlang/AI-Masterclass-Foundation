response = {
    "status": "success",
    "user": {
        "id": 42,
        "name": "Kevin Mwangi",
        "location": {
            "city": "Kisumu",
            "country": "Kenya"
        }
    },
    "today": {
        "steps": 10800,
        "cold_shower": True,
        "fasting": {
            "protocol": "OMAD",
            "window_hours": 23
        },
        "workout": {
            "completed": True,
            "bench_press_kg": 90,
            "duration_minutes": 55
        }
    }
}


#Navigate layer by layer

name = response["user"]["name"]
city = response["user"]["location"]["city"]
steps = response["today"]["steps"]
protocol = response["today"]["fasting"]["protocol"]
bench = response["today"]["workout"]["bench_press_kg"]

print(f"Name: {name}")
print(f"City: {city}")
print(f"steps: {steps}")
print(f"Protocol: {protocol}")
print(f"Bench: {bench}")


#example 2 #when a value could be none 
users = [
    {"name": "James Omondi",  "workout": {"bench_press_kg": 80, "duration_minutes": 45}},
    {"name": "Sandra Weru",   "workout": None},   # did not train today
    {"name": "Grace Achieng", "workout": {"bench_press_kg": 60, "duration_minutes": 40}},
]

for user in users:
    name = user["name"]
    workout = user["workout"]
    if workout is None:
        print(f"{name}: rest day")
    else:
        bench = workout.get("bench_press_kg", "Not recorded")
        mins = workout.get("duration_minutes", "?")
        print(f" {name}: bench={bench} duration={mins}")

 #example 3 Extracting Fields from a List of Records
 # Raw API response: list of full user records
raw = [
    {"id": 1, "name": "James Omondi",  "email": "james@smp.ke", "steps": 9200,  "protocol": "OMAD", "sleep": 7.5, "active": True},
    {"id": 2, "name": "Sandra Weru",   "email": "sw@smp.ke",    "steps": 10500, "protocol": "2MAD", "sleep": 8.0, "active": True},
    {"id": 3, "name": "Patrick Njiru", "email": "pn@smp.ke",    "steps": 8100,  "protocol": "OMAD", "sleep": 6.5, "active": False},
    {"id": 4, "name": "Grace Achieng", "email": "ga@smp.ke",    "steps": 11000, "protocol": "OMAD", "sleep": 7.0, "active": True},
    {"id": 5, "name": "Brian Kamau",   "email": "bk@smp.ke",    "steps": 7400,  "protocol": "2MAD", "sleep": 9.0, "active": True},
]
#Extract active users with protocol, name and steps
#id, name, email, steps, protocol, sleep, active

clean = [
    { 
        "name": r["name"],
        "steps": r["steps"],
        "protocol": r["protocol"],
    }
    for r in raw if r["active"]
]

for record in clean:
    print(f"record{name} record{steps} record{protocol}")

    #example 4 Paginated Responses
    # What page 1 of a paginated API looks like
page_1 = {
    "page": 1,
    "total_pages": 3,
    "per_page": 3,
    "next_page": 2,
    "data": [
        {"name": "James Omondi",  "steps": 9200},
        {"name": "Sandra Weru",   "steps": 10500},
        {"name": "Patrick Njiru", "steps": 8100},
    ]
}

page_2 = {
    "page": 2,
    "total_pages": 3,
    "per_page": 3,
    "next_page": 3,
    "data": [
        {"name": "Grace Achieng", "steps": 11000},
        {"name": "Brian Kamau",   "steps": 7400},
        {"name": "Kevin Mwangi",  "steps": 10800},
    ]
}

#manual add them
all_records = page_1["data"] + page_2["data"]
print(f" Total records collected: {len(all_records)}")

for r in all_records:
 print(f" {r['name']} {r['steps']} steps")