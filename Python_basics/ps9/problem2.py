#2. The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score. 


# 1. import random
# 2. create a game function
# 3. create score from function
# 4. fetch the score from the File
#            if highscore file not empty
#               convert highscore into the integer
#             else hghscore is 0
# 5. print the score
#      if the scroe greater than the highscore
#            write the score in the file  
# 


import random

def game():
    score = random.randint(1, 90)
    #fetch the score from file
    with open("highscore.txt") as f:
        highscore = f.read()
        if (highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"Score: {score}")
    if (score > highscore):
        with open("highscore.txt", "w") as f:
            f.write(str(score))            


    return score

game()        

