daily_steps = [8200, 5100, 11300, 6800, 9400, 4200, 10100]
target = 8000

day = 1
total_steps= 0
valid_days = 0
for steps in daily_steps:
    print("Day", day, ": ", steps, "steps", end="")
    if steps >= target:
     print("target hit.")
    else:
     print("goal missed.") 
    day = day + 1

    #skip days <5000 for average
    
    if steps < 5000:
     day = day + 1
     continue
    total_steps = total_steps + steps
    valid_days = valid_days + 1 
    average= total_steps / valid_days
    print("\nweekly average:", average)