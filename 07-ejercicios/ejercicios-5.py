"""
Ejercicio 5.
    Escribir un program que muestre todos los numeros
    que el usuario indique entre dos numeros

"""



print("\nPROGRAMA PARA MOSTRAR TODOS LOS NÚMEROS ENTRE DOS NÚMEROS INDICADOS POR EL USUARIO\n")

print("OPCIÓN 1\n")

numero1 = int(input("Inserta el primer número: "))
numero2 = int(input("Inserta el segundo número: "))

# Asegurar que numero1 sea menor que numero2
if numero1 > numero2:
    numero1, numero2 = numero2, numero1  # Intercambia los valores si están en orden inverso

print(f"\nLos números entre {numero1} y {numero2} son:", end=" ")

for contador in range(numero1, numero2 + 1):  # Se usa numero2 + 1 para incluirlo en la lista
    print(contador, end=" ")

print("\n")  # Salto de línea final para estética

print("OPCIÓN 2\n")

numero1 = int(input("Inserta el primer número: "))
numero2 = int(input("Inserta el segundo número: "))

# Asegurar que numero1 sea menor que numero2
if numero1 < numero2:
    for contador in range(numero1, (numero2 + 1)):  # Se usa numero2 + 1 para incluirlo en la lista
        print(contador)
else:
    print("El numero 1 debe ser menor al numero 2")        