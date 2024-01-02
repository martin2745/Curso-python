#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea un programa para calcular el factorial de un número
'''

__author__ = "Martín Gil Blanco"

import utils

num = utils.pide_entero_usuario("Introduce un número entero: ")
factorial = 1

while num < 0:
    num = utils.pide_entero_usuario("Introduce un número entero: ")

while num > 0:
    factorial *= num
    num -= 1

print("El factorial es:", factorial)