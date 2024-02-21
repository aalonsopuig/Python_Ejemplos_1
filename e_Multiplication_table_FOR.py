# Program to generate a multiplication table for numbers 1 through 10
# This example demonstrates the use of nested for loops to calculate and print
# the multiplication results in a structured format.

# Outer loop for each number in the table
for i in range(1, 11):
    # Inner loop for multiplying the current number by each number 1 through 10
    for j in range(1, 11):
        # Calculate the product
        product = i * j
        # Print the formatted multiplication fact
        print(f"{i} * {j} = {product}")
    # Print a new line after each row of the table to separate the numbers
    print("-" * 20)
