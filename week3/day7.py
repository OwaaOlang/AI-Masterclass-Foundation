
#weekly assignments
#variable of name, age and city
name = "owaa_olang"
age = 33
city= "lira"

print(f" my name is:", {name})
print(f" i am:", {age})
print(f" i live in:", {city})
print(f"my name is {name}, from {city}, {age} old")

steps = 7200

if steps >= 8000:
    print("Step target hit.")

else:
    print(f" target missed. you need {8000 - steps} more steps")


    steps = 8000
    if steps>= 10000:
        print("Excellent. steps exceeded")
    elif steps >= 8000:
        print("steps achieved")
    elif steps >= 5000:
        print("steps half way achieved")
    else:
        print("today is sedentary")


steps = 9200
water_glasses = 8
cold_shower = True
sleep_hours = 7

if steps >= 8000 and water_glasses >= 6:
    print("both targets achieved")
else:
    print("steps or water glasses: below target")


workout_done = True
weight_lifted_kg = 5200
personal_best_kg = 5000

#nested if and if
if workout_done:
    print("workout logged")

    if weight_lifted_kg> personal_best_kg:
        print("personal best:", personal_best_kg)
        print("new record:", weight_lifted_kg)
    else:
      print("solid session. no new record")
else:
 print("rest day.")



 #loop
 steps_goal = 8000
 for day in range(10):
    print("Step goal: 8,000 steps")

    for day in range(5):
     print("Day:", day, "- Step goal: 8,000 steps")


daily_steps = [3200, 7100, 9800, 10500, 6400, 11200]
target = 10000

for steps in daily_steps:

    if steps >= target:
        print(f"checking: {steps} steps")
        print(f"Target hit on this day: {steps} steps. Stopping search.")
        break




daily_steps = [3200, 7100, 9800, 4100, 10500, 6400]
minimum = 7000

total = 0
valid_days = 0

for steps in daily_steps:
   if steps < minimum:
      continue
   total += steps
   valid_days += 1

print(f"valid days: {valid_days}")
print(f"total days: {total}")
print(f"average: {total // valid_days}")




 
