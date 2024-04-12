# Programa Calculadora Secuencial Interactiva

# Este programa simula una calculadora que puede realizar operaciones aritméticas básicas de manera secuencial.
# El usuario introduce un número, selecciona una operación aritmética (+, -, /, x), e introduce otro número.
# La calculadora ejecuta la operación y espera la siguiente entrada del usuario.
# Este proceso se repite hasta que el usuario introduce '=' para mostrar el resultado y terminar el programa.

# Solicita al usuario el primer número
print("Calculadora Secuencial Interactiva")
resultado = float(input("Introduce el primer número: "))

# Inicia un bucle para solicitar operaciones y números adicionales
while True:
    # Solicita al usuario la operación a realizar
    operacion = input("Introduce la operación (+, -, /, x, =): ")
    
    # Verifica si el usuario desea terminar y mostrar el resultado
    if operacion == "=":
        print("El resultado es:", resultado)
        break  # Termina el bucle y finaliza el programa
    
    # Solicita al usuario el siguiente número
    numero = float(input("Introduce el siguiente número: "))
    
    # Utiliza match para determinar la operación a realizar
    match operacion:
        case '+':
            resultado += numero
        case '-':
            resultado -= numero
        case '/':
            if numero != 0:  # Evita la división por cero
                resultado /= numero
            else:
                print("Error: División por cero. Por favor, intenta nuevamente.")
                continue  # Permite al usuario corregir su entrada sin terminar el programa
        case 'x':
            resultado *= numero
        case _:  # Captura cualquier entrada que no sea una operación válida
            print("Operación no válida. Por favor, intenta nuevamente.")

# Nota: Este programa no maneja errores de entrada no numérica. Se asume que el usuario introduce números válidos.
