import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
options = ["rock", "scissors", "paper"]

player_choice = options[int(input("Welcome to rock, paper, scissors! Choose 1 for rock, 2 for scissors, and 3 for paper!\n")) - 1]
com_choice = options[random.randint(0, 2)]

print("Your choice:")
if player_choice == "rock":
    print(rock)
elif player_choice == "paper":
    print(paper)
elif player_choice == "scissors":
    print(scissors)

print("Computer's choice:")
if com_choice == "rock":
    print(rock)
elif com_choice == "paper":
    print(paper)
elif com_choice == "scissors":
    print(scissors)

if player_choice == com_choice:
    print("It's a tie!")
elif (player_choice == "rock" and com_choice == "scissors") or \
        (player_choice == "scissors" and com_choice == "paper") or \
        (player_choice == "paper" and com_choice == "rock"):
    print("You win!")
else:
    print("You lose!")