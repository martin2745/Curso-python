#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Comprensión de listas

mi_lista_origina = [22, 14, 64, 28, 32, 28, 18]

# Operación -- for -- elementos a recorrer
# Forma de crear listas de forma rápida o en base a listas existentes

mi_lista = [i/10 for i in mi_lista_origina]
print("Divide i/10:")
print(mi_lista)

mi_lista = [i+1 for i in range(8)]
print("\nRango de los 8 primeros elementos + 1:")
print(mi_lista)

mi_lista = [i*2 for i in range(8)]
print("\nRango de los 8 primeros elementos * 2:")
print(mi_lista)

mi_lista = [i*i for i in range(8)]
print("\nRango de los 8 primeros elementos * i:")
print(mi_lista)

# Tambien puedo llamar a otra función para hacer la operación deseada

def sum_cinco(num):
    return num + 5

print("\nRango de los 8 primeros elementos + 5:")
mi_lista = [sum_cinco(i) for i in range(8)]
print(mi_lista)