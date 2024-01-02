#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Programa que calcule la suma de los N primeros números.
    N se pide al usuario y tiene que ser mayor que 0.
'''

__author__ = "Martín Gil Blanco"

import utils

texto = "Introduzca un número mayor que cero para calcular la suma de los N primeros números: "
num = utils.pide_entero_mayor_cero(texto)
resultado = 0

while num > 0:
    resultado += num
    num -= 1
else:
    print("Fin de la ejecución")

print("La suma de los N primeros números es:", resultado)