#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Variables

'''
Aunque python permite declarar variables de cualquier forma, existe un
estandar para ello y es escribir la variable en minúscula y separar las
palabras por _.
'''

mi_variable_str = "Mi nueva variable"
print(type(mi_variable_str))
print(mi_variable_str)

mi_variable_int = 2
print(type(mi_variable_int))
print(mi_variable_int)

mi_variable_float = 2.5
print(type(mi_variable_float))
print(mi_variable_float)

mi_variable_bool = True
print(type(mi_variable_bool))
print(mi_variable_bool)

#Concatenación de variables en el print
print(mi_variable_int, mi_variable_float)

#Creación  de variables en una linea
nombre, profesion = "Martín", "Profesor"
print("Mi nombre es:", nombre, "\nMi profesión es:", profesion)

#Pedir datos por consola
apellido = input("¿Cuál es tu primer apellido?: ")
print("El apellido es:", apellido)

#Es necesario tener cuidado ya que python es un lenguaje de tipado débil 
apellido = 123
print("Ahora sobreescribo el valor de apellido por un número:", apellido, "siendo de tipo", type(apellido))