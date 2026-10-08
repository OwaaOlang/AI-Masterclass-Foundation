
open("daily_log_txt", "w")
#writing to a file
#in a VS code, this creates a file on your computer:
with open("daily_log.txt", "w") as f:
    f.write("steps: 7200\n")
    f.write("protocols: OMAD\n")
    f.write("water: 8 glasses\n")
    f.write("cold shower: yes\n")


    #simulate writing a file
    import io

    file_content = io.StringIO()
    file_content.write("steps: 9200\n")
    file_content.write("water: 8 glasses\n")
    file_content.write("protocol: OMAD\n")
    file_content.write("cold shower: True\n")

    print("File written. contents:")
    print(file_content.getvalue())



    #Reading a file
    #in VS code, this reads a file from your computer:
    with open("file_content.txt", "r") as f:
        content = f.read()
        print(content)


#simulate reading a file

import io

#simulate file data

file_data = """Steps: 9200
    water: 8 glasses
    cold shower: yes
    protocol: OMAD
    sleep hours = 7.5
    """

#simulate reading the whole file
f = io.StringIO(file_data)
content = f.read()
print("Full file content:")
print(content)



#stimulate append

import io 
# In VS Code:
with open("daily_log.txt", "a") as f:
    f.write("Pages read: 30\n")
    f.write("Workout: bench press\n")


# Start with existing content
file_data = "Steps: 9200\nWater: 8 glasses\nProtocol: OMAD\n"

# Simulate append
file_data += "Pages read: 30\n"
file_data += "Workout: bench press 5x5 at 80kg\n"

print("File after appending:")
print(file_data)