#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Modifica o exercicio anterior para que ademais se realice unha busca nos subdirectorios do directorio.

__author__ = "Martín Gil Blanco"

import os

def buscador_extension_recursivo(extension, ruta=None):
    # Se non nos pasan a ruta, collemos a ruta do directorio de traballo
    if not ruta:
        ruta = os.getcwd()
    
    # Collemos a lista de todoslos ficheiros e carpetas do directorio
    lista_completa = os.listdir(ruta)

    # Creamos unha lista baleira para os arquivos
    lista_extension = []

    # Recorremos todolos ficheiros e carpetas
    for elemento in lista_completa:
        # Creamos a ruta do ficheiro (senon realizamos isto tan so temos o nome do ficheiro e entendera que esta no directorio de traballo)
        ruta_ficheiro = os.path.join(ruta,elemento)
        
        # Comprobamos se e un ficheiro
        if os.path.isfile(ruta_ficheiro):
            # Collemos a extension fo ficheiro
            extension_ficheiro = elemento.split(".")[-1]
            # Comprobamos se e un ficheiro da extension que se pide
            if extension_ficheiro == extension:
                # Se e metemolo coa ruta para poder diferencialos se hai varios co mesmo nome en diferentes directios 
                lista_extension.append(os.path.join(ruta,elemento))
        else:
            # Se e un directorio, collemos todolos arquivos coa extension e concatenamola ca nosa lista actual
            lista_extension = lista_extension + buscador_extension_recursivo(extension,os.path.join(ruta,elemento))

    # Devolvemos a lista
    return lista_extension

print(buscador_extension_recursivo("py","/home/martin/repos"))