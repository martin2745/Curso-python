#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Encapsulación

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre                   # Atributo público
        self._edad = edad                      # Atributo privado
        self.__direccion = "Desconocida"       # Atributo muy privado

    # Métodos para acceder y modificar atributos privados
    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, nueva_direccion):
        self.__direccion = nueva_direccion

# Crear una instancia de la clase Persona
persona = Persona("Juan", 30)

# Acceder a atributos públicos
print("Nombre:", persona.nombre)

# Acceder y modificar atributos privados
print("Edad:", persona.get_edad())
persona.set_edad(35)
print("Nueva Edad:", persona.get_edad())

print("Dirección:", persona.get_direccion())
persona.set_direccion("Calle Principal")
print("Nueva Dirección:", persona.get_direccion())

# Podemos tener problemas con casos como los siguientes donde accedemos sin pasar por el getter/setter
print("Edad:", persona._edad)
persona._edad = 100
print("Edad:", persona._edad)
# No permite modificar ni acceder a elementos muy privados como __direccion