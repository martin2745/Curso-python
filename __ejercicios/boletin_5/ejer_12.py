#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribir un programa que almacene las matrices:

    a = ((1, 2, 3),
     (4, 5, 6))

    b = ((-1, 0),
        (0, 1),
        (1,1))

    en una tupla y muestre por pantalla su producto.
    Nota: Para representar matrices mediante tuplas 
    usar tuplas anidadas, representando cada vector fila en una tupla.
'''

__author__ = "Martín Gil Blanco"

a = ((1, 2, 3),
     (4, 5, 6))

b = ((-1, 0),
     (0, 1),
     (1,1))

resultado = [[0,0],
          [0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            resultado[i][j] += a[i][k] * b[k][j]

for i in range(len(resultado)):
    resultado[i] = tuple(resultado[i])

resultado = tuple(resultado)

for i in range(len(resultado)):
    print(resultado[i])