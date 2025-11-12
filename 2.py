#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
import math

num = int(input("Ingrese un número (0 para salir): "))
contador = 0

if num  == 0:
    print("El número ingresado tiene 1 dígito.")
else:
    while num != 0:
        num = num//10
        contador += 1

print("El numero ingresado tiene ", contador," dígitos.")