"""
Ejercicio 3.
    Escribir program que muestre los cuadrados
    (un numero multiplicado por si mismo) de los 60 primeros 
    numeros naturales.
        - Resolverlos con FOR y WHILE
        
"""


# CODIGO PARA DETERMINAR SI UN MUNERO ES PAR O IMPAR
print("\nPROGRAMA PARA MOSTRAR LOS NÚMEROS CUADRADOS DEL 1 AL 60\n")

print("\n----- FOR -----\n")

print("OPCIÓN 1\n")
for numero in range(61):
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")

print("\nOPCIÓN 2\n")
print("El resultado cuadrado del 1 al 60 es:", end=" ")  
for numero in range(1, 61):
    print(numero ** 2, end=", ")

print("\n\n----- WHILE -----\n")

print("OPCIÓN 1\n")
numero = 0
while numero <= 60:
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")
    numero += 1

print("\nOPCIÓN 2\n")
print("El resultado cuadrado del 1 al 60 es:", end=" ")  
numero = 0
while numero <= 60:
    print(numero ** 2, end=", ")
    numero += 1

print("\n")  # Salto de línea final para estética
