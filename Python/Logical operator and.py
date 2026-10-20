# and Logical operator both conditions must be true

temp = 30
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀️")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀️")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is WARM outside 😊")
    print("It is SUNNY ☀️")