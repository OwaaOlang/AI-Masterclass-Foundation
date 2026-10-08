import json

daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5
}

#convert python to JSON json.dumps()
json_text = json.dumps(daily_log)
print("TYPE:", type(json))
print(json_text)


#indentations
pretty = json.dumps(daily_log, indent = 2)
print("\n PRETTY JSON:")
print(pretty)



#convert json to python
#json.loads()

import json

# This is what an API response might look like
api_response = '{"steps": 9200, "water_glasses": 8, "cold_shower": true, "protocol": "OMAD"}'
data = json.loads(api_response)

print("Type:", type(data))
print("Steps:", data["steps"])
print("water:", data["water_glasses"])
print("cold_shower:", data["cold_shower"])
print("protocol:", data["protocol"])

# working with JSON file
with open("log.json", "w") as f:
    json.dump(daily_log, f, indent = 2)

    #reading JSON in a file
    with open("log.json", "r") as f:
        data = json.load()

        import json

# A welding workshop stores job records as JSON
job_json = '''
{
  "workshop": "Kamau Metalworks",
  "location": "Gikomba, Nairobi",
  "jobs": [
    {"client": "Wanjiru",  "item": "gate",        "material": "mild steel", "quote_kes": 28000, "paid": true},
    {"client": "Otieno",   "item": "window grills","material": "angle iron", "quote_kes": 14500, "paid": false},
    {"client": "Mwangi",   "item": "door frame",   "material": "hollow tube","quote_kes": 9800,  "paid": true}
  ]
}
'''

data = json.loads(job_json)
print("workshop:", data["workshop"])
print("Location:", data["location"])
print()

total = 0
valid = 0
for job in data["jobs"]:
    status = "PAID" if job ["paid"] else "PENDING"
    print(f" {job['client']} : {job['item']} - KES{job['quote_kes']:,} [{status}]")
    total += job["quote_kes"]
    if job["paid"]:
        paid += job["quote_kes"]

        
print(f"\nTotal quoted: KES {total:,}")
print(f"Collected:    KES {paid:,}")
print(f"Outstanding:  KES {total - paid:,}")
