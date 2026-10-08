steps = [8800, 6500, 11000, 9200, 7300]

print("Before:", steps)
#add 10500 at the end
#listname.methodname (
steps.append(10500)
print("after:", steps)

#remove 6500
print("Before:", steps)
steps.remove(6500)
print("After:", steps)

#sort from lowest to highest
print("Before:", steps)
steps.sort()
print("After:", steps)

#highest to lowest
print("Unsorted:", steps)
steps.sort(reverse= True)
print("sorted:", steps)

#days that exceeds 9000
high_days = 0
for s in steps:
    if s>= 9000:
        high_days += 1
        print("Days over 9000:", high_days)