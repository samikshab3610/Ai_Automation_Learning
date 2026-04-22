# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old. 


# 1. create a loop that runs for the table from 2 to 20
#     call function that creates the FileExistsError

# 2. create a function that creates tables
#     create table conatainer
#     loop that create the each table as
#         table = table + f"{n} x {i} = {n*i}\n"
#     write the table in the each file


def generateTable(n):
    table = ""
    for i in range (1,11):
        table += f"{n} X {i} = {n*i}"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)    

for i in range (2,21):
    generateTable(i)





















































# def generateTable(n):
#     table = ''
#     for i in range (1, 11):
#         table += f"{n} x {i} = {n*i}\n"

#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table)    


# for i in range (2, 21):
#     generateTable(i)

    