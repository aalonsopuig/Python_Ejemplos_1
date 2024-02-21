# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:19:34 2024

@author: 026_aalonpui
"""

animales=["Perro", "Gate"]
print("animales(1)", animales)
animales[1]="Gato"
print("animales(2)", animales)
animales.insert(1,"Loro")
print("animales(3)", animales)
animales.append("caballo")
print("animales(4)", animales)
animales.append("tomate")
print("animales(5)", animales)
animales.append("tomate")
print("animales(6)", animales)
animales.remove("tomate")
print("animales(7)", animales)
del animales[4]
print("animales(8)", animales)