#math
import math
deg = int(input("Input degree:"))

x = math.radians(deg)

print(f"Output radians:{x}")

#2
height = int(input("Height:"))

val1 = int(input("Base, first value:")) 

val2 = int(input("Base, second value:"))
x = (val1+val2)*0.5*height
print(f"Output:{x}")

#3
import math

n_of_sides = int(input("Input number of sides:"))
lenght = int(input("Input the length of a side:"))
deg = 180/n_of_sides
rad = math.radians(deg)

x = ((lenght**2)*n_of_sides)/(4*math.ceil(math.tan(rad))) 
print(f"The area of the polygon is: {x}")

#4
x = int(input("Length of base:"))
y = int(input("Height of parallelogram:"))

print(x * y)