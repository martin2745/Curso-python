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

'''
Aunque podemos indicar el tipo de las variables no vamos a asegurar
con ello que una variable sea de un determinado tipo a lo largo del
código. Dicho de otro modo, podemos modificar el valor de la variable
nombre = 22 y el resultado será: Nombre: 22 Tipo: <class 'int'>
'''

# Indicamos tipo en código
nombre: str = "Juan"
edad: int = 25
altura: float = 1.75
es_estudiante: bool = True

# Imprimimos los valores y tipos
print("Nombre:", nombre, "Tipo:", type(nombre))
print("Edad:", edad, "Tipo:", type(edad))
print("Altura:", altura, "Tipo:", type(altura))
print("¿Es estudiante?", es_estudiante, "Tipo:", type(es_estudiante))