#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribir un programa que pida al usuario una palabra y muestre
    por pantalla si es un palíndromo.
'''

__author__ = "Martín Gil Blanco"

palabra = list(input("Introduce una palabra: "))
palabra_inversa = list(reversed(palabra))

if palabra == palabra_inversa:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
