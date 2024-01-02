#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribir un programa que almacene las asignaturas de un curso 
    (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
    en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
    donde <asignatura> es cada una de las asignaturas de la lista.
'''

__author__ = "Martín Gil Blanco"

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for asignatura in asignaturas:
    print("Yo estudio " + asignatura)