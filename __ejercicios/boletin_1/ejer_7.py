#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Pedir al usuario dos frases y juntalas. Mostrar el resultado por pantalla.
'''

__author__ = "Martín Gil Blanco"

frase_1 = input("Dime a primeira frase: ")
frase_2 = input("Dime a segunda frase: ")
frase_completa = frase_1 + " " + frase_2
print(f"El resultado de juntar {frase_1} con {frase_2} es: \n\t", frase_completa)