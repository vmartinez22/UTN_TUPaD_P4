#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

cantidad = 100

suma = 0

print(f"Ingresa {cantidad} números enteros:")

i = 1
while i <= cantidad:
    numero = int(input(f"Número {i}: "))
    suma = suma + numero
    i = i + 1

# Calcula la media
media = suma / cantidad

print(f"\nLa media de los {cantidad} números es: {media}")