"""
This code functions as a basic calculator
"""


def calculator(number_1, number_2, operation):
    if operation == "+":
        return number_1 + number_2

    # Subtraction
    elif operation == "-":
        return number_1 - number_2

    # Division

    elif operation == "/":
        return number_1 / number_2

    # Multiplication

    elif operation == "*":
        return number_1 * number_2
    else:
        return "no operation"


# getting the user inuts

number_1 = float(input("enter the first number \n"))
number_2 = float(input("enter the second number \n"))

print("enter '+' to add two numbers")
print("enter '-' to subtract two numbers")
print("enter '/' to divide two numbers")
print("enter '*' to multiply two numbers")

operation = input("choose the operation \n")

print(calculator(number_1, number_2, operation))
