#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Programa que solicita al usuario 3 números y le muestra por pantalla la media de los 3 números.
'''

__author__ = "Martín Gil Blanco"

num1 = float(input("Por favor, introduzca el primer número: "))
num2 = float(input("Por favor, introduzca ahora el segundo número: "))
num3 = float(input("Por favor, introduzca ahora el tercer y último número: "))

media = (num1 + num2 + num3) / 3
media_ent = (num1 + num2 + num3) // 3

print("El resultado entero es de",media_ent)
print("Por otro lado, el resultado, incluyendo decimales, es de",media)