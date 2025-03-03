"""
Ejercicio 6.
    Escribir un program que muestre todas las tablas de multiplicar del 1 al 10
    mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

"""



print("\nPROGRAMA PARA MOSTRAR TODOS LAS TABLAS DE MULTIPLICAR ENTRE EL 1 Y EL 10\n")

print("\nOPCIÓN 1\n")

numero = 1
while numero <= 10:
    print(f"\n########### Tabla de multiplicar del número {numero} ###########\n")
    
    multiplicador = 1
    while multiplicador <= 10:  
        print(f"{numero} x {multiplicador} = {numero*multiplicador}")
        multiplicador +=1

    numero +=1

    print("\nTabla finaliza.\n")


print("\nOPCIÓN 2\n")

for numero in range(1, 11):  # Iterar sobre los números del 1 al 10
    print('\n##########################################################')
    print(f"########### Tabla de multiplicar del número {numero} ###########")
    print('##########################################################')

    for multiplicador in range(1, 11):  # Multiplicar del 1 al 10
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")

print("\nFin del programa.")
       