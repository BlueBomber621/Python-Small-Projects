import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*?"
numbers = "01356789"
pass_list = []

print("Welcome to the Password Generator!")
length = int(input("How long do you want your password?\n"))
symbol_count = int(input("How many symbols do you want in it?\n"))
number_count = int(input("How many numbers do you want in it?\n"))

# Generation
for i in range(1, length + 1):
    pass_list.append("l")
if symbol_count + number_count > length:
    print("Cannot fit more symbols and numbers in the password than the password's length!\n")
else:
    for i in range(1, symbol_count + 1):
        target = random.randint(0, len(pass_list) - 1)
        if pass_list[target] == "l":
            pass_list[target] = "s"
        else:
            pass_list[pass_list.index("l")] = "s"
    for i in range(1, number_count + 1):
        target = random.randint(0, len(pass_list) - 1)
        if pass_list[target] == "l":
            pass_list[target] = "n"
        else:
            target = random.randint(0, len(pass_list) - 1)
            if pass_list[target] == "l":
                pass_list[target] = "n"
            else:
                pass_list[pass_list.index("l")] = "n"

final_pass = ""
for i in range(1, len(pass_list) + 1):
    if pass_list[i - 1] == "l":
        final_pass += letters[random.randint(0, len(letters) - 1)]
    elif pass_list[i - 1] == "s":
        final_pass += symbols[random.randint(0, len(symbols) - 1)]
    elif pass_list[i - 1] == "n":
        final_pass += numbers[random.randint(0, len(numbers) - 1)]

print(final_pass)