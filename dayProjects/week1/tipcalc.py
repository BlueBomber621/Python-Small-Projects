print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
perc = float(input("What percentage tip will you give? %"))
people = int(input("How many to split the total bill? "))

print(f"You should be paying ${round((bill * (1 + (perc / 100)) / people), 2)}")
