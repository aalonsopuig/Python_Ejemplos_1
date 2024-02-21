# -*- coding: utf-8 -*-
# Crear una lista vacía para almacenar los números
numeros = []

# Pedir al usuario que ingrese 5 números enteros
for i in range(5):
    numero = int(input("Ingresa número:"))
#    numero = int(2)
    numeros.append(numero)

# Calcular la suma de los números
suma_total = sum(numeros)
print(f"La suma total de los números es: {suma_total}")

# Imprimir números mayores que 10
print("Números mayores que 10:")
for numero in numeros:
    if numero > 10:
        print(numero)
