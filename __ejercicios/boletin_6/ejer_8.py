#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribir un programa que cree un diccionario de traducción
    español-inglés. El usuario introducirá las palabras en español
    e inglés separadas por dos puntos, y cada par <palabra>:<traducción>
    separados por comas. El programa debe crear un diccionario con las
    palabras y sus traducciones. Después pedirá una frase en español y
    utilizará el diccionario para traducirla palabra a palabra. Si una
    palabra no está en el diccionario debe dejarla sin traducir.
'''

__author__ = "Martín Gil Blanco"

diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')