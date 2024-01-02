#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Comprensión de listas

mi_lista_origina = [22, 14, 64, 28, 32, 28, 18]

#        Operación -- for -- elementos a recorrer
mi_lista = [i/10 for i in mi_lista_origina]
print(mi_lista)

mi_lista = [i+1 for i in range(8)]
print(mi_lista)

mi_lista = [i*2 for i in range(8)]
print(mi_lista)

mi_lista = [i*i for i in range(8)]
print(mi_lista)

def sum_five(number):
    return number + 5

mi_lista = [sum_five(i) for i in range(8)]
print(mi_lista)