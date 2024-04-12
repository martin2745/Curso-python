#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crea un *script* que copie tódolos ficheiros do sistema coa extensión "py" no directorio "python". Debes comprobar se existe este directorio, e se existe borrar todo o seu contido. Fai que o *script* se poida executar en Windows e en Linux.

__author__ = "Martín Gil Blanco"

import os, shutil


# Esta e aextension a buscar
estension_a_buscar = "py"
# Este o directorio onde os gardamos
directorio_arquivos = "python"

def obtener_unidades_windows():
    unidades = []
    # Recorremos as letras de unidades da A a Z
    for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        unidade = f"{letra}:\\"
        # Verificamos se a unidade existe como directorio
        if os.path.isdir(unidade):
            unidades.append(unidade)
    return unidades

rutas = []

def buscador_extension(ruta=None):
    # Comprobamos se non temos ruta
    if not ruta:
        # Comprobamos o sistema operativo
        if os.name == "posix":
            # Engadimos a ruta
            ruta = "/"
        else:
            # COmo podemos ter varias inicios de rutas diferentes isto ten que ser distinto
            # Cremos a lista de arquivos de python baleira
            lista_python = []
            # Obtemos as unidades de windows
            lista_directorios = obtener_unidades_windows()
            # Recorremos cada unha das unidades
            for unidade in lista_directorios:
                # COncatenamos a lista de ficheiros co resultante de cada unidade
                lista_python += buscador_py(unidade)
            # Devolvemos a lista final
            return lista_python
    
    # Collemos a lista de todolos arquivos e carpetas
    lista_completa = os.listdir(ruta)
    # Filtramos so os arquivos
    lista_arquivos = [x for x in lista_completa if os.path.isfile(os.path.join(ruta,x))]
    # Filtramos so os arquivos de python e gardamola ca ruta completa
    lista_python = [os.path.join(ruta,ficheiro) for ficheiro in lista_arquivos if ficheiro.split(".")[-1] == estension_a_buscar]
    # Filtramos os directorios
    lista_directorios = [x for x in lista_completa if os.path.isdir(os.path.join(ruta,x))]

    # Recorremos os directorios
    for carpeta in lista_directorios:
        # Comprobamos se estamos en linux
        if os.name == "posix":
            # Comprobamos que non sexa un enlace simbolico
            if not os.path.islink(os.path.join(ruta,carpeta)):
                # Concatenamos os arquivos do directorio inferior co da carpeta
                lista_python += buscador_extension(os.path.join(ruta,carpeta))
        else:
            # Deberiamos comprobar se e un enlace directo
            lista_python += buscador_py(os.path.join(ruta,carpeta))
    # Devolvemos a lista de arquivos Python
    return lista_python

# Collemos todolos arquivos python
arquivos = buscador_extension()


# Comprobamos se o dirctorio existe
if os.path.exists(directorio_arquivos):
    # Se existe eliminamolo
    shutil.rmtree(directorio_arquivos)

# Creamos o directorio
os.mkdir(directorio_arquivos)

# Recorremos todolos arquivos
for arquivo in arquivos:
    # Collemos o nome do arquivo sen a ruta
    nome_arquivo = os.path.basename(arquivo)
    # Construimos a ruta nova do arquivo
    ruta_nova = os.path.join(directorio_arquivos,nome_arquivo)
    # Comprobamos se existe o arquivo(podo ser temporal) e que non haxa xa un co mesmo nome
    if os.path.exists(arquivo) and not os.path.exists(ruta_nova):
        # Realizamos a copia
        shutil.copy(arquivo, ruta_nova)


