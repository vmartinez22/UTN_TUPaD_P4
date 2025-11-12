#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

n = int(input("Ingresa un número entero positivo: "))

suma = 0

i = 0
while i <= n:
    suma = suma + i
    i = i + 1

print(f"La suma de 0 hasta {n} es: {suma}")