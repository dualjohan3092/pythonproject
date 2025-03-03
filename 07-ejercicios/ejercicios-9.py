"""
Ejercicio 9.
    Hacer un programa que muestre un numero indefinidamente
    hasta insertar el numero 111

"""
print("\nPROGRAMA PARA MOSTRAR UN NUMERO INDEFINIDAMENTE\n")

contador = 1
while contador < 100:
    numero = int(input("Inserta un número: "))

    if numero == 111:
        break
    else:
        print(f"Has introducido el {numero}")
