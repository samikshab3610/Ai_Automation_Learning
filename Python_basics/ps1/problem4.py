# Q. Write a programm to print the contents of diractry using the os module. search online for function which does that . 

# Q. Write a python programm to print the contents of diractry using the os module. search online for function which does that .


import os

# specify the path (you can change this)
path = r"C:\Users\SAMIKSHA BHORE\Desktop\Automation\Python_basics\Chapter1"

# get list of files and directories
contents = os.listdir(path)

# print each item
for item in contents:
    print(item)