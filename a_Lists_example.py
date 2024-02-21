# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:19:34 2024

@author: 026_aalonpui
"""

# Initialize a list with two animal names
animales = ["Perro", "Gate"]  # 'Gate' is a typo
print("animales(1)", animales)

# Correct the typo from "Gate" to "Gato"
animales[1] = "Gato"
print("animales(2)", animales)

# Insert "Loro" at the second position
animales.insert(1, "Loro")
print("animales(3)", animales)

# Append "caballo" to the end of the list
animales.append("caballo")
print("animales(4)", animales)

# Append "tomate" to the list (intentionally adding a non-animal)
animales.append("tomate")
print("animales(5)", animales)

# Append another "tomate" to demonstrate handling duplicates
animales.append("tomate")
print("animales(6)", animales)

# Remove the first occurrence of "tomate"
animales.remove("tomate")
print("animales(7)", animales)

# Delete the fifth element of the list
del animales[4]
print("animales(8)", animales)
