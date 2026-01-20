import random

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter your choice (1=Rock ,2=Paper, 3=Scissors): ")
playerChoice = int(playerChoice)

if playerChoice > 3 & playerChoice < 1:
    print("Error: Choice must be between 1 and 3")
else:
    computerChoice = random.randint(1, 3)

    playerChoiceIndex = choices[playerChoice - 1]
    computerChoiceIndex = choices[computerChoice - 1]

    print("You chose: ", playerChoice)
    print("Computer chose: ", computerChoice)

    # Determine the winner using if/elif/else
    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissors - You're winer!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rock - You're winer!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats Paper - You're winer!")
    else:
        print("lol")