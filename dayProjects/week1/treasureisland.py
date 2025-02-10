print("Welcome to treasure island!\nYour goal is to find the treasure.\n")

choice1 = input("You are at the top of the hill, you spot a cabin, and a pathway down the hill. Type 'cabin' to go to the cabin, type 'hill' to head down the hill: ").lower()

if choice1 == 'cabin':
    choice2 = input("You find a chest, and you also find a comfy bed. Type 'chest' to open the chest, type 'bed' to sleep in the bed: ").lower()
    if choice2 == 'chest':
        print("The chest was a mimic, it sues you for trespassing in its home, you die of bankruptcy. Game Over :C")
    elif choice2 == 'bed':
        print("The bed was so comfy, you slept to death. Game Over :C")
    else:
        print("Invalid choice. Game Over :C")
elif choice1 == 'hill':
    choice2 = input("You find a crab, and a palm tree. Type 'crab' to go to the crab, type 'tree' to observe the tree: ").lower()
    if choice2 == 'crab':
        print("The crab attacks you with Hydro Pump, it's super effective! Game Over :C")
    elif choice2 == 'tree':
        choice3 = input("You trip over a lump in the sand going to the tree. Type 'hand' to dig with your bare hands, type 'rock' to hit the lump with a rock, type 'tree' to try to get a coconut from the tree to use: ").lower()
        if choice3 == 'hand':
            print("You died of hand cramps. Game Over :C")
        elif choice3 == 'rock':
            print("You hit some button hidden in the lump, opening up a safe. You won! You obtained 2 pennies!")
        elif choice3 == 'tree':
            print("You didn't know until now that you were deathly allergic to palm trees. Game Over :C")
        else:
            print("Invalid choice. Game Over :C")
    else:
        print("Invalid choice. Game Over :C")
else:
    print("Invalid choice. Game Over :C")