#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


import random

# Genera número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)

intentos = 0

print("¡Adivina el número entre 0 y 9!")

while True:
    intento = int(input("Tu intento: "))
    intentos = intentos + 1
    
    if intento == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número secreto en {intentos} intentos")
        break
    elif intento < numero_secreto:
        print("Más alto...")
    else:
        print("Más bajo...")