#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Programa que solicita al usuario su nombre y apellidos por separado, y muestra el siguiente mensaje por pantalla:
    "El usuario Apellido1 Apellido2, Nombre se ha registrado correctamente".
    NOTA: los dos apellidos se pueden pedir juntos; lo que se debe pedir por separado es el nombre por un lado y los apellidos por otro.
'''

__author__ = "Martín Gil Blanco"

nombre = input("Introduzca su nombre: ")
apellido1 = input("Introduzca su primer apellido: ")
apellido2 = input("Introduzca su segundo apellido: ")

print("El usuario " + apellido1 + " " + apellido2 + ", " + nombre +" se registró correctamente.")
