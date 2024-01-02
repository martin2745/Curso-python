#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Tipos de errores que puede generar python

from math import pi
import math

#----------------SyntaxError----------------
#print "Hola Mundo!!!" # Descomentar para Error

#----------------NameError----------------
lenguaje = "Spanish"  # Comentar para Error
print(lenguaje)

#----------------IndexError----------------
mi_lista = ["Python", "PHP", "CSS", "GO", "JavaScript"]
print(mi_lista[0])
print(mi_lista[4])
print(mi_lista[-1])
# print(mi_lista[5]) # Descomentar para Error

#----------------ModuleNotFoundError----------------
# import maths # Descomentar para Error

#----------------AttributeError----------------
# print(math.PI) # Descomentar para Error
print(math.pi)

#----------------KeyError----------------
mi_diccionario = {"Nombre": "Martin", "Apellido": "Gil", "Edad": 25, 1: "Python"}
print(mi_diccionario["Edad"])
# print(mi_diccionario["Dni"]) # Descomentar para Error
print(mi_diccionario["Apellido"])

#----------------TypeError----------------
# print(mi_lista["0"]) # Descomentar para Error
print(mi_lista[0])

#----------------ImportError----------------
# from math import PI # Descomentar para Error
print(pi)

#----------------ValueError----------------
#my_int = int("10 Años")
my_int = int("10")  # Descomentar para Error
print(type(my_int))

#----------------ZeroDivisionError----------------
# print(4/0) # Descomentar para Error
print(4/2)

#----------------Generar excepciones----------------

# Definir una excepción personalizada
class MiExcepcionPersonalizada(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(mensaje)
        
def generar_excepcion():
    raise MiExcepcionPersonalizada("¡Esto es una excepción personalizada!")

# Capturar la excepción en otro punto del código
try:
    generar_excepcion()
except MiExcepcionPersonalizada as ex:
    print(f"Se ha capturado la excepción: {ex.mensaje}")
except Exception as e:
    print(f"Se ha producido una excepción no manejada: {e}")