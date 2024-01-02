#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Operadores con números

print(10 + 4) # 14
print(10 - 4) # 6
print(10 * 4) # 40
print(10 / 4) # 2.5
print(10 % 4) # 2
print(10 // 4) # 2
print(10 ** 4) # 10000

# Operadores con cadenas
print("Hola " + "Mundo!!!") # Hola Mundo!!!
print("Número: " + str(5)) # Número 5
print("Hola " * 2) # Hola Hola --> Solo puede ser un número entero

# Operadores comparativos
print(3 > 4) # False
print(3 < 4) # True
print(3 <= 4) # True
print(3 <= 4) # True
print(3 == 4) # False
print(3 != 4) # True
print(3 == "3") # False Diferente tipo de datos

print(3 < 4 and 3 != 4) # True
print(3 < 4 or 3 != 4) # True
print(not(3 < 4 and 3 != 4)) # False

print("Hola" > "hola") # False Ordenación alfabética por ASCII
print("Hola" > "Chao") # True Ordenación alfabética por ASCII
print(len("Hola") > len("Chao")) # False Ordenación por tamaño
