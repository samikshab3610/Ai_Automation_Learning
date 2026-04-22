#8. If languages of two friends are same; what will happen to the program in problem 6? 


dict = {}

name1 = input("Enter your Name: ")
language1 = input("Enter your language: ")
dict.update({name1 : language1})

name2 = input("Enter your Name: ")
language2 = input("Enter your language: ")
dict.update({name2 : language2})

name3 = input("Enter your Name: ")
language3 = input("Enter your language: ")
dict.update({name3 : language3})


print(dict.items())
