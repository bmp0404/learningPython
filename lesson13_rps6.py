# Rock Paper Scissors Game
import sys
import random
from enum import Enum

def rps():
    game_count = 0 
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins # pulling in parent function scope to modify these inside nested
        nonlocal python_wins

        # Enum Class
        class RPS(Enum):
            ROCK = 1 # all caps bc won't ever change
            PAPER = 2
            SCISSORS = 3

        # Getting inputs from player
        playerchoice = input("\nEnter...\n1 for Rock, \n2 for Paper, \n3 for Scissors\n\n")
        # player input string -> int

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()
        player = int(playerchoice)

        # Checking if valid input
        if player < 1 or player > 3:
            sys.exit("You must enter 1, 2, or 3.")

        # random choosing from string
        computerchoice = random.choice("123")
        # computer choice string -> int
        computer = int(computerchoice)

        # Output Messages
        print(f"\nYou chose: {str(RPS(player)).replace("RPS.", "")}.")
        print(f"Python chose: {str(RPS(computer)).replace("RPS.", "")}.\n")

        # Adding game logic
        # Only 1 if & else statement allowed each
        def decide_winner(player, computer): # nested function
            nonlocal player_wins # need to use nonlocal to pass down one more level
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You win!"
            elif player == computer:
                return "Tie game!"
            else:
                python_wins += 1
                return "🐍 Python wins"
    
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count 
        game_count += 1

        print(f"\nGame count: {str(game_count)}") 
        print(f"\nPlayer wins: {str(player_wins)}") 
        print(f"\nPython wins: {str(python_wins)}") 
        print("\nPlay again?")

        while True:
            playagain = input("\nPlay again? \nY for Yes\nN for No\n")
            if playagain.lower() not in ["y", "n"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("Thank you for playing")
            sys.exit("Bye!")
        
    return play_rps # don't need () bc not calling function, just returning



play = rps() # play holds play_rps function
play()






