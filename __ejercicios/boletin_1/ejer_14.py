#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Pedir al usuario el radio de una esfera y calcular su volumen. 
    Mostrar el resultado por pantalla.
'''

from math import pi as PI_VALUE

radio = float(input("Indica el radio en cm de la esfera: "))

volume = round((4/3) * PI_VALUE * (radio**3),2)
print("El volumen de la esfera es:", volume, "cm^3")
