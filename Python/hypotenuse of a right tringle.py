#calculate the hypotenuse of a right tringle
#formula c = sqrt of A² + B²

import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2)) 

print(f"side C = {c}")
