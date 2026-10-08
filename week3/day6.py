
# Write a function called greet that takes a name
# and returns a greeting string

def greet(name):
    return (f"hello, {name}")

print(greet("Denis"))
print(greet("Owaa"))
print(greet("Andrew"))
print(greet("Olang"))
print(greet("Denis Junior"))


# Write a function called power(base, exp=2)
# that returns base raised to exp

def power(base, exp=2):
    return base ** exp

print(power(4))
print(power(10))


# Use a list comprehension to get all even numbers from 1 to 30

even= [n for n in range (1,31) if n % 2 == 0]
print(even)

# Now get the squares of those even numbers

squares = [n**2 for n in even]
print(squares)


# Write a function that takes a list of scores
# and returns the average, highest, and lowest

def analyse(scores):
    return {
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores)
    }

result = analyse([85, 72, 36, 64, 96])
for k, v in result.items():
    print(f"{k} : {v}")


