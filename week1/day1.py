#Pushed to Github successfully!

print("i have started.")
print("I am happy to start with Amerix")
steps = 9200
water_glasses = 8
fasting = True
name = "Amerix Student"
print(steps)
print(water_glasses)
print(fasting)
print(name)
print(name, "walked",steps, "steps and drank",water_glasses, "glasses of water")
steps = 7200
print("morning count:", steps)
steps = 9400 # update the variable
print("End of day:", steps)
steps = steps + 600 #add 600 to the current value
print("After evening walk:", steps)
steps_as_string = "9400"   # this is a str, not a number
steps_as_int = int(steps_as_string)   # now it is an int

print(type(steps_as_string))   # <class 'str'>
print(type(steps_as_int))      # <class 'int'>
target = 10000
gap = target - steps_as_int




weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
print("Last day:", weekly_steps[-1])
print("Second to last:", weekly_steps[-2])
print("First day:", weekly_steps[-7])

print("Days tracked:", len(weekly_steps))

skills = ["welding", "tiling", "upholstery", "phone repair", "copywriting"]

print("skills in list:", len(skills))

skills = ["welding", "tiling", "upholstery"]
print("Before.", skills)
skills.append("graaphic design")
print("final",skills)

#print "copywriting" at position 1
print("Before", skills)
skills.insert(1, "copywriting")
print("after", skills)
