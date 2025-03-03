"""
Una variable es un contenedor de informacion
que dentro guardara un dato, se puede crear
muchas variables y cada una tenga un dato distinto

"""
texto = "master en python"
texto2 = "Con Johan Bohorquez"
numero = 47
decimal = 6.5


# Mostrar variables de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)


print("----------------------------------------------------")


# sustituir el valor de alguna variables / reasignado variables 
numero = 77
decimal = 8.9
print(numero)
print(decimal)


print("----------------------------------------------------")

# Concatenacion

nombre = "Johan"
apellido = "Bohorquez"

web = "victorrobles.es"


print(nombre + " " + apellido + " - " + web)
print(f"{nombre} {apellido} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellido, web))

print(nombre, apellido, web)