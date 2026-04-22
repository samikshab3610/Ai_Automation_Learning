# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’. 

word = "Twinkle"

with open("poem.txt") as f:
    data=f.read()

if (word in data):
    print("Word found")    
else:
    print("Not found")    
    

