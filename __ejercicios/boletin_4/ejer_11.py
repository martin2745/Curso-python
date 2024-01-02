#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea un programa en el que el usuario pueda introducir números
    enteros hasta que escriba la palabra "fin". Después de escribir
    esto, indícale cuál es el número más pequeño introducido.
'''

__author__ = "Martín Gil Blanco"

menor = None
primera_iteracion = True

while True:
    mensaje = input("Introduce un número o a palabra fin para finalizar: ")

    # Cuando se escriba la palabra fin salimos del bucle
    if mensaje == "fin":
        break

    # Convertimos el texto a número entero
    try:
        numero = int(mensaje)
    except:
        # Si no se introduce un número entero, volvemos al comienzo del bucle
        continue

    # Si es la primera vez, asignamos el número
    if primera_iteracion:
        menor = numero
        primera_iteracion = False

    # Comprobamos si el número introducido era menor
    elif numero < menor:
        menor = numero

# Comprobamos si se introdujo algún número
if primera_iteracion:
    print("No se introdujo ningún número")
# Imprimimos el menor de los números
else:
    print("El número más pequeño ha sido:", menor)