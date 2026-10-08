
# Write a program that saves your name and city to a text file
# then reads it back and prints it

import tempfile
path = tempfile.mktemp('suffix = .txt')
with open("path", "w") as f:
    f.write("Name: Owaa\n City: Lira\n")
with open("path", "r") as f:
    print(f.read())


    import json
# Create a Python dictionary and convert it to JSON
# Then parse it back and access a value
data = {"name": "owaa", "age": 30, "city": "lira"}

#use json.dumps() #python to json
json.txt = json.dumps(data)
print("Type:", type(json.txt))
print("JSON:", json.txt)

parsed = json.loads(json.txt)
print(f"Name: {parsed['name']}")
