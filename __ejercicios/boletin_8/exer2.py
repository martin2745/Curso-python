#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe unha función que busque os arquivos con unha extensión específica nun directorio. Recibirá como parámetro obrigatorio a extensión e como opcional a ruta dun directorio. Se non se pasa este dato utilizarase o directorio actual. Devolve unha lista de nomes de ficheiros.

__author__ = "Martín Gil Blanco"

import os


def buscador_extension(extension, ruta=None):
    # Se non nos pasan a ruta, collemos a ruta do directorio de traballo
    if not ruta:
        ruta = os.getcwd()
    
    # Collemos a lista de todoslos ficheiros e carpetas do directorio
    lista_completa = os.listdir(ruta)

    # Creamos unha lista baleira para os arquivos
    lista_arquivos = []

    # Recorremos todolos ficheiros e carpetas
    for elemento in lista_completa:
        # Creamos a ruta do ficheiro (senon realizamos isto tan so temos o nome do ficheiro e entendera que esta no directorio de traballo)
        ruta_ficheiro = os.path.join(ruta,elemento)
        # Comprobamos se e un ficheiro
        if os.path.isfile(ruta_ficheiro):
            # Engadimolo a lista de ficheiros
            lista_arquivos.append(elemento)

    # Lista de arquivos coa extension
    lista_extension = []

    # Recorremos a lista de ficheiros
    for ficheiro in lista_arquivos:
        # Collemos a extension: primeiro partimos o nome do ficheiro por puntos, e da lista recibida collemos o ultimo elemento da lista
        extension_ficheiro = ficheiro.split(".")[-1]
        # Comprobamos a extension do ficheiro coincide coa extension pasada a función
        if extension == extension_ficheiro:
            # Engadimos o ficheiro a lista
            lista_extension.append(ficheiro)

    # Devolvemos a lista cos ficheiros coa extension
    return lista_extension

def buscador_extension_comphresion(extension, ruta=None):
    # Se non nos pasan a ruta, collemos a ruta do directorio de traballo
    if not ruta:
        ruta = os.getcwd()
    
    # Collemos a lista de todoslos ficheiros e carpetas do directorio
    lista_completa = os.listdir(ruta)

    # Utilizamos list comphresion para coller os ficheiros
    lista_arquivos = [x for x in lista_completa if os.path.isfile(os.path.join(ruta,x))]

    # Utilizamos list comphresion para coller os ficheiros coa extension que se pasa a funcion
    lista_extension = [ficheiro for ficheiro in lista_arquivos if ficheiro.split(".")[-1] == extension]

    return lista_extension