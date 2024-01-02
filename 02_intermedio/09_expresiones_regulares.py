#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Expresiones regulares

'''
Coincidencias Basicas
.       - Cualquier Caracter, excepto nueva linea
\d      - Cualquier Digitos (0-9)
\D      - No es un Digito (0-9)
\w      - Caracter de Palabra (a-z, A-Z, 0-9, _)
\W      - No es un Caracter de Palabra.
\s      - Espacios de cualquier tipo. (espacio, tab, nueva linea)
\S      - No es un Espacio, Tab o nueva linea.

Limites
\b      - Limite de Palabra
\B      - No es un Limite de Palabra
^       - Inicio de una cadena de texto
$       - Final de una cadena de texto

Cuantificadores:
*       - 0 o Más
+       - 1 o Más
?       - 0 o Uno
{3}     - Numero Exacto
{3,4}   - Rango de Numeros (Minimo, Maximo)

Conjuntos de Caracteres
[]      - Caracteres dentro de los brackets
[^ ]    - Caracteres que NO ESTAN dentro de los brackets

Grupos
( )     - Grupo
|       - Uno u otros
'''

import re

mi_cadena = "Cadena de texto para evaluar expresiones regulares"

# Ejemplo 1: Coincidencia al principio de la cadena
print("Ejemplo 1:")
print(re.match("Cadena", mi_cadena))  # Coincide, devuelve un objeto de coincidencia
print(re.match("expresiones", mi_cadena))  # No coincide, devuelve None
print("--------------------------------")

# Ejemplo 2: Búsqueda de patrón en toda la cadena
print("Ejemplo 2:")
print(re.search("texto", mi_cadena))  # Coincide, devuelve un objeto de coincidencia
print(re.search("patron", mi_cadena))  # No coincide, devuelve None
print("--------------------------------")

# Ejemplo 3: Búsqueda y extracción de coincidencias
print("Ejemplo 3:")
coincidencias = re.findall(r"\b\w{5}\b", mi_cadena)  # Coincide con palabras de exactamente 5 letras
print(coincidencias)
print("--------------------------------")

# Ejemplo 4: Sustitución de texto
print("Ejemplo 4:")
nueva_cadena = re.sub(r"expresiones", "regex", mi_cadena)  # Sustituye "expresiones" por "regex"
print(nueva_cadena)
print("--------------------------------")

# Ejemplo 5: División de cadena por un patrón
print("Ejemplo 5:")
segmentos = re.split(r"\s", mi_cadena)  # Divide la cadena por espacios en blanco
print(segmentos)
print("--------------------------------")

# Ejemplo 6: Uso de grupos en expresiones regulares
print("Ejemplo 6:")
resultado = re.match(r"(\w+) de (\w+)", mi_cadena)  # Coincide con palabras separadas por "de"
if resultado:
    print("Grupo completo:", resultado.group(0))
    print("Primer grupo:", resultado.group(1))
    print("Segundo grupo:", resultado.group(2))
else:
    print("No hubo coincidencia.")
print("--------------------------------")

# Ejemplo 7: Uso de caracteres especiales
print("Ejemplo 7:")
cadena_especial = "Una cadena con * y + caracteres especiales."
print(re.findall(r"\*\s\w+|\+\s\w+", cadena_especial))  # Coincide con palabras precedidas por * o +
print("--------------------------------")

# Ejemplo 8: Comprobación de correo electrónico
def es_correo_electronico(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
    if re.match(pattern, email):
        return True
    else:
        return False

# Correo electrónico válido
email1 = "mgb@gmail.com"
if es_correo_electronico(email1):
    print(f"{email1} es una dirección de correo electrónico válida.")
else:
    print(f"{email1} no es una dirección de correo electrónico válida.")

# Correo electrónico no válido
email2 = "mgbgmail.com"
if es_correo_electronico(email2):
    print(f"{email2} es una dirección de correo electrónico válida.")
else:
    print(f"{email2} no es una dirección de correo electrónico válida.")