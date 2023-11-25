
#doing a rock, paper, scissors game

import random

#make the computer generate random number
randomValue = random.randint(0,2)

if randomValue == 0:
    computerInput = "rock"
elif randomValue == 1:
    computerInput = "paper"
elif randomValue == 2:
    computerInput = "scissors"
    
firstGame = input("Choose rock, paper, or scissors: ")

if firstGame == computerInput:
    print(f'Computer is {computerInput}. You are {firstGame}.')
    print("Draw.")
elif firstGame == "rock":
    if computerInput == "paper":
        print(f'Computer is {computerInput}. You are {firstGame}.')
        print("Computer wins.")
    if computerInput == "scissors":
        print(f'Computer is {computerInput}. You are {firstGame}.')
        print("You win.")
elif firstGame == "paper":
    if computerInput == "rock":
        print(f'Computer is {computerInput}. You are {firstGame}.')
        print("You win.")
    if computerInput == "scissors":
        print(f'Computer is {computerInput}. You are {firstGame}.')
        print("Computer wins.")
elif firstGame == "scissors":
    if computerInput == "rock":
        print(f'Computer is {computerInput}. You are {firstGame}.')
        print("Computer wins.")
    if computerInput == "paper":
        print(f'Computer is {computerInput}. You are {firstGame}.')
        print("You win.")
            
              
    
