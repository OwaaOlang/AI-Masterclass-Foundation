

import csv
import io

csv_data = """name,steps,water,protocol,cold_shower
James Omondi,9200,8,OMAD,True
Sandra Weru,10500,9,2MAD,True
Patrick Njiru,7600,6,OMAD,False
Grace Achieng,11000,8,Autophagy Marathon,True"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

for row in reader:
    steps = int(row["steps"])
    status = "Goal reached" if steps >= 7000 else "Below goal"
    print(f" {row['name']}:{'steps'} steps | {row['protocol']} | {status}")




    import csv
    import io

csv_data = """day,steps,protocol
Monday,9200,OMAD
Tuesday,7500,2MAD
Wednesday,10500,OMAD
Thursday,4200,OMAD
Friday,8800,Autophagy Marathon
Saturday,11000,2MAD
Sunday,9600,OMAD"""


f = io.StringIO(csv_data)
reader = csv.DictReader(f)

valid_steps = []
for row in reader:
    steps = int(row["steps"])
    if steps >= 7000:
        valid_steps.append(steps)
        print(f" {row['day']} : {steps} steps")
    else:
        print(f"{row['day']} : {steps} steps - invalid")

        avg = sum(valid_steps) / len(valid_steps)
        print(f"\n average(valid days) : {round(avg)} steps")


        #skipping header next(reader)
        import csv
        import io

        f = io.StringIO(csv_data)
        reader = csv.reader(f)
        next(reader)  #skip header

        for row in reader:
            day, steps, protocol = row
            print(f"{day} | {protocol}")


            #writing with Dictwriter
            #writes dictuinary as csv row
             
             
             
import csv
import io

clients = [
    {"name": "James",   "skill": "welding",      "city": "Nairobi",  "sessions": 4},
    {"name": "Sandra",  "skill": "tiling",        "city": "Mombasa",  "sessions": 3},
    {"name": "Patrick", "skill": "phone repair",  "city": "Nairobi",  "sessions": 4},
    {"name": "Grace",   "skill": "copywriting",   "city": "Kisumu",   "sessions": 2},
]

output = io.StringIO()
fieldnames = ["name", "skill", "city", "sessions"]
writer = csv.DictWriter(output, fieldnames=fieldnames)

writer.writeheader()
writer.writerows(clients)

print(output.getvalue())

    

