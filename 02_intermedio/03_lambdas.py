#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Lambdas funciones anónimas

# Las funciones lambda en Python son funciones anónimas y pequeñas 
# que se pueden definir de forma concisa y en una sola línea. 

# Función lambda para la suma
suma = lambda x, y: x + y

# Función lambda para la resta
resta = lambda x, y: x - y

# Función lambda para la multiplicación
multiplicacion = lambda x, y: x * y

# Función lambda para la división
division = lambda x, y: x / y if y != 0 else "No se puede dividir por cero"

# Lambda con condicional
lambda_func = lambda x: True if x**2 >= 10 else False

# Función con lambda en su interior
def elevar_al_cuadrado(n):
    # Utilizando una función lambda para elevar al cuadrado
    cuadrado = lambda x: x ** 2
    resultado = cuadrado(n)
    return resultado

def suma_tres_valores(c):
    return lambda a, b: a + b + c

# Ejemplos de uso
print("Suma:", suma(5, 3))  # Salida: 8
print("Resta:", resta(7, 2))  # Salida: 5
print("Multiplicación:", multiplicacion(4, 6))  # Salida: 24
print("División:", division(8, 2))  # Salida: 4
print("Imprime", lambda_func(3)) # Imprime False
print("Imprime", lambda_func(4)) # Imprime True
print("Intento de división por cero:", division(6, 0))  # Salida: No se puede dividir por cero
print(f"El cuadrado de 4 es: {elevar_al_cuadrado(4)}") # El cuadrado de 4 es: 16
print("El resultado de sumar (2 + 4 + 5) es:",suma_tres_valores(5)(2, 4)) # El resultado de sumar (2 + 4 + 5) es: 11