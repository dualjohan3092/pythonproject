"""
# FOR

for variable in element it (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

"""

contador = 0
resultado = 0

for contador in range(0, 10):
    print("Voy por el " + str(contador))

    resultado = resultado + contador
    resultado += contador

print(f"El resultados es: {resultado}")


# Ejemplo tablas de multiplicador
print("\n################## Ejemplo ##################")

numero_usuario = int(input("¿De que número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"########### Tabla de multiplicar del número {numero_usuario} ###########")

for numero_tabla in range(0, 10):

    if numero_usuario == 45:
        print("No se pueden mostrar numeros prohibidos !!")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finaliza.")