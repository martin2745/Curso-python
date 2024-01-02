#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Tuplas

'''
Tupla (Tuple):

    Definición: Una tupla es similar a una lista,
    pero es inmutable, lo que significa que no puedes
    modificar sus elementos después de haber sido
    creada. Se define utilizando paréntesis ().

    Ejemplo: mi_tupla = (1, 2, 3, "cuatro")
'''

mi_tupla = tuple()
mi_otra_tupla = ()
mi_tupla = (23, 1.77,  "Martin", "Gil", "Martin")

print(type(mi_tupla))
print(mi_tupla[2])
print(mi_tupla.count("Martin")) # 2
print(mi_tupla.index("Gil")) # 3

# mi_tupla[5] = "nuevo" No se puede modificar el valor de la tupla
mi_otra_tupla = mi_tupla + mi_tupla
print(mi_otra_tupla)

# Puedo convertir una tupla en lista
mi_lista = list(mi_tupla)
print(type(mi_lista)) # <class 'list'>
print(type(mi_tupla)) # <class 'tuple'>
print(id(mi_lista)) # 3201672100672
print(id(mi_tupla)) # 3201669389648

mi_lista.append("nuevo")
print(mi_lista) # [23, 1.77, 'Martin', 'Gil', 'Martin', 'nuevo']