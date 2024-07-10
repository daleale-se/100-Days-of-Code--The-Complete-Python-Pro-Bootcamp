import os
from art import logo

clear = lambda: os.system('clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
    

def main():
    
    response = "n"
    result = 0
    first_number = 0
    
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    
    # i can use recursion function instead of while (True)
    while True:
        if response == "y":
            first_number = result
        elif response == "n":
            clear()
            print(logo)
            first_number = float(input("What's the first number?: "))
        
        for symbol in operations:
            print(symbol)
        
        type = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))

        operation = operations[type]
        result = operation(first_number, second_number)
                    
        print(f"{first_number} {type} {second_number} = {result}")
        
        response = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    
main()