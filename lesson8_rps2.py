# Rock Paper Scissors Game
import sys
import random
from enum import Enum

# Enum Class
class RPS(Enum):
    ROCK = 1 # all caps bc won't ever change
    PAPER = 2
    SCISSORS = 3

playagain = True
while playagain:

    # Getting inputs from player

    playerchoice = input("\nEnter...\n1 for Rock, \n2 for Paper, \n3 for Scissors\n\n")
    # player input string -> int
    player = int(playerchoice)


    # Checking if valid input
    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")


    # random choosing from string
    computerchoice = random.choice("123")
    # computer choice string -> int
    computer = int(computerchoice)


    # Output Messages

    print("\nYou chose: " + str(RPS(player)).replace("RPS.", ""))
    print("Python chose: " + str(RPS(computer)).replace("RPS.", "")+ "\n")



    # Adding game logic
    # Only 1 if & else statement allowed each
    if player == 1 and computer == 3:
        print("😂 You win!")
    elif player == 2 and computer == 1:
        print("You win!")
    elif player == 3 and computer == 2:
        print("You win!")
    elif player == computer:
        print("Tie game!")
    else:
        print("🐍 Python wins")


    playagain = input("\nPlay again? \nY for Yes\nN for No\n\n")
    if playagain.lower() == "y":
        continue
    else:
        print("Thank you for playing")
        break
        # playagain = False


sys.exit("Bye!")






