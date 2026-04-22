#1. Write a program to create a dictionary of marathi words with values as their English translation. Provide user with an option to look it up! 

dict = {
    "key"   : "value",
    "Batali" : "Bottle",
    "Undir" : "Mouse",
    "mulgi" : "girl",
    "patra" :"letter",
}

word = input("Enter a marathi word: ")
print("Meaning: ", dict[word])