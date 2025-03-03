"""
Ejercicio 8.
    Escribir un program que muestre X el porcentaje de X numero.

"""

print("\nPROGRAMA PARA MOSTRAR EL PORCENTAJE DE UN NUMERO\n")

numero = int(input("Inserta un número: "))
porcentaje = int(input(f"¿Que porcentaje quieres sacar del {numero}?: "))

operacion = (numero * (porcentaje/100))

print(f"El {porcentaje}% del {numero} es: {operacion}")



