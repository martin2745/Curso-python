#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea una aplicación que solicite al usuario un año e indique si es bisiesto o no. 
    Condiciones para ser bisiesto:
        Debe ser obligatoriamente divisible por 4.
        Si es divisible por 100, también debe ser divisible por 400.
'''

__author__ = "Martín Gil Blanco"

try:
    anho = int(input("Introduce el año: "))
except:
    print("Se ha producido un error, introduza valores numéricos.")
    exit()

if not (anho > 0):
    print("Solo se admiten años después de Cristo")
else:
    if anho % 4 == 0 and anho % 100 == 0 and anho % 400 == 0:
        print("Es bisiesto")
    elif anho % 4 == 0 and anho % 100 != 0:
        print("Es bisiesto")
    else:
        print("No es bisiesto")

