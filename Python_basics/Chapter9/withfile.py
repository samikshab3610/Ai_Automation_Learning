f = open("file.txt")
print(f.read())
f.close()


# the same thing can be written as using with statement like this:

with open("file.txt") as f:
    print(f.read())

# dont have to explicitly close the file 