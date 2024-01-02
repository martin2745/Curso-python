#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribir un programa que pida al usuario una palabra y muestre
    por pantalla el número de veces que contiene cada vocal.
'''

__author__ = "Martín Gil Blanco"

palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in vocales:
    times = palabra.lower().count(vocal)  # Ignora mayúsculas/minúsculas y usa count()
    print(f"La vocal {vocal} aparece {times} veces")
