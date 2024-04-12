#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe unha función no que a tódolos ficheiros se lles engada a extensión "backup" dun directorio dado por parámetros.

__author__ = "Martín Gil Blanco"

import os
from datetime import datetime,timedelta

def engadir_extension(ruta=None):
    # Se non nos pasan a ruta, collemos a ruta do directorio de traballo
    if not ruta:
        ruta = os.getcwd()
    
    # Collemos a lista de todoslos ficheiros e carpetas do directorio
    lista_completa = os.listdir(ruta)

    # Utilizamos list comphresion para coller os ficheiros
    lista_arquivos = [x for x in lista_completa if os.path.isfile(os.path.join(ruta,x))]

    # Recorremos a lista de arquivos
    for arquivo in lista_arquivos:
        # Creamos a ruta do arquivo antiga
        ruta_arquivo_antiga = os.path.join(ruta, arquivo)
        # Creamos a ruta do arquivo nova
        ruta_arquivo_nova = os.path.join(ruta, arquivo + ".backup")
        # Modificamos o nome dos ficheiros
        os.rename(ruta_arquivo_antiga, ruta_arquivo_nova)


engadir_extension("/home/martin/Imágenes/Capturas de pantalla")