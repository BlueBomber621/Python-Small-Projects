stock = [
    {"name": "Pepsi", "count": 10, "price": 1.75},
    {"name": "Coca Cola", "count": 7, "price": 1.50},
    {"name": "Sprite", "count": 9, "price": 1.50},
    {"name": "Mtn Dew", "count": 6, "price": 2.00},
    {"name": "Dr Pepper", "count": 4, "price": 1.50},
    {"name": "Fanta", "count": 5, "price": 1.25},
]
coins = {"pennies": 0, "nickels": 2, "dimes": 2, "quarters": 2}

current_cash = 0.00

def print_report():
    global coins
    print("Soda stock:")
    for soda in stock:
        print(soda["name"] + " - count: " + str(soda["count"]))
    print("Coin stock:")
    for key in coins:
        print(key.capitalize() + ": " + str(coins[key]))

def eject_coins():
    global current_cash
    eject_coins = {"pennies": 0, "nickels": 0, "dimes": 0, "quarters": 0}
    while current_cash > 0:
        if current_cash >= 0.25 and coins["quarters"] > 0:
            current_cash -= 0.25
            coins["quarters"] -= 1
            eject_coins["quarters"] += 1
        elif current_cash >= 0.10 and coins["dimes"] > 0:
            current_cash -= 0.10
            coins["dimes"] -= 1
            eject_coins["dimes"] += 1
        elif current_cash >= 0.05 and coins["nickels"] > 0:
            current_cash -= 0.05
            coins["nickels"] -= 1
            eject_coins["nickels"] += 1
        elif current_cash >= 0.01 and coins["pennies"] > 0:
            current_cash -= 0.01
            coins["pennies"] -= 1
            eject_coins["pennies"] += 1
    return eject_coins

def manage_coins():
    global current_cash
    global coins
    running = True
    while running:
        choice = input("Managing coins: Input 'exit' to return to the main navigation, 'insert' to add coins, 'eject' to eject any remaining coins. $" + str(round(current_cash, 2)) + "\n").lower()
        if choice == "exit":
            running = False
        elif choice == "insert":
            coin_choice = "None"
            while coin_choice != "":
                coin_choice = input("Input nothing to return to managing coins, input 'p' for penny, 'n' for nickel, 'd' for dime, or 'q' for quarter. $" + str(round(current_cash, 2)) + "\n").lower()
                if coin_choice == 'p':
                    current_cash += 0.01
                    coins["pennies"] += 1
                elif coin_choice == 'n':
                    current_cash += 0.05
                    coins["nickels"] += 1
                elif coin_choice == 'd':
                    current_cash += 0.10
                    coins["dimes"] += 1
                elif coin_choice == 'q':
                    current_cash += 0.25
                    coins["quarters"] += 1
                elif coin_choice != "":
                    print("Invalid input")
        elif choice == "eject":
            if current_cash <= 0:
                print("No cash to eject")
            else:
                returned_coins = eject_coins()
                print(f"Ejected {returned_coins["pennies"]} pennies, {returned_coins["nickels"]} nickels, {returned_coins["dimes"]} dimes, {returned_coins["quarters"]} quarters.")
            
def select_item():
    global current_cash
    global stock
    running = True
    while running:
        print("Select a soda by entering their number, or enter 'exit' to return to the main navigation. $" + str(round(current_cash, 2)))
        index = []
        i = 0
        for item in stock:
            i += 1
            if item["count"] > 0:
                print(f"{i} - {item["name"]} - ${item["price"]}")
            index.append(item)
        choice = input("").lower()
        if choice == "exit":
            running = False
        elif int(choice) <= len(index):
            if current_cash >= stock[int(choice) - 1]["price"] and stock[int(choice) - 1]["count"] > 0:
                confirmation = input("You want to buy " + stock[int(choice) - 1]["name"] + ". Confirm?\n(Y/N): ").lower()
                if confirmation == "y":
                    current_cash -= stock[int(choice) - 1]["price"]
                    stock[int(choice) - 1]["count"] -= 1
                    print("Thank you for your purchase of " + stock[int(choice) - 1]["name"] + "! Have a nice day!")
            else:
                if stock[int(choice) - 1]["count"] <= 0:
                    print("Insufficient stock")
                elif current_cash < stock[int(choice) - 1]["price"]:
                    print("Insufficient cash")
                else:
                    print("Unregistered error")
        elif int(choice) > len(index):
            print("Invalid input")

    

machine_running = True

while machine_running:
    choice = input("Welcome to the soda machine: Input 'exit' to exit, 'report' for stock report, 'coins' to manage coins, and 'select' to make a selection. $" + str(round(current_cash, 2)) + "\n").lower()
    if choice == "exit":
        machine_running = False
    elif choice == "report":
        print_report()
    elif choice == "coins":
        manage_coins()
    elif choice == "select":
        select_item()