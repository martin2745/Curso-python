#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea un programa que realice el cambio de divisas tanto de euros
    a libras como de libras a euros (1 libra = 1.10 euros). Crea un
    menú para que el usuario elija el cambio que desea realizar.
    Realiza una función para cada uno de los cambios.
'''

__author__ = "Martín Gil Blanco"

def libras_a_euros(libras):
    return round(libras * 1.10, 2)

def euros_a_libras(euros):
    return round(euros * (1/1.10), 2)

print("Seleccione una opción")
print("\t1) Cambio de libras a euros")
print("\t2) Cambio de euros a libras")

try:
    opcion = int(input(">"))
except:
    print("Selecciona una opción válida.")
    exit()

# De libras a euros
if opcion == 1:
    try:
        libras = float(input("Introduzca las libras:"))
    except:
        print("Introduzca un valor válido")
        exit()

    if libras < 0:
        print("Introduzca un valor válido")
        exit()

    print("El valor en euros es", libras_a_euros(libras))

# De euros a libras
if opcion == 2:
    try:
        euros = float(input("Introduzca los euros:"))
    except:
        print("Introduzca un valor válido")
        exit()

    if euros < 0:
        print("Introduzca un valor válido")
        exit()

    print("El valor en libras es", euros_a_libras(euros))