import random

userWins = 0
compWins = 0
ties = 0
playing = "yes"
cF = 1

while playing == "yes" or playing == "Yes" or playing == "y":
    while cF == 1:
        player = str(input("Rock, Paper, or Scissors? "))
        if player == "rock" or player == "Rock":
            cF = 0
            player = "Rock"
        elif player == "paper" or player == "Paper":
            cF = 0
            player = "Paper"
        elif player == "scissors" or player == "Scissors":
            cF = 0
            player = "Scissors"
    #Converts player to first capital letter if possible and checks if correct format 
    cpu = random.randint(1,3)
    if cpu == 1:
        computer = "Rock"
    elif cpu == 2:
        computer = "Paper"
    elif cpu == 3:
        computer = "Scissors"
    #above lets the computer choose values and what roll it does
    #the line above is only there to separate the second line and the
    #line below this one.
    if player == "Rock":
        if computer == "Rock":
            print("You and the Machine chose Rock!")
            print("This match is a tie.")
            ties += 1
        elif computer == "Paper":
            print("You chose", player, "and The Machine chose", computer)
            print("You Lose. Get Gud.")
            compWins += 1
        elif computer == "Scissors":
            print("You chose", player, "and The Machine chose", computer)
            print("You Win!")
            userWins += 1
    elif player == "Paper":
        if computer == "Paper":
            print("You and the Machine chose Paper!")
            print("This match is a tie.")
            ties += 1
        elif computer == "Scissors":
            print("You chose", player, "and The Machine chose", computer)
            print("You Lose. Get Gud.")
            compWins += 1
        elif computer == "Rock":
            print("You chose", player, "and The Machine chose", computer)
            print("You Win!")
            userWins += 1
    elif player == "Scissors":
        if computer == "Scissors":
            print("You and the Machine chose Scissors!")
            print("This match is a tie.")
            ties += 1
        elif computer == "Rock":
            print("You chose", player, "and The Machine chose", computer)
            print("You Lose. Get Gud.")
            compWins += 1
        elif computer == "Paper":
            print("You chose", player, "and The Machine chose", computer)
            print("You Win!")
            userWins += 1
    cF = 1
    print("Your wins:", userWins)
    print("Computer wins:", compWins)
    print("Ties:", ties)
    playing = str(input("Continue Playing? (Yes or No)"))
    player = "pineapple"

print("Loop is over")
