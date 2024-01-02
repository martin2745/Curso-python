#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribe un programa que calcule el mínimo común múltiplo
    de dos números introducidos por el usuario.
'''

__author__ = "Martín Gil Blanco"

import utils

def mcm(n1, n2):
    # Cogemos el mayor de los números
    if n1 > n2:
        mayor = n1
    else:
        mayor = n2

    # Buscamos el número divisible por los dos
    while (mayor % n1 != 0) or (mayor % n2 != 0):
        mayor = mayor + 1
    return mayor

n = utils.pide_entero_usuario("Inserte un número entero: ")
m = utils.pide_entero_usuario("Inserte otro número entero: ")

print("El mcm es", mcm(n, m))