#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Decorador

def mi_decorador(funcion_original):
    def nueva_funcion():
        print("Antes de llamar a la función original")
        funcion_original()
        print("Después de llamar a la función original")
    return nueva_funcion

@mi_decorador
def saludo():
    print("¡Hola, mundo!")

# Ahora, al llamar a la función 'saludo', en realidad estamos llamando a la función decorada
saludo()

'''
Una función decoradora es una función que toma otra función como argumento y agrega o 
modifica su comportamiento.
'''