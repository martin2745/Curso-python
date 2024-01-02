#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea un programa que realice el cambio de divisas tanto de euros a libras como de libras a euros.
    Crea un menú para que el usuario elija el cambio que desea realizar.
'''

__author__ = "Martín Gil Blanco"

# Valor de 1 € en libras
euro_libras = 0.85 

print("Elige una de las opciones:")
print("\t1) Cambio de euros a libras")
print("\t2) CAmbio de libras a euros")
print("\tCualquier otro caracter para salir")
eleccion = input("> ")

# Opcion 1: de euros a libras
if eleccion == "1":
    try:
        euros = float(input("Introduce los euros: "))
    except:
        print("Se ha producido un error, introduza valores numéricos.")
        exit()
    
    libras = euros * euro_libras
    print(euros,"euros son",libras,"libras")

# Opcion 2: de libras a euros
if eleccion == "2":
    try:
        libras = float(input("Introduce las libras: "))
    except:
        print("Se ha producido un error, introduza valores numéricos.")
        exit()
    
    euros = libras * (1/euro_libras)
    print(libras,"libras son",euros,"euros")

else:
    print("Adios")