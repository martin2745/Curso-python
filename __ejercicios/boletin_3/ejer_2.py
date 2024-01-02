#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Implementar una aplicación que calcule el menor de tres números introducidos 
    por el usuario mediante el teclado.
    Comprueba antes de nada que ningún par de números sea igual.
    Si esto es así, indícalo al usuario y no calcules cuál es el menor de los 3.
    Define dos funciones:
        comprobar_valores_iguales
        calcular_menor_numero.
'''

__author__ = "Martín Gil Blanco"

def comprobar_valores_iguais(a,b,c):
    if a == b or a == c or b == c:
        return True
    return False

def calcular_menor_numero(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    return c

try:
    numero1 = int(input("Ingrese un número por consola: "))
except:
    print("Se ha producido un error, introduza valores numéricos.")
    exit()

try:
    numero2 = int(input("Ingrese un número por consola: "))
except:
    print("Se ha producido un error, introduza valores numéricos.")
    exit()

try:
    numero3 = int(input("Ingrese un número por consola: "))
except:
    print("Se ha producido un error, introduza valores numéricos.")
    exit()

son_iguais = comprobar_valores_iguais(numero1, numero2, numero3)

if son_iguais:
    print("Los números son iguales y no existe un número menor.")
else:
    menor = calcular_menor_numero(numero1, numero2, numero3)
    print("El menor de los números es:", menor)