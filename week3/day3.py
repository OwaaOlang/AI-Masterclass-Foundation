
people = [
    {"name": "James",   "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200]},
    {"name": "Sandra",  "steps": [7000, 7500, 6800, 8000, 7200, 8500, 7800]},
    {"name": "Mwangi",  "steps": [10000, 11500, 9800, 12000, 10500, 11000, 10800]},
    {"name": "Patrick", "steps": [8500, 9000, 8800, 9200, 8600, 9400, 9100]},
]

#list of all steps count of any person above 10000
all_steps = [s for p in people for s in p ["steps"]]
high_steps = [s for s in all_steps if s >=10000]
print("steps above 10000:", high_steps)