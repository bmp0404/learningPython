# Rock Paper Scissors Game
import sys
import random
from enum import Enum

# Enum Class
class RPS(Enum):
    ROCK = 1 # all caps bc won't ever change
    PAPER = 2
    SCISSORS = 3

# Getting inputs from player
print("")
playerchoice = input("Enter...\n1 for Rock, \n2 for Paper, \n3 for Scissors\n\n")
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
print("")
print("You chose: " + str(RPS(player)).replace("RPS.", ""))
print("Python chose: " + str(RPS(computer)).replace("RPS.", ""))
print("")


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







