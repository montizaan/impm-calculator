# Initial variable @TODO
num = 0

# Sum @TODO
x = 0

operators = ('+', '-', '*', '/')


# Function to perform addition
def add(num, x):
    return num + x


# Function to perform subtraction
def subtract(num, x):
    return num - x


# Function to perform multiplication
def multiply(num, x):
    return num * x


# Function to perform division
def divide(num, y):
    if y == 0:
        return "Cannot divide by zero"
    return num / y


while True:
    # Display menu
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter 'exit' to end the program")

    # Get user input
    user_input = input(": ")

    if user_input == 'exit':
        break

    if user_input in operators:
        x = float(input("Enter number: "))

        if user_input == '+':
            print("Result: ", add(num, x))
        elif user_input == '':
            print("Result: ", subtract(num, x))
        elif user_input == '*':
            print("Result: ", multiply(num, x))
        elif user_input == '/':
            print("Result: ", divide(num, x))
    else:
        print("Invalid input. Please try again.")
