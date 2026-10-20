# if = Do some code If some conditions is True 
# Else do somthin else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign in")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up")