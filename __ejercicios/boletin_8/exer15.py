#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fai un *script* con dúas funcións que permitirá eliminar arquivos duplicados nun directorio:

__author__ = "Martín Gil Blanco"

import os
import hashlib

def obter_hash(directorio):

    # Creamos un dicionario baleiro no que gardamos todolos dicionarios
    dicionario_hash = {}

    # Collemos a lista de todolos arquivos e carpetas
    lista_completa = os.listdir(directorio)
    # Filtramos so os arquivos
    lista_arquivos = [x for x in lista_completa if os.path.isfile(os.path.join(directorio,x))]

    # Recorremos todolos ficheiros
    for nome_arquivo in lista_arquivos:
        # Construimos a ruta de cada un dos ficheiros
        ruta_arquivo = os.path.join(directorio, nome_arquivo)
        # abrimolo en binario
        with open(ruta_arquivo, 'rb') as arquivo:
            # Lemos o contido e creamos o seu hash
            contido = arquivo.read()
            hash_arquivo = hashlib.sha256(contido).hexdigest()
        
        # Comprobamos se o hash esta no dicionario como clave
        if hash_arquivo in dicionario_hash:
            # Como esta metemolo na lista xa creada
            dicionario_hash[hash_arquivo].append(ruta_arquivo)
        else:
            # Se non existe creamos a clave e como valor unha lista co nome do ficheiro
            dicionario_hash[hash_arquivo] = [ruta_arquivo]
    
    # Devolvemos o dicionario
    return dicionario_hash

def eliminar_duplicados(dicionario_hash):
    # Abrimos o ficheiro de log
    arquivo_log = open("eliminados.log", "w")
    # Recorremos a dicionario collendo tanto clave como valor
    for clave, valor in dicionario_hash.items():
        # So facemos algo se a lonxitude do valor e maior a 1, e dicir que hai duplicados
        if len(valor) > 1:
            # Recorremos a lista de duplicados pero obviando o primeiro valor, asi ese non o elimnamos
            for ruta_arquivo in valor[1:]:
                # Eliminamos o ficheiro e escribimolo no log
                os.remove(ruta_arquivo)
                arquivo_log.write(ruta_arquivo + "\n")
    
    # Cerramos o ficheiro de log
    arquivo_log.close()




dicionario = obter_hash("/home/martin/Imágenes/Capturas de pantalla")
print(dicionario)
eliminar_duplicados(dicionario)