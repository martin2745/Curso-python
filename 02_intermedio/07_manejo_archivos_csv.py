#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Manejo de archivos csv

import csv

def escribe_archivo_csv(nombre_archivo, contenido):
    with open(nombre_archivo, "w") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(contenido)

def lee_archivo_csv(nombre_archivo):
    toret = []
    with open(nombre_archivo, "r") as archivo:
        lector_csv = csv.reader(archivo)

        for registro in lector_csv:
            toret.append(registro)

    return toret

'''
    "dia", "mes", "anho"
    1,      1,      1970
    11,     11,      2000
'''

ruta_archivo = "02_intermedio/manejo_archivos/prueba.csv"
contenido = [
        ["dia","mes","anho"],
        [1,1,1970],
        [11,11,2000]
    ]
print(contenido)
escribe_archivo_csv(ruta_archivo, contenido)
mi_csv = lee_archivo_csv(ruta_archivo)
for registro in mi_csv:
    if registro != []: 
        print(registro)