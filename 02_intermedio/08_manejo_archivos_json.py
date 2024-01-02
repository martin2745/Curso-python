#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Manejo de archivos json

import json

def escribe_archivo_json(nombre_archivo, contenido):
    with open(nombre_archivo, "w") as archivo:
        json.dump(contenido, archivo, indent=2)

def lee_archivo_json(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        contenido = json.load(archivo)
        return contenido

mi_json = {
    "nombre": "Martin",
    "apellido": "Gil",
    "edad": 25,
    "lenguajes": ["Python", "PHP", "Java"],
    "url": "https://www.google.com"
}

ruta_archivo = "02_intermedio/manejo_archivos/prueba.json"

escribe_archivo_json(ruta_archivo, mi_json)
mi_json = lee_archivo_json(ruta_archivo)
for clave, valor in mi_json.items():
        print(f"{clave}: {valor}")
