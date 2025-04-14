import random
player_wins = 0
computer_wins = 0
while player_wins < 2 and computer_wins < 2:
  print("Let's play rock, paper, or scissors")
  player_choice = input("Choose between rock, paper, or scissors : ").lower()
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)
  print(f"Computer chose: {computer_choice}")
  if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
    winner = "Player"
    player_wins += 1
  elif (player_choice == "rock" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "paper"):
    winner = "Tie"
  else :
    winner = "Computer"
    computer_wins += 1
  if (winner == "Player"):
    print("You won")
  elif (winner == "Computer"):
    print("Computer won")
  else:
    print("It's a tie")
  print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")
if player_wins > computer_wins:
  print("Congratulations! You won.")
else:
  print("Computer won !")
