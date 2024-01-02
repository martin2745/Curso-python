#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Sumar una cantidad de números introducidos por teclado hasta
    que la suma total de los números sea 100 o más de 100.
'''

__author__ = "Martín Gil Blanco"

import utils

## Versión 1
suma = 0
while True:
    numero = utils.pide_entero_usuario("Introduzca un número enteiro: ")
    suma = suma + numero
    if suma >= 100:
        break
print("La suma de los números introducidos llegó a 100 o más. Total:", suma)

## Versión 2
suma = 0

while suma < 100:
    numero = utils.pide_entero_usuario("Introduzca un número enteiro: ")
    suma = suma + numero
print("La suma de los números introducidos llegó a 100 o más. Total:", suma)

## Versión 3
suma = 0
flag = True

while flag:
    numero = utils.pide_entero_usuario("Introduzca un número enteiro: ")
    suma = suma + numero
    if suma >= 100:
        flag = False
print("La suma de los números introducidos llegó a 100 o más. Total:", suma)

