#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribir un programa que pregunte por una muestra de números,
    separados por comas, los guarde en una tupla y muestre por pantalla
    su media y desviación típica.
'''

__author__ = "Martín Gil Blanco"

import statistics

# Pedir al usuario una muestra de números separados por comas
entrada_usuario = input("Introduce una muestra de números separados por comas: ")

# Convertir la entrada en una lista de números
numeros = [float(x.strip()) for x in entrada_usuario.split(',')]

# Convertir la lista de números a una tupla
muestra = tuple(numeros)

# Calcular y mostrar la media y desviación típica
media = statistics.mean(muestra)
stdev = round(statistics.stdev(muestra),2)

print('La media es', media, ', y la desviación típica es', stdev)
