# This program demonstrates various ways to use the print function in Python.
# It shows how to print variables and text together using different formatting techniques,
# including simple concatenation, the format() method, f-strings, and the % operator.

name = "Alice"
age = 30

# Simple printing
print("Name:", name, "Age:", age)

# Using string concatenation
print("Name: " + name + " Age: " + str(age))

# Using string formatting with .format()
print("Name: {} Age: {}".format(name, age))

# Using f-string (formatted string literals) - Recommended for Python 3.6+
print(f"Name: {name} Age: {age}")

# Using % operator (similar to printf in C)
print("Name: %s Age: %d" % (name, age))
