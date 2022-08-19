import random

def get_choice():
    choices = ["rock", "paper", "scissor"]
    player_choice = input("Choose (Rock, Paper, Scissor): ")
    computer_choice = random.choice(choices)
    
    return {"player": player_choice, "computer": computer_choice}

def check_win(player, computer):
    if player == computer:
        return "Draw!"
    elif player == "rock":
        if computer == "paper":
            return f"{player} Lose {computer} Win"
        else:
            return f"{player} Win {computer} Lose"
    elif player == "paper":
        if computer == "scissor":
            return f"{player} Lose {computer} Win"
        else:
            return f"{player} Win {computer} Lose"
    elif player == "scissor":
        if computer == "rock":
            return f"{player} Lose {computer} Win"
        else:
            return f"{player} Win {computer} Lose"
            
choices = get_choice()
player_choice = choices["player"]
computer_choice = choices["computer"]

win_or_not = check_win(player_choice, computer_choice)

print(win_or_not)