#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Realiza un programa que visualice las potencias para una base dada,
    hasta un exponente determinado. Si la base es 2 y el exponente es 10
    deberá mostrar 2^0, 2^1…2^10.
'''

__author__ = "Martín Gil Blanco"

import utils

texto_base = "Introduce la base numérica: "
texto_exponente = "Introduce el número de exponentes que quieres calcular: "

base = utils.pide_entero_mayor_cero(texto_base)
exp = utils.pide_entero_mayor_cero(texto_exponente)
i = 0

while i <= exp:
    print(f"{base}^{i}:", base**i)
    i += 1