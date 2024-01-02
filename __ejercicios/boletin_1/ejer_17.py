#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Programa que solicita al usuario el número de kilómetros recorridos en su último viaje en coche,
    el consumo del coche en litros cada 100 kilómetros y el precio en euros de un litro de combustible.
    Calcula el costo del viaje y lo muestra al usuario por pantalla.
'''

__author__ = "Martín Gil Blanco"

km = float(input("¿Cuántos kilómetros recorrió en su último viaje en coche? "))
consumo = float(input("¿Cuánto consume su vehículo cada cien kilómetros? "))
precio_combustible = float(input("¿Cuánto cuesta un litro del combustible que usa su vehículo? "))

combustible_consumido = km * (consumo/100)
coste = combustible_consumido * precio_combustible

print("Usted consumió un total de",combustible_consumido,"litros, por lo que gastó",coste,sep=" ")
