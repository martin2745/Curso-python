#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Aplicación que solicite las notas de un examen de los alumnos
    de una clase y cuente el número de aprobados y suspensos.
    Cuando el usuario introduzca un número inferior a 0 o superior
    a 10, no se solicitarán más notas y se indicará el número total
    de aprobados y suspensos.
'''

__author__ = "Martín Gil Blanco"

import utils

aprobados = 0
suspensos = 0

while True:
    mensaxe = input("Introduzca unha nota: ")

    try:
        nota = float(mensaxe)
    except:
        print("Por favor, introduzca un número decimal.")
        continue

    if nota < 0 or nota > 10:
        print("Finalización de introdución de notas")
        break

    if nota >= 5:
        aprobados = aprobados + 1
    else:
        suspensos = suspensos + 1

print("Número de aprobados: ", aprobados)
print("Número de suspensos: ", suspensos)

print("\n--------------\n")