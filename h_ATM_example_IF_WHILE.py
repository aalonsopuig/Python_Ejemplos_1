# Simple ATM Simulator
# This program simulates a simple ATM system in Python. Users start with a balance of $1000
# and can withdraw money in multiples of $100. The program checks if the withdrawal amount
# is valid (a multiple of $100 and does not exceed the current balance). If the user attempts
# to withdraw more than their balance or an invalid amount, an error message is displayed.
# The loop continues until the user exits by entering '0'. This demonstrates basic use of
# control flow with while, if, elif, and else statements in Python.

# Initial balance
balance = 1000

# Start of the program
print("Welcome to the ATM simulator. Your current balance is $1000")
print("Enter the amount to withdraw in multiples of $100, or '0' to exit.")

# Main loop
while True:
    # Ask the user for the amount to withdraw
    amount = int(input("Amount to withdraw: "))
    
    # Check for exit condition
    if amount == 0:
        print("Exiting. Thank you for using the ATM simulator.")
        break
    # Validate withdrawal amount
    elif amount % 100 == 0 and amount <= balance:
        balance -= amount  # Deduct the amount from balance
        print(f"${amount} withdrawn. New balance: ${balance}")
    else:
        # Handle errors: amount not in multiples of 100 or exceeds balance
        print("Invalid amount. Please enter a multiple of $100 not exceeding your balance.")
