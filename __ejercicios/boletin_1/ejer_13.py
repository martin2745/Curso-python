#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Pedir al usuario el radio y la altura de un cilindro y calcular su volumen. 
    Mostrar el resultado por pantalla.
'''

from math import pi as PI_VALUE

radio = float(input("Indica el radio en cm del cilindro: "))
altura = float(input("Indica la altura en cm del cilindro: "))

volume = round(altura * PI_VALUE * radio ** 2,2)
print("El volumen del cilindro es:", volume, "cm^3")