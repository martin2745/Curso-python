#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Pedir al usuario dos números enteros y mostrar el resto. Mostrar el resultado por pantalla.
'''

__author__ = "Martín Gil Blanco"

entero_1 = int(input("Introduce el primero número entero: "))
entero_2 = int(input("Introduce el segundo número entero: "))
print(f"El resto de la división de {entero_1} y {entero_2} es:", entero_1 % entero_2)