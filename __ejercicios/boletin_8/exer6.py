#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe unha función que devolva o ficheiro máis grande dentro do directorio actual e os seus subdirectorios. Débese de utilizar recursividade para simplificar dito algoritmo. A función devolverá a ruta absoluta do ficheiro.

__author__ = "Martín Gil Blanco"

import os

def buscador_arquivo_mais_pesado(ruta=None):
    # Se non nos pasan a ruta, collemos a ruta do directorio de traballo
    if not ruta:
        ruta = os.getcwd()

    # Imos gardando o arquivo mais grande e o seu tamaño
    arquivo_mais_grande = ""
    peso_mais_grande = -1
    
    # Collemos a lista de todoslos ficheiros e carpetas do directorio
    lista_completa = os.listdir(ruta)

    # Recorremos todolos ficheiros e carpetas
    for elemento in lista_completa:
        # Creamos a ruta do ficheiro (senon realizamos isto tan so temos o nome do ficheiro e entendera que esta no directorio de traballo)
        ruta_ficheiro = os.path.join(ruta,elemento)

        # Comprobamos se e un ficheiro
        if os.path.isfile(ruta_ficheiro):
            # Collemos o peso do ficheiro
            tamano_arquivo_bytes = os.path.getsize(ruta_ficheiro)

        else:
            # En cambio se e un directorio collemos a ruta do ficheiro mais grande dese directorio e o seu tamaño
            ruta_directorio = os.path.join(ruta, elemento)
            ruta_ficheiro, tamano_arquivo_bytes = buscador_arquivo_mais_pesado(ruta_directorio)
        
        # Se o tamaño adquirido e mais grande que o actual mais grande, modificamos as variables con esta informacion
        if tamano_arquivo_bytes > peso_mais_grande:
            arquivo_mais_grande = ruta_ficheiro
            peso_mais_grande = tamano_arquivo_bytes
            
    
    # Devolvemos a lista
    return arquivo_mais_grande, peso_mais_grande