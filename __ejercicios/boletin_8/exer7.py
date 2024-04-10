#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe unha función que reciba a ruta dun directorio e unha cadea de texto. Esta debe buscar en que ficheiros ".txt" se encontra dito texto como contido. Debe devolver unha lista con tódolos nomes deses ficheiros.

__author__ = "Martín Gil Blanco"

import os

def buscador_palabra(ruta, palabra):
    
    # Collemos a lista de todoslos ficheiros e carpetas do directorio
    lista_completa = os.listdir(ruta)

    # Utilizamos list comphresion para coller os ficheiros
    lista_arquivos = [x for x in lista_completa if os.path.isfile(os.path.join(ruta,x))]

    # Utilizamos list comphresion para coller os ficheiros coa extension txt
    lista_txt = [ficheiro for ficheiro in lista_arquivos if ficheiro.split(".")[-1] == "txt"]

    # Aqui alamcenamos a lista dos ficheiros que conteñan a palabra
    lista_encontrados = []

    # Recorremos todolos ficheiros txt da lista
    for nome_ficheiro in lista_txt:
        # Construimos a ruta completa
        ruta_ficheiro = os.path.join(ruta,nome_ficheiro)
        # Abrimos o ficheiro para lectura
        with open(ruta_ficheiro, "r") as ficheiro:
            # Lemos todo o texto do ficheiro
            texto = ficheiro.read()
            # Comprobamos se esta a palabra
            if palabra in texto:
                # Alamcenamos a ruta do ficheiro na lista
                lista_encontrados.append(ruta_ficheiro)
    
    # Devolvemos a lista de encontrados
    return lista_encontrados

print(buscador_palabra("/home/martin/Imágenes/Capturas de pantalla","python"))

