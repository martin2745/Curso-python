#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe unha función que conte a cantidade de ficheiros dun directorio dado por argumento. Deberá devolver a cantidade.

__author__ = "Martín Gil Blanco"

import os

def contador_ficheiros(carpeta):
    # Collemos a lista de todoslos ficheiros e carpetas do directorio
    lista_completa = os.listdir(carpeta)

    # Creamos unha lista baleira para os arquivos
    lista_arquivos = []

    # Recorremos todolos ficheiros e carpetas
    for elemento in lista_completa:
        # Creamos a ruta do ficheiro (senon realizamos isto tan so temos o nome do ficheiro e entendera que esta no directorio de traballo)
        ruta_ficheiro = os.path.join(carpeta,elemento)
        # Comprobamos se e un ficheiro
        if os.path.isfile(ruta_ficheiro):
            # Engadimolo a lista de ficheiros
            lista_arquivos.append(elemento)
    
    # Devolvemos a lonxitude da lista
    return len(lista_arquivos)

# Neste caso utilizamos list comphresion
def contador_ficheiros_comphresion(carpeta):
    lista_completa = os.listdir(carpeta)
    lista_arquivos = [x for x in lista_completa if os.path.isfile(os.path.join(carpeta,x))]
    return len(lista_arquivos)


# Neste caso con programación funcional
def contador_ficheiros_funcional(carpeta):
    lista_completa = os.listdir(carpeta)
    lista_arquivos = list(filter(lambda nome_arquivo: os.path.isfile(os.path.join(carpeta,nome_arquivo)),lista_completa))
    return len(lista_arquivos)
