import random

randnum = random.randint(0, 1)
flip = "none"

if randnum == 1:
    flip = "heads"
elif randnum == 0:
    flip = "tails"

print("Welcome to Heads or Tails!")
guess = input("Pick heads or tails!: ")

if guess.lower() == flip or guess[0].lower() == flip[0]:
    print(flip.capitalize() + "! You Win!")
else:
    print(flip.capitalize() + "! You Lose!")
