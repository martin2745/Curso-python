#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribir un programa que almacene las asignaturas de un curso
    (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
    en una lista, pregunte al usuario la nota que ha sacado en cada
    asignatura y elimine de la lista las asignaturas aprobadas. Al
    final el programa debe mostrar por pantalla las asignaturas que
    el usuario tiene que repetir.
'''

__author__ = "Martín Gil Blanco"

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
suspensas = []
for asignatura in asignaturas:
    score = float(input("¿Qué nota has sacado en " + asignatura + "?: "))
    if score < 5:
        suspensas.append(asignatura)
print("Tienes que repetir " + str(suspensas))