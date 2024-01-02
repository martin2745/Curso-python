#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Funciones de orden superior

from functools import reduce

def suma_uno(value):
    return value + 1

def suma_cinco(value):
    return value + 5

def suma_dos_valores_mas_funcion(a, b, f_sum):
    return f_sum(a + b)

print(suma_dos_valores_mas_funcion(5, 2, suma_uno)) # 8
print(suma_dos_valores_mas_funcion(5, 2, suma_cinco)) # 12

### Closures ###

def suma_diez(valor_original):
    def suma(valor):
        return valor + 10 + valor_original
    return suma

closure = suma_diez(1)
print(closure(5))
print((suma_diez(5))(1))

### Built-in Higher Order Functions ###

numeros = [2, 5, 10, 21, 3, 30]

# Map - acción a realizar / conjunto de elementos iterables

def miltiplicar_por_dos(numero):
    return numero * 2

print(list(map(miltiplicar_por_dos, numeros)))
print(list(map(lambda numero: numero * 2, numeros)))

# Filter - condición a evaluar / conjunto de elementos iterables

def mayor_que_diez(numero):
    if numero > 10:
        return True
    return False

print(list(filter(mayor_que_diez, numeros)))
print(list(filter(lambda numero: numero > 10, numeros)))