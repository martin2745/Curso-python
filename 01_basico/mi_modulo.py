#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Módulo para pruebas

'''
Cuando creas un módulo en Python, es posible que se
genere automáticamente una carpeta llamada "pycache".

Esta carpeta se utiliza para almacenar archivos de
caché compilados (.pyc) que contienen el código
bytecode de tus archivos fuente (.py). El bytecode es
una representación intermedia del código fuente que es
más fácilmente ejecutable por la máquina virtual de Python.
'''

def mi_suma(numero_uno, numero_dos, numero_tres):
    print(numero_uno + numero_dos + numero_tres)


def mi_print(valor):
    print(valor)