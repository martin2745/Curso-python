#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribir un programa que almacene las asignaturas de un curso 
    (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
    en una lista y la muestre por pantalla.
'''

__author__ = "Martín Gil Blanco"

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(asignaturas)):
    print(f"La materia {i+1} es: {asignaturas[i]}")
