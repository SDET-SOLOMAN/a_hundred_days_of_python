from arts.day_10_art import logo

print(logo)

a = 5
b = 10


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


operations = {
    '+': add,
    '-': substract,
    "/": divide,
    '*': multiply
}


def calculator():

    solve = True

    if solve:
        num1 = int(input("What's the number?: "))

    while solve:

        for symbol in operations:
            print(symbol)

        # Here we select operation/sign
        operation_symbol = input("Pick an operation: ")

        num2 = int(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        print("Do you want to continue, y or n")

        user_answer = input('').lower()

        if user_answer == 'y':
            num1 = answer
        else:
            print('Thanks for using OUR SDET CALCULATOR')
            calculator()


calculator()