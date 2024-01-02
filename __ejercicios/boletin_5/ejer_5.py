#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribir un programa que almacene en una lista los números del 1 al 10
    y los muestre por pantalla en orden inverso separados por comas.
'''

__author__ = "Martín Gil Blanco"

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.reverse()
for numero in numeros:
    print(numero, end=", ")
