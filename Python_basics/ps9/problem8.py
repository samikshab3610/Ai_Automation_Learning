#  8. Write a program to make a copy of a text file “this. txt” 


with open("this.txt", "r") as f1:
    content = f1.read()

with open("this_copy.txt", "w") as f2:
    f2.write(content)    
    