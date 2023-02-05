"""
 Python Functions 
 Python Lambda 
 Python Classes and Objects. 
 Python Inheritance 
 """
 # python functions 
 
def my_function():
print("Hello from a function")
# 

def my_function(fname, lname):
  print(fname)
#  printling 1st item in function
def my_function(x):
  return x + 5
  # changing the value of x
  #
  # function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ",sum)
# function call with two values
add_numbers(5, 4)
#
def find_square(num):
    result = num * num
    return result
square = find_square(3)
print('Square:',square)
#
def my_function(**kid):
  print("His last name is " + kid["lname"])
  # when keyboard arguments a lot and unknown
  # 
  x = lambda a : a * a
  # lambda function
  def getSum(*numbers):
    sum = 0
    for i in numbers:
    sum += i
    return sum
    # 
    class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)
# Inheritance
class Person:
  def __init__(self, fname):
    self.firstname = fname
 def printname(self):
    print(self.firstname)
class Student(Person):
  pass
x = Student("Mike")
x.printname()


