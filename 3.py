#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

suma = 0

i = a+1

while i < b:
    suma = suma+i
    i = i+1

print("La suma es: ", suma)