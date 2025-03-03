"""
Ejercicio 1.
    - Crear variables una "pais" y otra "continente".
    - Mostrar su valor por pantalla (imprimir).
    - Poner un comentario diciendo el tipo de dato.
    - Mostrar su tipo en pantalla (imprimir).

"""
print("PROGRAMA PARA EL CONTENIDO DE UNA VARIABLES Y TU TIPO")

pais = input("¿De que pais vienes?: ")                                    # String
continente = input("¿En que continente que pais vienes?: ")               # String  
year = int(input("¿En que año naciste?: "))                               # integer  
tipo_dato_pais = type(pais)
tipo_dato_continente = type(continente)
tipo_dato_year = type(year)

print(f"Tu pais es {pais}, su tipo es {tipo_dato_pais} y pertenece al {continente}, su tipo es {tipo_dato_continente}, el año de nacimiento es {str(year)}, su tipo es {tipo_dato_year} ")

