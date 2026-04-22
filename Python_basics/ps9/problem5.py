# 5. Repeat program 4 for a list of such words to be censored. 

words = ['donkey', 'a', 'animal', 'stubborn']


with open("para.txt", "r") as f:
    content = f.read()

for word in words:
  content = content.replace(word, "#"*len(word))

with open("para.txt", "w") as f:
    f.write(content)
    
with open("para.txt") as f:
    para = f.read()
    print(para)   