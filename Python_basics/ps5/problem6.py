#6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 

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
