#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea un módulo que contenga las funciones:
        pide_entero_usuario(texto)
        pide_entero_mayor_cero(texto)
'''

__author__ = "Martín Gil Blanco"

def pide_entero_usuario(texto):
    while True:
        try:
            numero = int(input(texto))
            return numero
        except:
            print("Por favor, introduzca un valor numérico:")

def pide_entero_mayor_cero(texto):
    while True:
        try:
            numero = int(input(texto))
            if numero > 0:
                return numero
            print("El número tiene que ser mayor que 0")
        except:
            print("Por favor, introduzca un valor numérico:")

def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False