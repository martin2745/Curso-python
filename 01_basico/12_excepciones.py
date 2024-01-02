#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Manejo de exepciones 

numero_uno = 5
numero_dos = 1
numero_dos = "1"

# Excepción base: try except

try:
    print(numero_uno + numero_dos)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally

try:
    print(numero_uno + numero_dos)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(numero_uno + numero_dos)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numero_uno + numero_dos)
    print("No se ha producido un error")
except ValueError as error:
    print("Error de tipo ValueError:", error)
except Exception as my_random_error_name:
    print("Error de tipo TypeError:", my_random_error_name)