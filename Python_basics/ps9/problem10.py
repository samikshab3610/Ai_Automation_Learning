# 10. Write a program to wipe out the content of a file using python.

# f =  open ("this_copy.txt", "w") 
# f.close()

with open ("this_copy.txt", "w") as f:
    f.write("") 

