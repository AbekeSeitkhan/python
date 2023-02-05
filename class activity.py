#1
class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()

#2
class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.1416*(self.radius**2)


circle = Circle(5)
print(circle.area())

#3
def grams_to_ounces(x):
	return 28.3495231 * x

grams = 10
ounces = grams_to_ounces(grams)
print ounces

# 4
def array(x):
    for i in range(len(x)-1):
        if x[i:i+2] == [3,3]:
            return True
    return False