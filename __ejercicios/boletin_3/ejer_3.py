#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea una aplicación que solicite al usuario un año e indique si es bisiesto o no. 
    Cuidado, ya que la condición para ser bisiesto no es solo ser divisible entre 4. 
    El algoritmo debe estar dentro de una función denominada es_bisiesto().
'''

__author__ = "Martín Gil Blanco"

def es_bisiesto(ano):
    if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
        return True
    elif ano % 4 == 0 and ano % 100 != 0:
        return True
    else:
        return False

try:
    ano = int(input("Indica un año: "))
except:
    print("Se ha producido un error, introduza valores numéricos.")
    exit()

if ano <= 0:
    print("El año tiene que ser después de Cristo")
    exit()

bisiesto = es_bisiesto(ano)
if bisiesto:
    print("Es bisiesto")
else:
    print("No es bisiesto")




