# This program is designed to demonstrate the application of functions in Python for temperature conversion.
# It allows the user to input a temperature and choose whether they want to convert it from Celsius to Fahrenheit
# or from Fahrenheit to Celsius. The program defines two functions, one for each conversion direction, and uses
# conditional logic to execute the appropriate conversion based on user input. It showcases fundamental programming
# concepts such as function definition, arithmetic operations, conditional statements, and user input handling.

def convert_to_celsius(fahrenheit):
    #Converts Fahrenheit to Celsius.
    return (fahrenheit - 32) * 5/9

def convert_to_fahrenheit(celsius):
    #Converts Celsius to Fahrenheit.
    return (celsius * 9/5) + 32

# Main program
temp = float(input("Enter the temperature: "))
unit = input("Convert to (F)ahrenheit or (C)elsius? ")

if unit.upper() == 'F':
    print(f"{temp}C is {convert_to_fahrenheit(temp)}F")
elif unit.upper() == 'C':
    print(f"{temp}F is {convert_to_celsius(temp)}C")
else:
    print("Invalid unit.")
