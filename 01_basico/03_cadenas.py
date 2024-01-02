#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Cadenas

mi_cadena = "Mi cadena"
mi_otra_cadena = "Mi cadena"

print("mi_cadena: " + str(len(mi_cadena)))
print("mi_otra_cadena: " + str(len(mi_otra_cadena)))
print(mi_cadena + " " + mi_otra_cadena)

# Formato de cadenas
print("\tTabulación")
print("\nSalto de linea")
print("\\tNo hace caso a la tabulación \\n ni al salto de linea")

nombre, apellido, edad = "Mateo", "Gil", 33
print("Nombre: " + nombre + ", Apellido: " + apellido + ", Edad: " + str(edad))
print("Nombre: {}, Apellido: {}, Edad: {}".format(nombre, apellido, edad))
print("Nombre: %s, Apellido: %s, Edad: %d" %(nombre, apellido, edad))
print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}") # Inferencia de datos

# Desempaquetado de caracteres
lenguaje = "python"
p, y, t, h, o, n = lenguaje
print(p)
print(y)
print(t)
print(h)
print(o)
print(n)

# Funciones de python para cadenas
print(len(lenguaje)) # 6
print(lenguaje.capitalize()) # Python
print(lenguaje.upper()) # PYTHON
print(lenguaje.count("t")) # 1
print(lenguaje.isnumeric()) # False
print("1".isnumeric()) # True
print(lenguaje.lower()) # python
print(lenguaje.upper().isupper()) # True
print(lenguaje.startswith("py")) # True
print(lenguaje.startswith("Py")) # False
print("Py" == "py") # False ya que se hace su conversión a ASCII

otra_cadena = "Otra cadena en python"
print("El segundo caracter de otra_cadena es:", otra_cadena[1])
# No es posible modificar un elemento concreto de la cadena con: otra_cadena[1] = "T" 
# TypeError: 'str' object does not support item assignment

# También puedo emplear indices negativos siendo -1 el último elemento y así sucesivamente
print(otra_cadena[-1]) # n
print(otra_cadena[-2]) # o

# Otras funciones de python para cadenas

frase = "Hola, esto es un ejemplo"
# split: Divide la cadena usando el espacio como delimitador
palabras = frase.split()
print(palabras)

# split: Divide la cadena usando la , como delimitador
palabras = frase.split(",")
print(palabras)

# strip: Elimina espacios en Gil al principio y al final de la cadena.
cadena = "   Hola, mundo!   "
resultado = cadena.strip()
print(resultado)  # Salida: "Hola, mundo!"

# lstrip: Elimina espacios en Gil al principio de la cadena.
cadena = "   Hola, mundo!   "
resultado = cadena.lstrip()
print(resultado)  # Salida: "Hola, mundo!   "

# rstrip: Elimina espacios en Gil al final de la cadena.
cadena = "   Hola, mundo!   "
resultado = cadena.rstrip()
print(resultado)  # Salida: "   Hola, mundo!"

# find: Encuentra la posición de la primera aparición de una subcadena.
cadena = "Hola, mundo!"
posicion = cadena.find("mundo")
print(posicion)  # Salida: 6

# index: Similar a find, pero genera un error si la subcadena no se encuentra.
cadena = "Hola, mundo!"
posicion = cadena.index("mundo")
print(posicion)  # Salida: 6

# replace: Reemplaza una subcadena por otra.
cadena = "Hola, mundo!"
nueva_cadena = cadena.replace("mundo", "Python")
print(nueva_cadena)  # Salida: "Hola, Python!"