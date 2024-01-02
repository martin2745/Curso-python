#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# MRO - Method Resolution Order

class A:
    def saludar(self):
        print("Hola desde A")

class B(A):
    def saludar(self):
        print("Hola desde B")
        super().saludar()

class C(A):
    def saludar(self):
        print("Hola desde C")
        super().saludar()

class D(B, C):
    def saludar(self):
        print("Hola desde D")
        super().saludar()

# Crear una instancia de la clase D
instancia_d = D()

# Llamar al método saludar de la clase D
instancia_d.saludar()

print(D.mro())

print("-------------------------------------------")

class E:
    def saludar(self):
        print("Hola desde E")

class F(E):
    def saludar(self):
        print("Hola desde F")
        super().saludar()

class H:
    def saludar(self):
        print("Hola desde H")

class I(H):
    def saludar(self):
        print("Hola desde I")
        super().saludar()

class J(I, F):  # Cambiado el orden y eliminado la herencia de H
    def saludar(self):
        print("Hola desde J")
        super().saludar()

# Crear una instancia de la clase J
instancia_j = J()

# Llamar al método saludar de la clase J
instancia_j.saludar()

print(J.mro())


