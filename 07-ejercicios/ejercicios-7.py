"""
Ejercicio 7.
    Escribir un program que muestre todos los numeros impares 
    que decida el usuario entre dos numeros.

"""


numero1 = int(input("Inserta el primer número: "))
numero2 = int(input("Inserta el segundo número: "))

print(f"\nPROGRAMA PARA MOSTRAR LOS NUMEROS PARES ENTRE EL {str(numero1)} Y {str(numero2)}\n")

print("\nOPCIÓN 1\n")

contador = 1

# print (10%3) ## muestra el residuo de una division


for contador in range(numero1, numero2+1):
    if contador % 2 != 0:
        print(f"{contador} es impar") 
    # else:    
        #print(f"{contador} es impar")

print("\nLos números impares son: ", end="\n")  
for contador in range(numero1, numero2+1):
    if contador % 2 != 0:
        print(contador, end=", ")

print("\n")
print("\nOPCIÓN 2\n")

numero1 = int(input("Inserta el primer número: "))
numero2 = int(input("Inserta el segundo número: "))

if numero1 < numero2:
    for X in range(numero1, (numero2 +1)):

        if X%2 == 0:
            print(f"{X} es PAR")
        else:
            print(f"{X} es IMPAR")
else:
    print("El numero 1 debe ser mayor al")