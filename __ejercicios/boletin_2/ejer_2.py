#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    A partir de un número introducido por pantalla, crear un algoritmo que indique
    si es un número positivo, negativo o igual a cero.
'''

__author__ = "Martín Gil Blanco"

try:
    num = int(input("Introduce un número: "))
except:
    print("Se ha producido un error, introduza valores numéricos.")
    exit()

if num > 0:
    print("El número es mayor que 0")
elif num == 0:
    print("El número es igual a 0")
else:
    print("El número es menor que 0")