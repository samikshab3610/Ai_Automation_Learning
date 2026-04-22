# 9. Write a program to find out whether a file is identical & matches the content of another file. 

# with open("file1.txt") as f1, open("file2.txt") as f2:
#     if f1.read() == f2.read():
#         print("Files are identical")
#     else:
#         print("Files are not identical") 
# 


with open("file1.txt") as f1:
    content1 = f1.read()


with open("file2.txt") as f2:
    content2 = f2.read()


if (content1 == content2):
    print("Files are identical")
else:
    print("Files are not identical") 


