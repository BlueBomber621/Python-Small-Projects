import random

CHOSEN_NUMBER = random.randint(1, 100)
LIVES = 0

cont_game = True

def take_guess():
    global CHOSEN_NUMBER
    guess = int(input("Guess a number: "))
    if guess == CHOSEN_NUMBER:
        print(f"You guessed it! The number was {CHOSEN_NUMBER}!")
        return True
    else:
        if guess > CHOSEN_NUMBER:
            print("Too high!")
        else:
            print("Too low!")
        return False

while cont_game:
    CHOSEN_NUMBER = random.randint(1, 100)
    print("I'm thinking of a random number between 1 and 100!\nTry to guess it!")
    difficulty_chosen = input("Pick your difficulty from easy, medium, or hard: ").lower()
    if difficulty_chosen == "hard":
        LIVES = 5
    elif difficulty_chosen == "medium" or difficulty_chosen == "med":
        LIVES = 10
    else:
        LIVES = 15
    win_logic = False
    while LIVES > 0 and not win_logic:
        print(f"You have {LIVES} lives remaining.")
        win_logic = take_guess()
        if win_logic:
            continuation = input("\nWould you like to play again?\n(Y/N): ").lower()
            if continuation == "n":
                cont_game = False
        else:
            LIVES -= 1
    if LIVES <= 0:
        continuation = input("\nToo bad! Would you like to play again?\n(Y/N): ").lower()
        if continuation == "n":
            cont_game = False
    print("")