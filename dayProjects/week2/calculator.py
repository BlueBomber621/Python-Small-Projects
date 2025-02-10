print("Welcome to the Calculator!\n")

def add_num(n1, n2):
    return n1 + n2

def sub_num(n1, n2):
    return n1 - n2

def mult_num(n1, n2):
    return n1 * n2

def div_num(n1, n2):
    return n1 / n2

current_num = "none"
cont_calc = True

def init_query():
    """The function to return the calculation with no initial number"""
    first_num = float(input("What is the first number?: "))
    method = input("What is the mathematical method being used? ( + - * / ): ")
    second_num = float(input("What is the second number?: "))
    if method == "+":
        new_num = add_num(first_num, second_num)
    elif method == "-":
        new_num = sub_num(first_num, second_num)
    elif method == "*":
        new_num = mult_num(first_num, second_num)
    elif method == "/":
        new_num = div_num(first_num, second_num)
    
    return new_num

def cont_query(old_num):
    """Function to return the previous number after an operation"""
    method = input("What is the mathematical method being used? ( + - * / ): ")
    second_num = float(input("What is the second number?: "))
    if method == "+":
        new_num = add_num(old_num, second_num)
    elif method == "-":
        new_num = sub_num(old_num, second_num)
    elif method == "*":
        new_num = mult_num(old_num, second_num)
    elif method == "/":
        new_num = div_num(old_num, second_num)

    return new_num
    


while cont_calc:
    if current_num == "none":
        current_num = init_query()
        continuation = input("Enter 'y' to continue with current number " + str(current_num) + ", enter 'c' to continue from scratch, enter 'n' to exit: ").lower()
        if continuation == "n":
            cont_calc = False
        elif continuation == "c":
            current_num = "none"
    else:
        current_num = cont_query(current_num)
        continuation = input("Enter 'y' to continue with current number " + str(current_num) + ", enter 'c' to continue from scratch, enter 'n' to exit: ").lower()
        if continuation == "n":
            cont_calc = False
        elif continuation == "c":
            current_num = "none"