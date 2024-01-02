#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Diccionario

'''
Diccionario (Dictionary):

    Definición: Un diccionario es una colección de
    pares clave-valor, donde cada clave debe ser única.
    Se define utilizando llaves {} y los elementos se
    representan en pares clave: valor.

    Ejemplo: mi_diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Ejemplo"}
'''

mi_diccionario = dict()
mi_otro_diccionario = {}
print(type(mi_diccionario)) # <class 'dict'>

mi_diccionario = {
    "Nombre": "Martin",
    "Apellido": "Gil",
    "Edad": 23,
    "diccionario_2": {
        "titulo": "Diccionario 2", 
        "descripcion": "Diccionario interno de mi_diccionario"
    },
    1 : 1
}

print(mi_diccionario)
# {'Nombre': 'Martin', 'Apellido': 'Gil', 'Edad': 23, 'diccionario_2': {'titulo': 'Diccionario 2', 'descripcion': 'Diccionario interno de mi_diccionario'}}

print(mi_diccionario["diccionario_2"])
# {'titulo': 'Diccionario 2', 'descripcion': 'Diccionario interno de mi_diccionario'}

print(mi_diccionario[1]) # 1

mi_diccionario["nuevo_campo"] = "Nuevo campo"
print(mi_diccionario["nuevo_campo"])

del mi_diccionario["nuevo_campo"]
print(mi_diccionario)

print("Nombre" in mi_diccionario) # True Buscamos por clave
print("Martin" in mi_diccionario) # False Buscamos por clave y no por valor
print("titulo" in mi_diccionario) # False
print("titulo" in mi_diccionario["diccionario_2"])  # True

print(mi_diccionario.items())
# dict_items([('Nombre', 'Martin'), ('Apellido', 'Gil'), ('Edad', 23), ('diccionario_2', {'titulo': 'Diccionario 2', 'descripcion': 'Diccionario interno de mi_diccionario'}), (1, 1)])

print(mi_diccionario.keys())
# dict_keys(['Nombre', 'Apellido', 'Edad', 'diccionario_2', 1])

print(mi_diccionario.values())
# dict_values(['Martin', 'Gil', 23, {'titulo': 'Diccionario 2', 'descripcion': 'Diccionario interno de mi_diccionario'}, 1])

# print(mi_diccionario["ApellidoS"]) Genera una excepción, una forma más segura es emplear el método get()
print(mi_diccionario.get("Apellido")) # Gil
print(mi_diccionario.get("ApellidoS")) # None
print(mi_diccionario.get("ApellidoS", "Valor por defecto para no encontrados")) # Valor por defecto para no encontrados