# with open('data.txt', 'w')as f:
#     f.write("This is appended txt")

# with open('data.txt', 'a')as f:
#     f.write("This is appended txt")

with open('data.txt', 'r')as f:
    data = f.read()
    print(data)