"""
FUNCIONES:
    Una funcion es un conjunto de instrucciones agrupadas bajo
    un nombre concreto que pueden reutilizarse invocando a la
    funcion tantas veces como sea necesario.

    def nombreDeMiFuncion(parametros):
        # BLOQUES / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)

"""

# Ejemplo 1

print("\n######### EJEMPLO 1 #########")

# Definir la funcion

def muestraNombre():
    print("\nJohan")
    print("Bimbo")
    print("Cepe")
    print("Lubri")
    print("Parejon")
    print("\n")

# Invocar funcion
muestraNombre()
muestraNombre()
muestraNombre()


# Ejemplo 2 : Parametros

print("\n######### EJEMPLO 2 #########")

#nombre = "Johan Bohorquez"

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

mostrarTuNombre(nombre, edad)
