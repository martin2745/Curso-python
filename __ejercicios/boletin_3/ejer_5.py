#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Calcula el importe a pagar por un vehículo al circular por una autopista. 
    Selecciona el vehículo mediante un menú. Si es necesario, pídele al usuario
    los kilómetros recorridos por la autopista y su peso. 
    Crea 4 funciones:
        mostrar_menu que solo muestra el menú.
        calculo_precio_moto
        calculo_precio_turismo
        calculo_precio_camión. 
    Precios:
        Moto: importe fijo de 1€.
        Turismo: 0,25€ por km.
        Camión: 0,25€ por km más 0,15€ por tonelada de peso.
'''

__author__ = "Martín Gil Blanco"

def mostra_menu():
    print("Elige unha opcion:")
    print("\t1) Moto")
    print("\t2) Turismo")
    print("\t3) Camión")

def calculo_precio_camion(km, peso):
    precio = 0.25 * km + 0.15 * peso
    return precio

def calculo_precio_turismo(km):
    precio = km * 0.25
    return precio

def calculo_precio_moto():
    return 1

mostra_menu()
opcion = input(">")

# Opcion de moto
if opcion == "1":
    precio = calculo_precio_moto()
    print("La tarifa a pagar es de", precio, "€")

# Opcion de turismo
elif opcion == "2":
    try:
        kilometros = float(input("Ingrerse el número de km:"))
    except:
        print("Por favor introduza un valor numérico")
        exit()

    precio = calculo_precio_turismo(kilometros)
    print("La tarifa a pagar es de", precio, "€")

# Opcion de camión
elif opcion == "3":
    try:
        kilometros = float(input("Ingrerse o número de km:"))
        toneladas = float(input("Ingrerse o peso en toneladas:"))
    except:
        print("Por favor introduza un valor numérico")
        exit()

    precio = calculo_precio_camion(kilometros, toneladas)
    print("La tarifa a pagar es de", precio, "€")

else:
    print("La opción no existe")