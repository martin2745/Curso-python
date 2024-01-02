#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribe un programa que calcule la tabla de multiplicar
    para un número pedido por teclado.
'''

__author__ = "Martín Gil Blanco"

import utils

texto = "Ingrese un numero para mostrar a tabla: "
tabla = utils.pide_entero_mayor_cero(texto)

# Creamos a tabla
i = 0
while i < 10:
    print(tabla, "*", i+1, "=", tabla*(i+1))
    i = i + 1