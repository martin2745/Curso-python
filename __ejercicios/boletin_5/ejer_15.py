#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea un programa que le pida al usuario su DNI y compruebe que sea correcto.
'''

__author__ = "Martín Gil Blanco"

def calcular_letra_dni(numero_dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    indice_letra = int(numero_dni) % 23
    return letras[indice_letra]

def comprobar_dni(dni):
    try:
        numero_dni = int(dni[:-1])
        letra_ingresada = dni[-1].upper()
        letra_calculada = calcular_letra_dni(numero_dni)

        if letra_ingresada == letra_calculada:
            return True
        else:
            return False
    except ValueError:
        return False

def main():
    dni_usuario = input("Ingrese su DNI (sin la letra): ")

    if comprobar_dni(dni_usuario):
        print("El DNI es válido.")
    else:
        print("El DNI no es válido.")