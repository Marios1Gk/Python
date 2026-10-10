# Python calculator

try:
    num1 = float(input("Enter the 1st number: "))
    operator = input("Enter an operator (+ - * /): ")
    num2 = float(input("Enter the 2nd number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        result = "invalid operator"
    print("Result:", round(result))

except ValueError:
    print("You must enter a number.")
