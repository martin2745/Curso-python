#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Manejo de exepciones 

numero_uno = 5
numero_dos = "1"

# Excepción base: try except

try:
    print(numero_uno + numero_dos)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("---------Primer Try/Except---------")
    print("Se ha producido un error\n")

# Flujo completo de una excepción: try except else finally

try:
    print(numero_uno + numero_dos)
    print("No se ha producido un error")
except:
    print("---------Segundo Try/Except---------")
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa\n")

# Excepciones por tipo

try:
    print(numero_uno + numero_dos)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("---------Tercer Try/Except---------")
    print("Se ha producido un TypeError al intentar sumar un int y un str\n")
except:
    print("Se ha producido un error\n")

# Captura de la información de la excepción
numero_dos = "abc"

try:
    print(numero_uno + int(numero_dos))
    print("No se ha producido un error")
except ValueError as error:
    print("---------Cuarto Try/Except---------")
    print("Error de tipo ValueError al intentar hacer un casteo a entero de un str que no corresponde a un número:")
    print(error, "\n")
except Exception as my_random_error_name:
    print("Error de tipo TypeError:", my_random_error_name, "\n")
except:
    print("Se ha producido un error\n")

# Lanzamiento de excepciones en python
    
def verificar_numero_positivo(numero):
    if numero <= 0:
        raise ValueError("El número debe ser positivo")
    else:
        print("Número válido:", numero)

try:
    input_numero = int(input("Introduce un número positivo: "))
    verificar_numero_positivo(input_numero)
except ValueError as ve:
    # Capturar la excepción y mostrar un mensaje de error personalizado
    print(f"Error: {ve}")
except Exception as e:
    print("Se ha producido un error\n")