#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Realizar una aplicación que imprima los números impares comprendidos
    en un intervalo (a, b). Una vez introducido el intervalo, verificar
    que "a" es menor que "b". Si no es así, invierte los valores.
'''

__author__ = "Martín Gil Blanco"

import utils

def imprimir_impares_en_intervalo(a, b):
    if a > b: a, b = b, a
    print(f"Números impares en el intervalo ({a}, {b}):")
    # Itera sobre cada número en el rango desde a hasta b-1
    for numero in range(a, b):
        if numero % 2 != 0:
            print(numero)

texto_a = "Introduce el valor de a: "
texto_b = "Introduce el valor de b: "
a = utils.pide_entero_mayor_cero(texto_a)
b = utils.pide_entero_mayor_cero(texto_b)

imprimir_impares_en_intervalo(a, b)
