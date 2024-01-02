#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Programa que solicite al usuario dos números enteros y determine si la suma es mayor que 10. 
    Haz un control de excepciones si no se introducen valores numéricos.
'''

__author__ = "Martín Gil Blanco"

try:
    num1 = int(input("Introduce el primeiro número: "))
    num2 = int(input("Introduce el segundo número: "))
except:
    print("Se ha producido un error, introduza valores numéricos.")
    exit()

suma = num1 + num2

print("La suma es mayor que 10") if suma > 10 else print("La suma es menor que 10")