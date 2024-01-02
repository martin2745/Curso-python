#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea un programa que indique si es par o impar el número introducido.
'''

__author__ = "Martín Gil Blanco"

try:
    num = int(input("Introduce un número: "))
except:
    print("Se ha producido un error, introduza valores numéricos.")
    exit()

print("El número es par") if num % 2 == 0 else print("El número no es par")