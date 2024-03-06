# -*- coding: utf-8 -*-
# This program asks the user to input 5 integers and stores them in a list. It calculates the total sum of these numbers
# and then prints the sum. Additionally, it prints out numbers from the list that are greater than 10.

# Create an empty list to store the numbers
numbers = []

# Ask the user to enter 5 integers
for i in range(5):
    number = int(input("Enter a number:"))
    numbers.append(number)

# Calculate the total sum of the numbers
total_sum = sum(numbers)
print(f"The total sum of the numbers is: {total_sum}")

# Print numbers greater than 10
print("Numbers greater than 10:")
for number in numbers:
    if number > 10:
        print(number)

