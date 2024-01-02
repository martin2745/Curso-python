#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Bucles

# While

mi_condicion = 0

while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while mi_condicion < 20:
    mi_condicion += 1
    if mi_condicion == 15:
        print("Se detiene la ejecución")
        break
    print(mi_condicion)

print("La ejecución continúa")

# For

mi_lista = [23, 24, 62, 52, 30, 30, 17]

for element in mi_lista:
    print(element)

mi_tupla = (23, 1.77, "Martin", "Gil", "Martin")

for element in mi_tupla:
    print(element)

mi_conjunto = {"Martin", "Gil", 23}

for element in mi_conjunto:
    print(element)

mi_diccionario = {"Nombre": "Martin", "Apellido": "Gil", "Edad": 23, 1: "Python"}

for element in mi_diccionario:
    print(element)
    if element == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")

for element in mi_diccionario:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")

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