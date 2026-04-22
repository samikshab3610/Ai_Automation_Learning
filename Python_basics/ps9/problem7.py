# 7. Write a program to find out the line number where python is present from ques 6. 

with open("logfile.txt") as f:
    lines = f.readlines()
   
lineno = 1

for line in lines:
    if ("Python" in line):
      print(f"word found. Line no: {lineno}")   
      break
    lineno += 1 

else:
       print("word not found")    



 