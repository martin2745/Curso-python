#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe unha función que substitúa unha palabra dun ficheiro de texto por outra. A función recibirá a ruta do ficheiro, a palabra a substituír e o texto co se realizará o cambio.

__author__ = "Martín Gil Blanco"

def sustituir_palabra_ficheiro(ruta, palabra_orixinal, texto_remprazo):
    # Abrimos o ficheiro en modo lectura
    with open(ruta,"r") as ficheiro:
        # Lemos todo o contido do texto
        texto = ficheiro.read()

    # Remprazamos o texto orixinal polo novo
    # Recordar que un str e inmutable polo que un metodo non modifica o seu estado
    texto = texto.replace(palabra_orixinal, texto_remprazo)

    # Abrimos o mesmo ficheiro para escritura
    with open(ruta,"w") as ficheiro:
        # Escribimos o texto novo no ficheiro
        ficheiro.write(texto)


sustituir_palabra_ficheiro("/home/martin/Imágenes/Capturas de pantalla/si.txt","python","Java")