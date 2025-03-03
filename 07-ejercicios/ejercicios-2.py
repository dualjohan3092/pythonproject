"""
Ejercicio 2.
    Escribir en un script que nos muestre 
    todos los numeros pares por pantalla del 1 al 120
"""


# CODIGO PARA DETERMINAR SI UN MUNERO ES PAR O IMPAR
print("PROGRAMA PARA MOSTRAR LOS NUMEROS PARES ENTRE EL 1 Y 120")

contador = 1

# print (10%3) ## muestra el residuo de una division


for contador in range(1, 121):
    if contador%2 == 0:
        print(f"{contador} es par") 
    # else:    
        #print(f"{contador} es impar")

print("Los números pares son:", end=" ")  
for contador in range(1, 121):
    if contador % 2 == 0:
        print(contador, end=", ")


