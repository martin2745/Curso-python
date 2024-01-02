#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Programa que solicita al usuario los coeficientes de una ecuación
    de segundo grado y calcula la solución. Comprueba si hay una solución,
    dos o ninguna. Dependiendo del caso, muestra las soluciones que
    correspondan. 
    
    Crea las siguientes funciones:
        Una función que calcule el número de soluciones.
        Otra para calcular la solución cuando es única.
        Cuando haya dos soluciones, crearemos dos funciones distintas: 
        una para la solución del "+" y otra para la del "-".
'''

import math

__author__ = "Martín Gil Blanco"

def pedir_numero_entero(texto):
    while True:
        try:
            return int(input(texto))
        except:
            print("Por favor, introduza un número entero")

def comproba_numero_soluciones(a, b, c):
    if type(a) != int or type(b) != int or type(c) != int:
        raise Exception
    discriminante = (b ** 2) - (4 * a * c)
    solucion = 2
    if discriminante == 0:
        solucion = 1
    elif discriminante < 0:
        solucion = 0
    return solucion

def calcula_una_solucion(a, b):
    if type(a) != int or type(b) != int or type(c) != int:
        raise Exception
    if a == 0:
        raise Exception

    return (b * (-1)) / (2*a)

def calcula_solucion_positiva(a, b, c):
    if type(a) != int or type(b) != int or type(c) != int:
        raise Exception
    if a == 0:
        raise Exception
    
    discriminante = (b ** 2) - (4 * a * c)
    return ((b * (-1)) + math.sqrt(discriminante)) / (2 * a)

def calcula_solucion_negativa(a, b, c):
    if type(a) != int or type(b) != int or type(c) != int:
        raise Exception
    if a == 0:
        raise Exception
    
    discriminante = (b ** 2) - (4 * a * c)
    return ((b * (-1)) - math.sqrt(discriminante)) / (2 * a)

a = 0
while a == 0:
    a = pedir_numero_entero("Coeficiente a: ")
    if a == 0:
        print("A non pode valer 0")
b = pedir_numero_entero("Coeficiente b: ")
c = pedir_numero_entero("Coeficiente c: ")

numero_soluciones = comproba_numero_soluciones(a, b, c)

if numero_soluciones == 0:
    print("La ecuación no tiene solución")

elif numero_soluciones == 1:
    try:
        solucion = calcula_una_solucion(a, b)
        print("La solucion es", solucion)
    except:
        print("El coeficiente a no puede ser 0")

else:
    try:
        solucion1 = calcula_solucion_positiva(a, b, c)
        solucion2 = calcula_solucion_negativa(a, b, c)
        print("Las soluciones son: ", solucion1, "y", solucion2)
    except:
        print("El coeficiente a no puede ser 0")


