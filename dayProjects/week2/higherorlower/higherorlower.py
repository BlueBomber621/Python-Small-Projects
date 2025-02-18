import random
from higherorlowerdata import GAME_DATASET

# The top 30 games in sales of 2016
GAME_DATA = []

cont_game = True
pass_game = True
score = 0

def get_game(current_game):
    """Get a new game based on the array of games, different from the current dictionary value"""
    global GAME_DATA
    select_game = random.randint(0, len(GAME_DATA) - 1)
    if GAME_DATA[select_game]["revenue"] == current_game["revenue"]:
        while GAME_DATA[select_game]["revenue"] == current_game["revenue"]:
            select_game = random.randint(0, len(GAME_DATA) - 1)
    return select_game

def versus_output(current_game, next_game):
    """Take in two dictionaries and their name, description, and revenue values, and return the player choice between the two dictionaries"""
    print(f"Does {next_game["name"]} have higher or lower revenue than {current_game["name"]} as of 2016?\n")
    print(f"{current_game["name"]}, {current_game["description"]} Revenue: ${current_game["revenue"]}\n")
    print("VS\n")
    print(f"{next_game["name"]}, {next_game["description"]}\n")
    pinput = input("(H)igher or (L)ower: ").lower()
    print("")
    return pinput


while cont_game:
    GAME_DATA = GAME_DATASET
    score = 0
    current_game = GAME_DATA[get_game({"name": "None", "revenue": -997})]
    next_game = GAME_DATA[get_game(current_game)]
    while pass_game:
        pinput = versus_output(current_game, next_game)
        if pinput == "h" or pinput == "higher":
            if current_game["revenue"] < next_game["revenue"]:
                print(f"\n*.*.* CORRECT *.*.*\n{current_game["name"]}: ${current_game["revenue"]}\n{next_game["name"]}: ${next_game["revenue"]}\n")
                score += 1
                if len(GAME_DATA) > 1:
                    GAME_DATA.remove(current_game)
                    current_game = next_game
                    next_game = GAME_DATA[get_game(current_game)]
                else:
                    print(f"You got the max score: {score}!")
            else:
                print(f"\nX-X-X INCORRECT X-X-X\n{current_game["name"]}: ${current_game["revenue"]}\n{next_game["name"]}: ${next_game["revenue"]}\n")
                pass_game = False
        elif pinput == "l" or pinput == "lower":
            if current_game["revenue"] > next_game["revenue"]:
                print(f"\n*.*.* CORRECT *.*.*\n{current_game["name"]}: ${current_game["revenue"]}\n{next_game["name"]}: ${next_game["revenue"]}\n")
                score += 1
                if len(GAME_DATA) > 1:
                    GAME_DATA.remove(current_game)
                    current_game = next_game
                    next_game = GAME_DATA[get_game(current_game)]
                else:
                    print(f"You got the max score: {score}!")
            else:
                print(f"\nX-X-X INCORRECT X-X-X\n{current_game["name"]}: ${current_game["revenue"]}\n{next_game["name"]}: ${next_game["revenue"]}\n")
                pass_game = False
        else:
            print("Provide a valid input.\n")
    
    pchoice = input(f"Game Over! Your score was {score}! Want to try again?\n(Y/N): ").lower()
    if pchoice == "n":
        cont_game = False
    else:
        print("")
        pass_game = True