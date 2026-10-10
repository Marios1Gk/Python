#calculate the circumference of a circle
#formula c=2πr

import math

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius 

print(f"The circumference is: {round(circumference, 2)}cm")
