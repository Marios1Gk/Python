# while loops = execute some code WHILE some condition remains true

# EXAMPLE 1

#name = input("Enter your name: ")

#while name == "":
#    print("You did not enter your name")
#    name = input("Enter your name: ")

#print(f"Hello {name}")

# EXAMPLE 2

#age = int(input("Enter your age: "))

#while age < 0:
#    print("Age can't be negative")
#    age = int(input("Enter your age: "))

#print(f"You are {age} years old")

# EXAMPLE 3 (logical operators inderduced)

#food = input("Enter a food you like (q to quit): ")

#while not food == "q":
#    print(F"You like {food}")
#    food = input("Enter another food you like (q to quit): ")

#print("bye")

# EXAMPLE 4 (or logical operator)

num = int(input("Enter a number between 1 - 10: "))

while num <1 or num >10:
    print(f"{num} is not a valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")



