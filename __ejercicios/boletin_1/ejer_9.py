#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Pedir al usuario el radio de una circunferencia y calcular su perímetro y área. 
    Mostrar el resultado por pantalla.
'''

__author__ = "Martín Gil Blanco"

from math import pi as PI_VALUE

radio = float(input("Introduce el radio de una circunferencia en cm: "))

perimetro = 2 * PI_VALUE * radio
area = PI_VALUE * radio**2

# Mostramos o resultado por pantalla
print("El perímetro de la circunferencia es",round(perimetro,2),"cm")
print("El área de la circunferencia es",round(area,2),"cm^2")