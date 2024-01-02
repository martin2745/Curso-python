#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Programa que pide al usuario los coeficientes de una ecuación de segundo grado
    y calcula la solución. Comprueba si hay una solución, dos o ninguna. Dependiendo 
    del caso, muestra las soluciones que correspondan.
'''

__author__ = "Martín Gil Blanco"

try:
    a = float(input("Introduce el coeficiente a: "))
    b = float(input("Introduce el coeficiente b: "))
    c = float(input("Introduce el coeficiente c: "))
except:
    print("Se ha producido un error, introduza valores numéricos.")
    exit()

# Calculamos el discriminante
discriminante = b**2 - 4 * a * c

# Cuando el discriminante es mayor que 0, la ecuación tiene dos soluciones
if discriminante > 0:
    # Calculamos las soluciones
    solucion_1 = (-b + discriminante**0.5) / (2 * a)
    solucion_2 = (-b - discriminante**0.5) / (2 * a)
    print("Las soluciones son: ", solucion_1, "y", solucion_2)
# Si el discriminante es igual a 0, tenemos una solución
elif discriminante == 0:
    solucion = -b (2*a)
    print("A solución é", solucion)
# Si el discriminante es menor que 0, la ecuación no tiene solución
else:
    print("La ecuación no tiene solución")
