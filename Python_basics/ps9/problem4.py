#  4. A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

# 1. open file para.txt
# 2. find word donkey
# 3. if there :
#       update word with "#####"
# 4. read that File

with open("para.txt", "r") as f:
    content = f.read()

content = content.replace('donkey', "#####")

with open("para.txt", "w") as f:
    f.write(content)
    
with open("para.txt") as f:
    para = f.read()
    print(para)    