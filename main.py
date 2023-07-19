from art import logo
import os


# Calculator

# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    flag = True
    while flag:
        for symbol in operations:
            print(symbol)
        symbol = input("Enter any one of the above operations: ")
        num2 = float(input("What's the second number?: "))
        function = operations[symbol]
        result = function(num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")
        cont = input(f"Enter '1' to continue operations with {result},\n"
                     f"enter '2' to start a fresh operation,\n"
                     f"or enter '3' to exit: ")
        alpha = True
        while alpha:
            if cont == '1':
                num1 = result
                alpha = False
            elif cont == '2':
                flag = False
                os.system('cls')
                calculator()
            elif cont == '3':
                return
            else:
                print("Invalid input! Try again")


calculator()
