#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    El programa elegirá un número al azar entre 1 y 25 (utilizando la librería random).
    El usuario irá introduciendo números por teclado, y el programa le dará pistas, como
    "el número es mayor" o "el número es menor", hasta que el usuario acierte. Después de
    esto, si los números introducidos por el usuario son menores que 5, se le indicará al
    usuario que ha ganado; de lo contrario, se le indicará que ha perdido.
'''

__author__ = "Martín Gil Blanco"

import random

# Función que pide por consola un número entero entre dos valores
# Devuelve un entero mayor que está entre dos números

def pedir_numero_valido(texto, error, limite_inferior, limite_superior):
    while True:
        try:
            numero = int(input(texto))
            if numero >= limite_inferior and numero <= limite_superior:
                return numero
            print(error)
        except:
            print(error)

# Configuración del juego
numero_mas_bajo = 1
numero_mas_alto = 25
numero_intentos = 5
numero_adivinar = random.randint(numero_mas_bajo, numero_mas_alto)
intentos = 0
# Mensajes para el usuario
mensaxe = "Dame un número entre " + str(numero_mas_bajo) + " y " + str(numero_mas_alto) + " incluidos: "
erro = "Introduce un valor numérico entre " + str(numero_mas_bajo) + " y " + str(numero_mas_alto) + " incluidos: "

while True:

    numero = pedir_numero_valido(mensaxe, erro, numero_mas_bajo, numero_mas_alto)
    intentos = intentos + 1

    if numero == numero_adivinar:
        break
    elif numero > numero_adivinar:
        print("El número a adivinar es más pequeño.")
    else:
        print("El número a adivinar es más grande.")

if intentos > numero_intentos:
    print("GAME OVER")
else:
    print("WIN")