
steps_data = ["9200", "7500", "ten thousand", "8800", "6900"]

for item in steps_data:
    try:
        steps = int(item)
        if steps >=8000:
            print( steps, "well done on steps")
        else:
            print(steps, "below level")
    except ValueError:
     print(f" {item}, is not a vlaid number")