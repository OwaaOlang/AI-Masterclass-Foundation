

#Inspecting Data file

import pandas as pd
# Create a DataFrame from a dictionary and inspect it
data = {
    "name": ["Eric", "James", "Amina", "Sara"],
    "score": [85, 72, 91, 68],
    "city": ["Nairobi", "Mombasa", "Nairobi", "Kisumu"]
}

df = pd.DataFrame(data)

print("Size:", df.shape),
print("Header:", list(df.columns)),
print("Type:", df.dtypes),
print("First 3 rows:", df.head(3))

#Ex 2: 


import pandas as pd
data = {"name": ["Eric","James","Amina","Sara"], "score": [85,72,91,68], "city": ["Nairobi","Mombasa","Nairobi","Kisumu"]}
df = pd.DataFrame(data)
#Filter to shows students from Nairobi with scores 80
nairobi_scorce = df[(df["city"]=="Nairobi") & (df["score"]> 80)]
print(nairobi_scorce)

#Ex 3
import pandas as pd
data = {"name": ["Eric","James","Amina","Sara"],
         "score": [85,72,91,68], 
         "city": ["Nairobi","Mombasa","Nairobi","Kisumu"]}

df = pd.DataFrame(data)

#Groupby city and get average score per city
city_score= df.groupby("city")["score"].mean()
print("Average score per city:")
print(city_score)


#Ex 4
import numpy as np
# Create an array of 10 random integers between 1 and 100
# Print the mean, max, min, and standard deviation

print("np.linspace(1,100,1):")
print(np.linspace(1,100,10))

arr = np.array([1,12,23,34,45,56,67,78,89,100])

print(f"max: {arr.mean()}")
print(f"min: {arr.min()}")
print(f"mean: {arr.mean()}")
print(f"std dev: {arr.std()}")

#Ex 5
# Tiling contractor job records
jobs = [
    {"client": "Kamau", "location": "Kiambu", "boxes_used": 30, "price_per_box": 1800},
    {"client": "Mutua", "location": "Machakos", "boxes_used": 48, "price_per_box": 2100},
    {"client": "Odhiambo", "location": "Kisumu", "boxes_used": 20, "price_per_box": 1600},
    {"client": "Wanjiru", "location": "Nakuru", "boxes_used": 60, "price_per_box": 2200},
]
#Calculate total boxes laid, total revenue, and the average price per box across all jobs.

print("*** SUMMARY***:")
print("_" *50)
total_boxes = 0
total_revenue = 0

for j in jobs: 
    revenue = j["boxes_used"] * j["price_per_box"]
    print(f"{j['client']} {j['location']} : {j['boxes_used']} boxes |KES {revenue}")
    total_boxes  += j["boxes_used"] 
    total_revenue += revenue

avg_price = total_boxes / total_revenue

print(f" Total Boxes: {total_boxes}")
print(f"Total Revenue: {total_revenue}")
print(f"Average price: {avg_price}")


#6 Ex 
# Weekly milk yield per cow (litres)
herd_data = [
    {"cow": "Daisy", "yields": [72, 68, 74, 70]},
    {"cow": "Bella", "yields": [45, 42, 38, 40]},
    {"cow": "Nala",  "yields": [88, 91, 85, 93]},
    {"cow": "Rosa",  "yields": [55, 58, 52, 50]},
    {"cow": "Lola",  "yields": [78, 80, 76, 82]},
]


#Calculate each cow's total and average, identify the top producer, and flag any cow whose weekly average drops below 60 litres.

Minimun = 60
top_cow = None
top_total = 0

for cow in herd_data:
    total = sum(cow["yields"])
    avg = total / len(cow["yields"])
    status = "OK" if avg >= Minimun else "NEEDS ATTENTION"
    print(f"{cow['cow']} {total} {avg} {status}")

    if total> top_total:
        top_total = total
        top_cow = cow["cow"]

        print(f"Top producer: {top_total} {top_cow}")


print(f" Header: {df.shape}")

#EX
import pandas as pd

df = pd.DataFrame({
    "name":     ["James Omondi", "Sandra Weru", "Patrick Njiru", "Grace Achieng", "Brian Kamau", "Kevin Mwangi"],
    "city":     ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa"],
    "steps":    [9200, 10500, 8100, 11000, 7400, 10800],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD"],
})

print("Alternative Mombasa or Nairobi")
print("_" *50)

niro_momb = df[(df["city"] == "Nairobi") | (df["city"] == "mombasa")]
print(niro_momb)

print("Option 2")
print("_" * 30)

nrm_mom = df[df["city"].isin(["Nairobi", "mombasa"])]
print(nrm_mom[["name", "steps", "protocol"]])

# in Python  
def fetch_and_format(url):
with urllib.request.urlopen(url) as r:
      data = json.loads(r.load())
#format like a mini backend would
formatted = {
    "tool": "AI Summeriser",
    "status": "success",
    "origin": data.get("origin"),
    "url": data.get("url")

}

return json.dumps(formatted, indent = 2)  #convert to json string
#Test it 
result= fetch_and_format("https://httpbin.org/get")

