#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Bucles

print("------------------While--------------------\n")

# While

mi_condicion = 0

while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("\n----------------------------------------\n")

mi_condicion = 0

while mi_condicion < 20:
    mi_condicion += 1
    if mi_condicion == 15:
        print("Se detiene la ejecución")
        break
    print(mi_condicion)

print("\n-----------------For--------------------\n")

# For

print("Lista\n")
mi_lista = [23, 24, 62, 52, 30, 30, 17]

for element in mi_lista:
    print(element)

print("\n----------------------------------------\n")

print("Tupla\n")
mi_tupla = (23, 1.77, "Martin", "Gil", "Martin")

for element in mi_tupla:
    print(element)

print("\n----------------------------------------\n")

print("Conjunto\n")

mi_conjunto = {"Martin", "Gil", 23}

for element in mi_conjunto:
    print(element)

print("\n----------------------------------------\n")

print("Diccionario\n")

mi_diccionario = {"Nombre": "Martin", "Apellido": "Gil", "Edad": 23, 1: "Python"}

# Mostrar claves
print("Mostrar claves:\n")
for key in mi_diccionario:
    print(key)

# Mostrar valores
print("\nMostrar valores:\n")
for value in mi_diccionario.values():
    print(value)

# Mostrar claves y valores
print("\nMostrar claves y valores:\n")
for key, value in mi_diccionario.items():
    print(f"{key}: {value}")


print("\n----------------Switch-------------------\n")

# En python no existe el switch pero podemos replicarlo con un diccionario
    
def case_a():
    print("case_a")

def case_b():
    pass

def case_c():
    pass

def default_case():
    pass

def switch_case(caso):
    switch_dict = {
        'a': case_a,
        'b': case_b,
        'c': case_c
    }

    funcion_case = switch_dict.get(caso, default_case)
    resultado = funcion_case()
    return resultado

switch_case('a')

print("\n-------------Continue y break---------------\n")

'''
Diferencia entre continue y break

En el siguiente ejemplo, cuando el contador es par, la declaración 
continue hace que el bucle salte a la siguiente iteración sin ejecutar
el código restante dentro del bucle para ese ciclo en particular.
'''

contador = 0

while contador < 5:
    contador += 1
    # Si el contador es par, salta a la siguiente iteración sin ejecutar el código debajo
    if contador % 2 == 0:
        continue
    print(f"Contador: {contador}")
print("Fin del bucle")

'''
En el siguiente ejemplo, cuando el contador alcanza el valor de 3, 
la declaración break termina abruptamente el bucle, ignorando cualquier
código que pueda seguir después del bucle.
'''

contador = 0

while contador < 5:
    contador += 1
    # Si el contador es 3, se sale del bucle inmediatamente
    if contador == 3:
        break
    print(f"Contador: {contador}")
print("Fin del bucle")