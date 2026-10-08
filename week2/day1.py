week_steps = [9200, 7400, 10500, 8800, 6900, 11000, 9600]

for steps in week_steps:
    if steps>= 8000:
     print("Goal achieved", steps)
else:
    print("steps below", steps)


print("Days tracked:", len(week_steps))
