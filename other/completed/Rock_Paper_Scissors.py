################################################################
# Challenge 02 
# Game "Rock, Paper, Scissors"
# Uses: Basic Python - e.g. If, elif,input, print 
################################################################
import os
clearScreen = lambda: os.system('cls')



def computeGame(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! One of the player did not enter rock, paper or scissors, try again.")
        sys.exit()

clearScreen()
print("---------------------------------------------------------")
print("Game: Rock, Paper, Scissors!")
user1_answer = input("Player01, do yo want to choose rock, paper or scissors? ")
user2_answer = input("Player02, do you want to choose rock, paper or scissors? ")
result = computeGame(user1_answer, user2_answer)
print(result)
print("---------------------------------------------------------")