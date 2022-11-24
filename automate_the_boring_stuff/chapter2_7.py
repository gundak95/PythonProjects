import random, sys

print("Welcome to a game of")
print("ROCK, PAPER, SCISSORS!")

#To track wins, losses and ties

wins=0
losses=0
ties=0

while True:
    print("% wins, % losses, % ties" %(wins, losses, ties))
    while True:
        #Let the player make a move
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        move=input()
        if move == "q":
            sys.exit()
        if move == "r" or move == "p" or move == "s":
            break
        print("Please enter either r, p, s, or q.")

        if move == "r":
            print ("ROCK versus...")
        elif move == "p":
            print ("PAPER versus...")
        elif move == "s":
            print ("SCISSORS versus...")
        
        #Let the computer make a move
        randomNumber=random.randint(1,3)
        if randomNumber == 1:
            computerMove == "r"
            print("ROCK!")
        elif randomNumber == 2:
            computerMove = "p"
            print("PAPER!")
        elif randomNumber == 3:
            computerMove = "s"
            print("SCISSORS!")
        
        #Calculate the outcome
        if move == computerMove:
            print("It's a tie!")
            ties=ties+1
        
        if move == "r" and computerMove == "p":
            print("You lose!")
            losses=losses+1

        if move == "r" and computerMove == "s":
            print("You win!")
            wins=wins+1

        if move == "p" and computerMove == "r":
            print("You win!")
            wins=wins+1

        if move == "p" and computerMove == "s":
            print("You lose!")
            losses=losses+1

        if move == "s" and computerMove == "r":
            print("You lose!")
            losses=losses+1

        if move == "s" and computerMove == "p":
            print("You win!")
            wins=wins+1