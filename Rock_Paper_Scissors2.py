from random import randint
moves = ["rock", "paper", "scissors"]
while True:
    computer = moves[randint(0, 2)]
    player = input("rock, paper, or scissors? or end the game? ").lower()
    if player == "end the game":
        print("The game  has ended")
        break
    elif player == computer:
        print("Draw")
    elif player == "rock":
        if computer == "paper":
            print("Paper beats Rock , you lose")
        elif computer == "scissors":
            print("rock beats scissors, you win")
    elif player == "paper":
        if computer == "rock":
            print("Paper beats Rock , you win")
        elif computer == "scissors":
            print("scissors beats paper , you win")
    elif player == "scissors":
        if computer == "rock":
            print("rock beats scissors , you lose")
        elif computer == "paper":
            print("scissors beats paper, you win")


