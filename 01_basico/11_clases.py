#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Clases

# Definición

class MiPersonaVacia:
    pass  
    # Para poder dejar la clase vacía
    # pass es un marcador de posición que permite que el código sea sintácticamente
    # válido sin realizar ninguna acción real. Se utiliza cuando se desea indicar que
    # ciertas partes del código están incompletas y se espera llenarlas más tarde.

print(MiPersonaVacia)
print(MiPersonaVacia())

# Clase con constructor, funciones y popiedades privadas y públicas

class Persona:
    def __init__(self, nombre, apellido, alias="Sin alias"):
        self.nombre_completo = f"{nombre} {apellido} ({alias})"  # Propiedad pública
        self.__nombre = nombre  # Propiedad privada

    def get_nombre(self):
        return self.__nombre

    def caminar(self):
        print(f"{self.nombre_completo} está caminando")


mi_persona = Persona("Martin", "Gil")
print(mi_persona.nombre_completo)
print(mi_persona.get_nombre())
mi_persona.caminar()

my_other_person = Persona("Martin", "Gil", "Aliax")
print(my_other_person.nombre_completo)
my_other_person.caminar()
my_other_person.nombre_completo = "Martin Fernández Gil"
print(my_other_person.nombre_completo)

# Al ser un lenguaje de tipado débil y dinámico, podemos cambiar el tipo de variable
my_other_person.nombre_completo = 123
print(my_other_person.nombre_completo)
print(mi_persona.get_nombre())
my_other_person.caminar()