#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Funciones de orden superior

def suma_uno(value):
    return value + 1

def suma_cinco(value):
    return value + 5

# Función de orden superior a la que le paso otra función como parámetro
def suma_dos_valores_mas_funcion(a, b, f_suma):
    return f_suma(a + b)

print("La suma es:", suma_dos_valores_mas_funcion(5, 2, suma_uno)) # 8
print("La suma es:", suma_dos_valores_mas_funcion(5, 2, suma_cinco)) # 12

# Map - acción a realizar / conjunto de elementos iterables

numeros = [2, 5, 10, 21, 3, 30]

def miltiplicar_por_dos(numero):
    return numero * 2

print("Lista de valores multiplicados por dos:", list(map(miltiplicar_por_dos, numeros)))
print("Lista de valores multiplicados por dos con lambda:", list(map(lambda numero: numero * 2, numeros)))

# Filter - condición a evaluar / conjunto de elementos iterables

def mayor_que_diez(numero):
    if numero > 10:
        return True
    return False

print("Lista de valores menores que 10:", list(filter(mayor_que_diez, numeros)))
print("Lista de valores menores que 10 con lambda:",list(filter(lambda numero: numero > 10, numeros)))