# 2. Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# ''' 



# name = input("Enter a name: ")
# date = input("Enter date as DD-MM-YYYY: ")

# letter = f"Dear {name}, \n You are selected! \n{date} " 
# print(letter)

letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 

print(letter.replace("<|Name|>","Harry").replace("<|Date|>","24-09-2025"))