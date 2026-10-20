# or Logical operator at least one condition must be true

temp = 15
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")