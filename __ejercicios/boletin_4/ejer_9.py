#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea un programa que reciba un entero (n) mayor o igual a 1 y
    ofrezca el resultado de la siguiente suma:
    1 + 1/2 + 1/3 + ... 1/n 
    NOTA: Utiliza el tipo de datos float para calcular el resultado de la suma.
'''

__author__ = "Martín Gil Blanco"

import utils

def progresion(n):
    i = 1.0
    res = 0.0
    while i <= n:
        res = res + (1.0/i)
        i = i + 1.0
    return res

# Pedimos o numero enteiro
numero = utils.pide_entero_mayor_cero("Ingresa un número entero: ")

resultado = round(progresion(numero), 2)
print("El resultado de la progresión es:", resultado)
