#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Realiza un programa que lea un número y determine si está entre 10 y 100 (ambos inclusive).
    Haz un control de excepciones si no se introducen valores numéricos.
'''

__author__ = "Martín Gil Blanco"

try:
    num = float(input("Introduce un número: "))
except:
    print("Se ha producido un error, introduza valores numéricos.")
    exit()

if (num >= 10) and (num <= 100):
    print("El número está entre 10 y 100")
else:
    print("El número no está entre 10 y 100")
