#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Realiza un programa que compruebe si para dos números introducidos por pantalla uno es divisor del otro.
'''

__author__ = "Martín Gil Blanco"

try:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
except:
    print("Se ha producido un error, introduza valores numéricos.")
    exit()

if num1 % num2 == 0 or num2 % num1 == 0:
    print("Unos de los números es divisor del otro")
else:
    print("Nunguno de los números es divisor")

