# Sequential Interactive Calculator

# This program simulates a calculator that can perform basic arithmetic operations sequentially.
# The user enters a number, selects an arithmetic operation (+, -, /, x), and enters another number.
# The calculator performs the operation and waits for the next user input.
# This process repeats until the user enters '=' to display the result and end the program.

# Ask the user for the first number
print("Sequential Interactive Calculator")
result = float(input("Enter the first number: "))                       # Reads the first number and converts it to float

# Start a loop to request additional operations and numbers
while True:
    # Ask the user for the operation to be performed
    operation = input("Enter the operation (+, -, /, x, =): ")          # Reads the operation

    # Check if the user wants to end and show the result
    if operation == "=":
        print("The result is:", result)                                 # Displays the final result
        break                                                           # Ends the loop and exits the program

    # Ask the user for the next number
    number = float(input("Enter the next number: "))                    # Reads the next number and converts it to float

    # Use match to determine the operation to be performed
    if operation == "+":
        result += number                                                # Adds the number to the result
    elif operation == "-":
        result -= number                                                # Subtracts the number from the result
    elif operation == "/":
        if number != 0:                                                 # Prevents division by zero
            result /= number
        else:
            print("Error: Division by zero. Please try again.")         # Error message for division by zero
            continue                                                    # Allows the user to correct their input without ending the program
    elif operation == "x":
        result *= number                                                # Multiplies the result by the number
    else:  # Captures any input that is not a valid operation
        print("Invalid operation. Please try again.")                   # Error message for invalid operation

# Note: This program does not handle errors for non-numeric input. It is assumed that the user inputs valid numbers.
