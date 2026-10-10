#calculate the area of a circle
#formula A=πr²

import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"the area of a circle is: {round(area, 2)}cm^2")