import random

def getChoices():
    player_Choice = input("enter a choice (Rock,Paper,Scissors): \n")
    options = ["Rock","Paper","Scissors"]
    computer_Choice = random.choice(options)
    choices  = {"player":player_Choice ,"computer":computer_Choice}

    return choices

def checkWin(player, computer):
    print(f"Your choice is {player} , Computer's choice is {computer}. ") 
    if player == computer:
        return "It's a tie."
    elif player == "Rock": 
        if computer == "Scissors":
            return "Player WIN'S."
        else:
            return "Computer wins"
    elif player == "Scissors": 
        if computer == "Paper":
            return "Player WIN'S."
        else:
            return "Computer wins"
    elif player == "Paper": 
        if computer == "Rock":
            return "Player WIN'S."
        else:
            return "Computer wins"


choices = getChoices()
result = checkWin(choices["player"],choices["computer"])
print(f"\n The result is:  {result}")
