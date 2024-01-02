#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribir un programa que pregunte al usuario los números ganadores
    de la lotería primitiva, los almacene en una lista y los muestre
    ordenados de menor a mayor.
'''

__author__ = "Martín Gil Blanco"

ganadores = []
for i in range(6):
    ganadores.append(int(input("Introduce un número ganador: ")))
ganadores.sort()
print("Los números ganadores son " + str(ganadores))