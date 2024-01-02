#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Calcula el importe a pagar por un vehículo al circular por una autopista.
    Selecciona el vehículo mediante un menú. Si es necesario, pídele al usuario los
    kilómetros recorridos por la autopista y su peso.
        Moto: importe fijo de 1€.
        Turismo: 0,25€ por kilómetro.
        Camión: 0,25€ por kilómetro más 0,15€ por tonelada de peso.
'''

__author__ = "Martín Gil Blanco"

print("Elige un transporte:")
print("\t1) Moto")
print("\t2) Turismo")
print("\t3) Camion")
print("\tCualquier otro caracter para salir")
eleccion = input("> ")

# Opcion 1: Moto
if eleccion == "1":
    print("O importe a pagar e de 1 €")

# Opcion 2: Turismo
elif eleccion == "2":
    try:
        km = int(input("Introduce los kilometros recorridos: "))
    except:
        print("Se ha producido un error, introduza valores numéricos.")
        exit()

    if km <= 0:
        print("Necesitamos los kilometros recorridos")
        exit()

    print("El importe a pagar es de", km * 0.25 ,"€")

# Opcion 3: Camión
elif eleccion == "3":
    try:
        km = int(input("Introduce los kilometros recorridos: "))
    except:
        print("Se ha producido un error, introduza valores numéricos.")
        exit()

    if km <= 0:
        print("Necesitamos los kilometros recorridos")
        exit()

    # Pedimos as toneladas
    try:
        toneladas = float(input("Introduce o peso en toneladas: "))
    except:
        print("Se ha producido un error, introduza valores numéricos.")
        exit()

    if toneladas <= 0:
        print("Necesitamos el peso en toneladas")
        exit()

    print("El importe a pagar es de", km * 0.25 + 0.15 * toneladas, "€")

else:
    print("Adios")