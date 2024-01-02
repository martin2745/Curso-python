#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Realizar un programa que nos muestre los números del 1 al N (introducido por pantalla). 
    El programa indicará:
        El número de pares.
        El número de impares.
        La suma total de todos los números.
        La media solo de los números pares.
'''

__author__ = "Martín Gil Blanco"

import utils

n = utils.pide_entero_mayor_cero("Dame N: ")

# Iterador
i = 1

# Acumuladores
numero_pares = 0
numero_impares = 0
suma_total = 0
suma_pares = 0

# Recorremos todos los números
while i <= n:

    # Calculamos lo que se nos pide
    suma_total = suma_total + i
    if utils.es_par(i):
        numero_pares = numero_pares + 1
        suma_pares = suma_pares + i
    else:
        numero_impares = numero_impares + 1

    # Sumamos el iterador
    i += 1

# Calulamos a media de pares
media_pares = suma_pares / numero_pares

# Imprimimos lo que nos pide el ejercicio
print("Número pares: ", numero_pares)
print("Nñumero impares: ", numero_impares)
print("Suma total: ", suma_total)
print("Media pares: ", media_pares)