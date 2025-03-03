"""
Ejercicio 4.
    Escribir program que pida dos numeros al usuario y hacer
    todas las operaciones basicas de una calculadora y mostrarlo en pantalla

"""


# CODIGO PARA DETERMINAR SI UN MUNERO ES PAR O IMPAR
print("\nPROGRAMA PARA MOSTRAR TODAS LAS OPERACIONES BASICAS DE DOS NUMEROS\n")

numero1 = int(input("Inserta el primer numero: "))
numero2 = int(input("Inserta el segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
resto = numero1 % numero2
cuadrado1 = numero1 ** 2
cuadrado2 = numero2 ** 2


print("\n********************* CALCULADORA *********************\n")
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicacion es: {multiplicacion}")
print(f"La division es: {division}")
print(f"La resto de la division es: {resto}")
print(f"El cuadrado del primer numero es {str(cuadrado1)} y el cuadrado del segundo numero es {str(cuadrado2)}")