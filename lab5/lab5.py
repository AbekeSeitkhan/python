#1 #Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
txt = input()


x = re.search('ab*', txt )

print(x)

#2 #Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
txt = input()

x = re.search("ab{2,3}", txt )

print(x)

#3 #Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

txt = input()

x = re.findall("[a-z]+_[a-z]+", txt )

print(x)

#4 #Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

txt = input()

x = re.findall("[A-Z]_[a-z]+", txt )

print(x)
#5 #Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re 

txt = input()

x = re.sub("[ ,.]", ":", txt)

print(x)

#6 #Write a python program to convert snake case string to camel case string.
import re

txt = input()

m = txt.split('_')
text = ''
for i in range(len(m)):
    x = m[i].capitalize()
    text += x

print(text)

#7 #Write a Python program to split a string at uppercase letters.
import re

txt = input()

x = re.findall('[A-Z][^A-Z]*', txt)

print(x)

#8 #Write a Python program to insert spaces between words starting with capital letters.
import re

txt = input()

x = re.findall('[A-Z][^A-Z]*', txt)
text = ' '.join(x)

print(text)

#9 #Write a Python program to convert a given camel case string to snake case.
import re

txt = input()

m = re.findall('[A-Z][^A-Z]*', txt)
for i in range(len(m)):
    m[i] = m[i].lower()

text = '_'.join(m)

print(text)