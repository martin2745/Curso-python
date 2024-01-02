#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Calcula el valor del siguiente polinomio 2x^2 + 5x - 3 para el valor de x 
    que especifique el usuario. Muestra el resultado por pantalla.
'''

__author__ = "Martín Gil Blanco"

x = float(input("Indique el valor de la variable x:"))
resultado = 2*(x**2)+ 5 * x -3
print("El valor del polinomio para el valor de x:",x,"es:",resultado)

