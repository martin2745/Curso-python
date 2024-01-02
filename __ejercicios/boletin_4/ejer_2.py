#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea un programa que muestre los números pares 
    hasta el valor introducido por el usuario.
'''

__author__ = "Martín Gil Blanco"

import utils

texto = "Introduce un valor mayor a 0 para mostrar los números pares desde cero hasta ese número: "
num = utils.pide_entero_mayor_cero(texto)

if num % 2 != 0:
    fin = num - 1
else:
    fin = num

incremento = 0

while fin >= incremento:
    print(f"Desde 0 hasta {num}, tenemos el número par:",incremento)
    incremento += 2
else:
    print("Fin de la ejecución")