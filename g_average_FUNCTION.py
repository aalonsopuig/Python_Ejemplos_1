# This program calculates the average temperature from a list of temperatures.
# It demonstrates the use of functions, lists, and basic arithmetic operations in Python.

def average_temperature(temp):
    """
    Calculate the average of the given list of temperatures.
    
    Parameters:
    temperatures (list): A list of temperatures (float or int values).
    
    Returns:
    float: The average temperature.
    """
    # Calculate the sum of all temperatures and divide by the length of the list
    return sum(temp) / len(temp)

# List of temperatures 
temperatures = [22.0, 18.5, 25.3, 30.0, 16.2]

# Calculate the average temperature
avg_temp = average_temperature(temperatures)

# Print the average temperature
print ("Temperatures: ", temperatures)
print(f"The average temperature is: {avg_temp:.2f} degrees")
