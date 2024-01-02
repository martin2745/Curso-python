#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' 
    Realiza una calculadora que reciba una cantidad de Libras y realice el cambio 
    de divisas a euros. Vamos a suponer que el cambio de libra a euros está en 
    1 libra = 1.10 euros. Muestra el resultado por pantalla.
'''

__author__ = "Martín Gil Blanco"

libras = float(input("Ingrese la cantidad en libras: "))
euros = round(libras * 1.10, 2)
print("Sus libras equivalen a un total de ", euros, "€")
