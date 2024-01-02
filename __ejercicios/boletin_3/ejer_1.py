#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea un programa que informe si un número es par o impar. 
    Este algoritmo debe estar dentro de una función definida 
    como: comprobar_par()
'''

__author__ = "Martín Gil Blanco"

def comproba_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

try:
    numero = int(input("Ingrese un número por consola: "))
except:
    print("Se ha producido un error, introduza valores numéricos.")
    exit()

es_par = comproba_par(numero)

print("El número es par") if es_par else print("El número no es par")