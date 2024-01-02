#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Programa que solicita al usuario los coeficientes de una ecuación de segundo grado y
    calcula las dos soluciones. Muestra las dos soluciones por pantalla.
'''

from math import sqrt

__author__ = "Martín Gil Blanco"

coe_a = float(input("Por favor, introduzca el valor del coeficiente a: "))
coe_b = float(input("Por favor, introduzca el valor del coeficiente b: "))
coe_c = float(input("Por favor, introduzca el valor del coeficiente c: "))

neg_b = coe_b * -1
coe_belv2 = coe_b**2
doscoe_a = 2*coe_a
poraporc = 4 * coe_a * coe_c
raizcuadrada = sqrt(coe_belv2 - poraporc)
valor_x = neg_b - raizcuadrada / doscoe_a

print("El valor de x con los coeficientes definidos puede ser " + str(-valor_x) + " o " + str(valor_x))
