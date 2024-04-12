#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A partir do ficheiro `/etc/fstab` e utilizando expresións regulares, crea unha función en Python no que se obteñan tódolos dispositivos montados e o seu punto de montaxe a través deste ficheiro. Devolve esta información nunha lista de dicionarios.

__author__ = "Martín Gil Blanco"

import os
import re


def dispositivos_punto_montaxe():

    # Lista donde gardamos a informacion
    lista = []

    # Ruta do arquivo tab
    fstab = '/etc/fstab'

    # Expresión regular para buscar líneas con el formato del archivo fstab
    regex= re.compile(r'^(\S+)\s+(\S+)\s+\S+\s+\S+\s+\S+\s+\S+$')

    """
    ^: Indica o principio de liña
    \s+: Coincide con un oi máis caracteres de espazo en branco (espazos, tabulacións, etc.).
    \S+: Coincide con un ou máis caracteres que non son espazos en branco. 
        1º: Coincide co dispositivo
        2º: Coincide co punto de montaxe
        3º: Coincide co tipo de sistema de ficheiros
        4º: Coincide coas opcions
        5º Coincide co dump
        6º: Coincide co pass
    ^: Indica o final de liña
    """

    # Abrimolo arquivo
    with open(fstab, 'r') as arquivo_fstab:
        # Lemos linha a linha
        for linha in arquivo_fstab.readlines():
            # Buscamos coincidencias nas linhas que non son comentarios
            if linha[0] != "#":
                match = regex.match(linha)
                # Hai coincidencia
                if match:
                    # Gardamos na lista un dicionario ca informacion que se pidiu
                    lista.append(
                        {
                            "dispositivo": match.group(1),
                            "punto de montaxe": match.group(2)
                        }
                    )
    # Devolvemos a lista
    return lista


print(dispositivos_punto_montaxe())