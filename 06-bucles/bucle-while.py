"""
# BUCLE WHILE

Estructura de control que itera o repite la ejecucion de una 
serie de intrucciones tantas veces como sea necesario, 
hasta que deja cumplirse la condicion

while condicion:
    bloque de instrucciones
    actualizacion de contador


"""

print("\n################## Ejemplo ##################")    

contador = 1

while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador += 1

print("-------------------------------------------------")    

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador +=1

print(muestrame) 



# Ejemplo

print("\n################## Ejemplo ##################")    

numero_usuario = int(input("¿De que número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"########### Tabla de multiplicar del número {numero_usuario} ###########")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    contador +=1
else:
    print("Tabla finaliza.")