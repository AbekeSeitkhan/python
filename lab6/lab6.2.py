#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

def listDirectories(path):
    print("Directories: ")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

def listFiles(path):
    print("Files: ")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

def listAll(path):
    print("All directories and files: ")
    for item in os.listdir(path):
        print(item)

path = 'pp2'
listDirectories(path)
listFiles(path)
listAll(path)

#2
#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os

path = 'tsis1'
if os.path.exists(path):
    print("exist")
    if os.access(path, os.R_OK):
        print("readable")
    if os.access(path, os.W_OK):
        print("writable")
    if os.access(path, os.X_OK):
        print("executable")

#3
#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

path = 'C:/Users/modik/Documents/pp2/Word.txt'
if os.path.exists(path):
    print( os.path.basename(path) )
    print( os.path.dirname(path) )
else:
    print( 'not exist' )

#4
#Write a Python program to count the number of lines in a text file.
import os

path = 'lab5/row.txt'
with open( path , 'r', encoding='UTF8') as f:
    lines = f.readlines()
    print( len(lines) )
    
#5
#Write a Python program to write a list to a file.
mylist = ['My', 'Name', "is", "Aziz"]

with open("text.txt", "w") as f:
    for i in range(len(mylist)):
        f.write(mylist[i] + ' ')
    
#6
#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string
for i in string.ascii_uppercase:
    file_name = i + '.txt'
    # print (file_name)
    with open(file_name, 'w') as f:
        pass

#7
#Write a Python program to copy the contents of a file to another file
with open('input.txt', 'r') as f:
    content = f.read()

with open('output.txt', 'w') as k:
    k.write( content )

#8
import os

path = ''
if os.path.exists(path):
    if os.path.access(path, os.R_OK):
        os.remove(path)
