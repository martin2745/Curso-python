#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crea unha función en Python para realizar unha copia de seguridade dun directorio. Débese gardar cada copia de seguridade nun arquivo comprimido que terá como nome o día, mes e ano do momento no que se execute. A función recibirá a carpeta da que se fará a copia de seguridade e o directorio donde se almacenará dita copia.

__author__ = "Martín Gil Blanco"

import os
from datetime import date
import shutil

def facer_copia_seguridade(directorio, directorio_zip):
    
    # Collemos o dia actual
    dia_actual = date.today()
    
    # Collemos o nome de ficheiro, e o nome do ficheiro con extension
    nome_ficheiro = str(dia_actual.year) + str(dia_actual.month) + str(dia_actual.day)
    nome_ficheiro_extension = nome_ficheiro + ".zip"

    # Creamos o arquivo comprimido
    shutil.make_archive(nome_ficheiro, 'zip', directorio)

    # Creamos a nova ruta do ficheiro, na carpeta destino
    nova_localizacion = os.path.join(directorio_zip, nome_ficheiro_extension)

    # Movemos o ficheiro comprimido
    shutil.move(nome_ficheiro_extension, nova_localizacion)


facer_copia_seguridade("content", "/home/martin/Imágenes/Capturas de pantalla")