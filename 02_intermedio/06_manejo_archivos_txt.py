#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Manejo de archivos txt

'''
    La diferencia fundamental entre las dos versiones es
    el uso de la sentencia with que garantiza dos cosas:
    
        - Que siempre se cierre el archivo sin necesidad
        de llamar a .close().
        - En caso de que se produzca una excepción se va
        a llamar a .close() siempre.
'''

'''
    La función open() admite diferentes formas de manejar
    el archivo:
    
    r: Abre el fichero en modo lectura.
    r+: Si quieres leer y escribir en el fichero.
    w: Para sobreescribir el contenido.
    a: Para añadir al final del fichero en el caso de que ya exista.

'''

# -----------------------------------------------

def escribe_archivo_v1(name_file, contenido):
    file = open(name_file, "w")
    file.write(contenido)
    file.close()

def lee_archivo_v1(name_file):
    file = open(name_file, "r")
    toret = file.readlines()
    file.close()
    return toret

def inserta_archivo_v1(name_file, contenido_final):
    file = open(name_file, "a")
    file.write(contenido_final)
    file.close()

# -----------------------------------------------

def escribe_archivo_v2(name_file, contenido):
    with open(name_file, "w") as archivo:
        archivo.write(contenido)

def lee_archivo_v2(name_file):
    toret = []
    with open(name_file, "r") as archivo:
        for linea in archivo:
            toret.append(linea)
    return toret

def inserta_archivo_v2(name_file, contenido_final):
    with open(name_file, "a") as archivo:
        archivo.write(contenido_final)

# -----------------------------------------------

print("----------------Versión 1----------------")

ruta_archivo = "02_intermedio/manejo_archivos/prueba.txt"
escribe_archivo_v1(ruta_archivo, "Hola Mundo!!!\nEspero que te guste el curso")
for linea in lee_archivo_v1(ruta_archivo):
    print(linea.strip())
inserta_archivo_v1(ruta_archivo, "\nInserto al final")

print("----------------Versión 2----------------")

ruta_archivo = "02_intermedio/manejo_archivos/prueba.txt"
escribe_archivo_v2(ruta_archivo, "Hola Mundo!!!\nEspero que te guste el curso")
for linea in lee_archivo_v2(ruta_archivo):
    print(linea.strip())
inserta_archivo_v2(ruta_archivo, "\nInserto al final")