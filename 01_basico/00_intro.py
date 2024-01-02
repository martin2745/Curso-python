# Intro

#!/usr/bin/env python    --> Script escrito en python
# -*- coding: utf-8 -*-  --> Codificación del script

__author__ = "Martín Gil Blanco"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Rob Knight", "Peter Maxwell", "Gavin Huttley",
                    "Matthew Wakefield"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Rob Knight"
__email__ = "rob@spot.colorado.edu"
__status__ = "Production"

'''
Tipo de datos en python

Tipo/clase 	Categoría 	Notas 	Ejemplo
int 	Números 	Número entero de precisión fija 	42
long 	Números 	Número entero en caso de overflow 	42L o 456966786151987643L
float 	Números 	Número en coma flotante 	        3.1415927
bool 	Booleano 	Solo existen los dos valores lógicos 	True y False
str 	Cadena 	    Cadena de caracteres 	            “Hola mundo”

Existe un tipo de datos que representa la ausencia de un valor o la falta de un 
valor dado: None. Se utiliza mucho para indicar que una variable o una expresión
no tiene un valor definido.

Puede ser útil cuando se desea inicializar una variable antes de asignarle un
valor específico.

python

variable_sin_valor = None

'''

#Esto es un comentario
#Nuestro Hola mundo en python

"""
Comentario de 
varias lineas
"""

#Hola mundo!!!
print('Hola mundo!!!')

#Tipos de datos
print(type("Hola mundo!!!")) # str
print(type(2)) # int
print(type(2.5)) # float
print(type(1 + 3j)) # complex
print(type(True)) # bool