#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe unha función que elimine os arquivos dun directorio se teñen máis dunha cantidade de días. Recibirá como parámetro obrigatorio a cantidade de días como un enteiro e como opcional a ruta dun directorio. Se non se pasa este dato utilizarase o directorio actual. 

__author__ = "Martín Gil Blanco"

import os
from datetime import datetime,timedelta

def eliminar_antigos(dias, ruta=None):
    # Se non nos pasan a ruta, collemos a ruta do directorio de traballo
    if not ruta:
        ruta = os.getcwd()
    
    # Collemos a lista de todoslos ficheiros e carpetas do directorio
    lista_completa = os.listdir(ruta)

    # Utilizamos list comphresion para coller os ficheiros
    lista_arquivos = [x for x in lista_completa if os.path.isfile(os.path.join(ruta,x))]

    # Collemos a diferencia de tempo en dias
    delta = timedelta(days=dias)

    # Collemos o dia e hora ao partir do cal eliminaremos os arquivos
    frontera_eliminacion = datetime.now() - delta

    # Recorremos a lista de arquivos
    for arquivo in lista_arquivos:
        # Creamos a ruta do arquivo
        ruta_arquivo = os.path.join(ruta, arquivo)
        # Collemos a data de modificacion do ficheiro
        data_modificacion = os.path.getmtime(ruta_arquivo)
        # Pasamos a data de modificacion doa arquivo a un arquivo datatime
        data_modificacion_dt = datetime.fromtimestamp(data_modificacion)
        # Comparamos data de modificacion coa data de fronteira calculada
        if data_modificacion_dt < frontera_eliminacion:
            # Se a da ta de modificacion e mais antiga, eliminamos o arquivo
            os.remove(ruta_arquivo)


eliminar_antigos(1, "/home/martin/Imágenes/Capturas de pantalla")