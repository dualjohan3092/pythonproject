"""
# Condicional IF

Si se_cumple_esta_condicion:
    Ejecutar grupo de instruccion
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else.
    otras intrucciones

# Operadores de comparacion

== igual
¡= diferente
< menor que 
> mayor que
<= menor igual que 
>= mayor igual que 


# Operadores de logicos

and = Y 
or = O
! = NEGACION
not = NO

"""


# Ejemplo 1

print("################## Ejemplo 1 ##################")

# color = input("¿Cual es mi color?: ")
color = "verde"

if color == "rojo":
    print("Felicitaciones!!!")
    print("El color es ROJO")
else:
    print("El color NO es CORRECTO")


# Ejemplo 2

print("\n################## Ejemplo 2 ##################")

# year = int(input("¿En que año estamos?: "))
year = 2025

if year >= 2025:
    print(" Estamos del 2025 en adelante !!")
else:
    print(" Es un año anterior a 2025")


# Ejemplo 3

print("\n################## Ejemplo 3 ##################")

nombre = "Johan Bohorquez"
ciudad = "Bogota"
continente = "America"
edad = 16
mayor_de_edad = 18


if edad >= mayor_de_edad:
    print(f"{nombre} es mayor de edad !!")

    if continente != "America":
        print("El usuario NO es Americano")
    else:
        print(f"Es Americano y de {ciudad}")

else:
    print(f"{nombre} NO es mayor de edad")


# Ejemplo 4

print("\n################## Ejemplo 4 ##################")

# dia = int(input("¿En que dia de la semana estamos?: "))
dia = 2

"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana")   
"""

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")


# Ejemplo 5

print("\n################## Ejemplo 5 ##################")

edad_maxima = 65
edad_minima = 18
# edad_oficial = int(input("¿Cual es tu edad?: "))
edad_oficial = 32


if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar !!")
else:
    print("NO esta en edad de trabajar !!")


# Ejemplo 6

print("\n################## Ejemplo 6 ##################")

pais = "Rusia"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana !!")
else:
     print(f"{pais} no es un pais de habla hispana !!")


# Ejemplo 7

print("\n################## Ejemplo 7 ##################")

pais = "España"

if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO un pais de habla hispana !!")
else:
     print(f"{pais} es un pais de habla hispana !!")


# Ejemplo 8

print("\n################## Ejemplo 8 ##################")

pais = "USA"

if  pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO un pais de habla hispana !!")
else:
     print(f"{pais} es un pais de habla hispana !!")