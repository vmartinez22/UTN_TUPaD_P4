#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingresa {cantidad} números enteros:")

i = 1
while i <= cantidad:
    numero = int(input(f"Número {i}: "))
    
    # Contar par o impar
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    
    # Contar positivo o negativo
    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1
    
    i = i + 1

# Resultados
print("\n--- Resultados ---")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")