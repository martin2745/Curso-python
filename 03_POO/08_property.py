#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Encapsulación

class Persona:
    
    contador_personas = 0                      # Atributo estático

    def __init__(self, nombre, edad):
        self.nombre = nombre                   # Atributo público
        self._edad = edad                      # Atributo protegido
        self.__direccion = "Desconocida"       # Atributo privado
        Persona.contador_personas += 1

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, nueva_direccion):
        self.__direccion = nueva_direccion

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18
    
# Crear una instancia de la clase Persona
persona = Persona("Alex", 30)
persona = Persona("Martín", 30)

# Acceder a atributos públicos
print("Nombre:", persona.nombre)

# Acceder y modificar atributos protegidos
print("Edad:", persona.edad)
persona.edad = 35
print("Nueva Edad:", persona.edad)

# Acceder y modificar atributos privados
print("Dirección:", persona.direccion)
persona.direccion = "Calle Principal"
print("Nueva Dirección:", persona.direccion)

# Método estático 
# Un método estático en Python es un método que pertenece a una clase en lugar de a una 
# instancia específica de esa clase. Es decir, pertenece a la clase y no al objeto.
if Persona.es_mayor_de_edad(persona.edad):
    print(f"{persona.nombre} es mayor de edad.")
else:
    print(f"{persona.nombre} es menor de edad.")

# Atributo estático 
# Del mismo modo que los métodos, los atributos estáticos son comunes a la clase y no al objeto.
print("Contador de personas:", Persona.contador_personas)  # Salida: 2