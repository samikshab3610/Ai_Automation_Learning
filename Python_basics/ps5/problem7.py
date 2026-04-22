#7. If the names of 2 friends are same; what will happen to the program in problem 6? 


dict = {}

language1 = input("Enter your language: ")
name1 = input("Enter your Name: ")
dict.update({language1 : name1})

language2 = input("Enter your language: ")
name2 = input("Enter your Name: ")
dict.update({language2 : name2})

language3 = input("Enter your language: ")
name3 = input("Enter your Name: ")
dict.update({language3 : name3})

language4 = input("Enter your language: ")
name4 = input("Enter your Name: ")
dict.update({language4 : name4})

print(dict.items())
