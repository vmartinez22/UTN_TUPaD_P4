#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

suma = 0 #inicializa la suma

print("Ingrese numeros enteros (Para terminar, ingrese un 0): ")

while True:
    numero = int(input("Número: "))

    if numero == 0:
        break

    suma = suma+numero

print("Total acumulado: ", suma)