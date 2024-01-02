#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Funciones

# Definición

def mi_funcion():
    print("Esto es una función")

mi_funcion()
mi_funcion()
mi_funcion()

# Función con parámetros de entrada/argumentos
# No podemos forzar el tipo de datos de entrada podemos indicarlo
def suma(primer_valor: int, segundo_valor: int):
    print(primer_valor + segundo_valor)


suma(5, 7) # 12
suma(54754, 71231) # 125985
suma("5", "7") # 57 --> Como str
suma(1.4, 5.2) # 6.6

# Función con parámetros de entrada/argumentos y retorno

def suma_with_return(primer_valor, segundo_valor):
    mi_suma = primer_valor + segundo_valor
    return mi_suma

mi_resultado = suma(1.4, 5.2)
print(mi_resultado) # 6.6

mi_resultado = suma_with_return(10, 5)
print(mi_resultado) # 15

# Función con parámetros de entrada/argumentos por clave

def print_nombre(name, surname):
    print(f"{name} {surname}")

print_nombre(surname="Gil", name="Martin")

# Función con parámetros de entrada/argumentos por defecto

def print_nombre_valor_defecto(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_nombre_valor_defecto("Martin", "Gil")
print_nombre_valor_defecto("Martin", "Gil", "Aliax")

# Si deseamos utilizar un número variable de argumentos podemos
# utilizar algo como lo siguiente

def print_texto_upper_args(*args):
    print(type(args)) # <class 'tuple'>
    for arg in args:
        print(arg.upper())

print_texto_upper_args("Hola", "Python", "Aliax")
print_texto_upper_args("Hola")

# Si deseamos utilizar un número variable de argumentos en formato
# clave valor, podemos utilizar algo como lo siguiente

def ejemplo_kwargs(**kwargs):
    print(type(kwargs)) # <class 'dict'>
    for clave, valor in kwargs.items():
        print(clave, " : ", valor)

ejemplo_kwargs(nombre="Manuel", apellidos="Varela")
# Nombre : Manuel
# Apellidos : Varela