# Compount intrest calculator (including while loops)

principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principle amount: "))
    if principal < 0:
      print("Principle cant't be less than or equal to zero")
    else:
       break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
      print("Interest rate cant't be less than or equal to zero")
    else:
       break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
      print("Time cant't be less than or equal to zero")
    else:
       break

total = principal * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
