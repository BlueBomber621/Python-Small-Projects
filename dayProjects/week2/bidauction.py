print("Bid Auction")

bid_dict = {}

more_users = True

while more_users:
    my_name = input("What is your name?\n")
    my_bid = float(input("What is your bid?\n$"))
    bid_dict[my_name] = round(my_bid, 2)
    continuation = input("Are there any more users?\n(Y/N): ").lower()
    if continuation == "n":
        more_users = False
    
    if more_users:
        # Clear Console
        print("Continue\n\n\n")

max_bid = 0
winner = ""

for key in bid_dict:
    if bid_dict[key] > max_bid:
        winner = key
        max_bid = bid_dict[key]

if winner == "":
    print("\nThere's no winners smh.")
else:
    print(f"\n{winner} has won the auction with a bid of ${max_bid}!")