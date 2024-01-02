#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Pedir al usuario base y altura de un triángulo y calcular su área. Mostrar el resultado por pantalla.
'''

__author__ = "Martín Gil Blanco"

base = float(input("Introduce la base del triángulo: "))
altura = float(input("Introduce la altura del triángulo: "))
area = (base * altura) / 2
print(f"El resultado de juntar {base} con {altura} es:", area)