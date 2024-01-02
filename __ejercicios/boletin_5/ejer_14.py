#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea un programa en el que se ingresen las notas de los alumnos.
    Ve guardando todas estas notas en una lista. Cuando el usuario
    introduzca la palabra 'fin', no se pedirán más notas. Al finalizar
    el ingreso de notas, muestra por pantalla la media de todas las notas.
'''

__author__ = "Martín Gil Blanco"

def calcular_media(lista_numeros):
    if len(lista_numeros) == 0:
        return 0

    suma = 0
    # Calcula la suma de todos los números
    for numero in lista_numeros:
        suma = suma + numero

    # Calculamos la media
    tam_lista = len(lista_numeros)
    media = float(suma) / float(tam_lista)
    return media

notas = []
# Comenzamos a recorrer los datos
while True:

    mensaje = input("Introduce una nota o la palabra fin para finalizar: ")

    # Cuando se escriba la plabra fin salimos ded bucle
    if mensaje == "fin":
        break
    
    # Convertimos a nota en texto a numérica
    try:
        nota = float(mensaje)
    except:
        print("Por favor introduza un numero decimal.")
        continue
    
    # Comprobamos se a nota é correcta
    if nota < 0 or nota > 10:
        print("A nota deberia estar entre 0 e 10")
        continue

    # Gardamos la nota en la lista
    notas.append(nota)

# Calculamos la media de notas
media = calcular_media(notas)
print("La media de las notas es:", media)
