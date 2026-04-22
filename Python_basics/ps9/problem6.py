# 6. Write a program to mine a log file and find out whether it contains ‘python’.


word = 'Python'

with open("logfile.txt") as f:
    data = f.read()
    print(data)

if word in data:
    print("word found")        
else:
    print("word not found")    
