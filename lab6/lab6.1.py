#Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce

mylist = list((1, 2, 3, 4))
multiplication =  reduce(lambda x, y: x*y, mylist)

#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_upper_lower(string):
    upper = 0
    lower = 0

    for i in string:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1

    return upper, lower

#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def ispalindrome(string):
    reversed_string = ''.join(reversed(string))
    return (string == reversed_string)

#Write a Python program that invoke square root function after specific milliseconds.
from time import sleep
import math
def function(num, delay):
    sleep(delay / 1000.0)
    return math.sqrt(num)

b = int(input())
t = int(input())
print("Square root of {} after {} miliseconds is {}".format(b, t, function(b, t)))

#Write a Python program with builtin function that returns True if all elements of the tuple are true.
mytup = (0, 1, 1)
g = all( mytup )