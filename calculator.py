# The welcome message displayed at the beginning of the program
welcome_message = ("Welcome to Melvin's calculator. \n"
                   "Options: \n"
                   "Enter '+ {number}' for addition. \n"
                   "Enter '- {number}' for subtraction. \n"
                   "Enter '* {number}' for multiplication. \n"
                   "Enter '/ {number}' for division. \n"
                   "Enter 'q' to show calculator's history \n"
                   "Enter 'exit' to end the program.")

# Mathematical operators
operators = ('+', '-', '*', '/')

# Results history
history = [0]


# Function of adding two numbers
def addition(number, operand):
    return number + operand


# Function of subtracting two numbers
def subtraction(number, operand):
    return number - operand


# Function of multiplication two numbers
def multiplication(number, operand):
    return number * operand


# Function of dividing two numbers
def division(number, operand):
    # The number cannot be plugged in, as dividing by zero is not possible, thus raising ValueError
    if operand == 0:
        raise ValueError("Division with 0 is not possible. Please try again with another number.")
    return number / operand


# The calculator function
def calculator():
    # Initial number
    number = 0

    # Result of the equation
    result = 0

    while True:
        # User inputs the operator with the operand
        user_input = input("Enter the operator followed by the operand, e.g. + 5: ")

        # The user can query their history with 'q
        if user_input == 'q':
            print(history)
            break

        # Exiting the program
        if user_input == 'exit':
            print("Bye!")
            break

        # Calculator sequence
        try:
            # Split the user input in an operator value (str) and operand value (number)
            operator, operand = user_input.split()

            # Convert the operand to a float variable for the equation
            operand = float(operand)

            # Check if the first character is an operator
            if operator in operators:
                if operator == '+':
                    result = addition(number, operand)
                    print(result)
                elif operator == '-':
                    result = subtraction(number, operand)
                    print(result)
                elif operator == '*':
                    result = multiplication(number, operand)
                    print(result)
                elif operator == '/':
                    result = division(number, operand)
                    print(result)
                else:
                    raise ValueError("The first character was no operator. Please use an operator.")

            # The user adds the result to the history list
            history.append(result)

            # The result of the previous equation becomes the initial value of the new equation
            number = result

        # The user cannot enter anything other than the operator and operand
        except ValueError:
            print("The input provided is not valid. Please check the instructions.")


# Instantiate a calculator instance
if __name__ == "__main__":
    print(welcome_message)
    calculator()
