#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Herencia

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def tipo(self):
        print("Soy una persona")

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nacionalidad: {self.nacionalidad}"

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, puesto):
        # Llamamos al constructor de la clase base (Persona)
        super().__init__(nombre, edad, nacionalidad)
        self.puesto = puesto

    def tipo(self):
        print("Soy un emleado")

    def __str__(self):
        # Utilizamos super().__str__() para obtener la representación de la clase base
        return super().__str__() + f", Puesto: {self.puesto}"

# Crear instancias de las clases
persona1 = Persona("Alex", 30, "Mexicana")
empleado1 = Empleado("Martín", 25, "Española", "Desarrollador")

# Imprimir información de las instancias
print("Información de la Persona:")
print(persona1)
persona1.tipo()

print("\nInformación del Empleado:")
print(empleado1)
empleado1.tipo()