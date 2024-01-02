#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribir un programa que pregunte al usuario su nombre, edad, 
    dirección y teléfono y lo guarde en un diccionario. Después 
    debe mostrar por pantalla el mensaje <nombre> tiene <edad> 
    años, vive en <dirección> y su número de teléfono es <teléfono>.
    Guarda la información en un archivo json.
'''

__author__ = "Martín Gil Blanco"

import json

def escribe_archivo_json(nombre_archivo, contenido):
    with open(nombre_archivo, "w") as archivo:
        json.dump(contenido, archivo, indent=2)

nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])

ruta_archivo = "ejer_2.json"
escribe_archivo_json(ruta_archivo, persona)