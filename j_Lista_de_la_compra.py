"""
Programa de Lista de Compras Simplificado

Título: Lista de Compras Interactiva

Descripción:
Este programa permite al usuario crear y gestionar una lista de compras de manera interactiva.
El usuario puede añadir artículos a la lista de compras ingresando los nombres de los artículos uno por uno.
Para finalizar y ver todos los artículos añadidos a la lista, el usuario debe ingresar '0'.
El programa muestra entonces la lista completa de compras antes de terminar su ejecución.
Es una herramienta sencilla pero práctica para llevar un registro de compras pendientes.
"""

# Instrucción para el usuario
print("Bienvenido al programa de la lista de compras.")
print("Por favor, introduce los artículos que deseas añadir a tu lista.")
print("Cuando hayas terminado, escribe '0' para finalizar y mostrar la lista completa.\n")

# Inicialización de la lista de compras
lista_compras = []

# Bucle para añadir artículos a la lista
while True:
    # Solicita al usuario el artículo a añadir
    articulo = input("Introduce el nombre del artículo a agregar o '0' para finalizar: ")
    # Verifica si el usuario desea terminar
    if articulo == '0':
        break  # Sale del bucle
    # Añade el artículo a la lista de compras
    lista_compras.append(articulo)

# Verifica si la lista está vacía antes de mostrarla
if lista_compras:
    # Muestra todos los artículos de la lista
    print()
    print("Lista de compras:")
    for articulo in lista_compras:
        print(f"- {articulo}")
else:
    # Informa al usuario que la lista está vacía
    print("No se añadieron artículos a la lista.")
