#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribir un programa que guarde en una variable el diccionario 
    {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}, pregunte al usuario por 
    una divisa y muestre su símbolo o un mensaje de aviso si la 
    divisa no está en el diccionario.
'''

__author__ = "Martín Gil Blanco"

monedas = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))