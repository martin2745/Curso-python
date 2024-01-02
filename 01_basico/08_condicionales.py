#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Condicionales

# if

mi_condicion = False

if mi_condicion:  # Es lo mismo que if mi_condicion mi_condicion == True:
    print("Se ejecuta la condición del if")

mi_condicion = 5 * 5

if mi_condicion == 10:
    print("Se ejecuta la condición del segundo if")

# if, elif, else

if mi_condicion > 10 and mi_condicion < 20:
    print("Es mayor que 10 y menor que 20")
elif mi_condicion == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")