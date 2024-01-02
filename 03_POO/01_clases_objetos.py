#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Clases y Objetos

# Clase
class Telefono():
    color_caja = "Blanco" # Atributo estático, será igual para todos los objetos

    def __init__(self, marca, modelo, camara): # Constructor
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estas llamando desde un teléfono:", self.marca)

# Objeto
telefono_uno = Telefono("Samsung", "S23", "48MP")
telefono_dos = Telefono("Apple", "15 Pro", "48MP")
print(telefono_uno) # <__main__.Telefono object at 0x0000018C135A9A30>
print(telefono_dos) # <__main__.Telefono object at 0x0000018C135A9A30>
print(Telefono.color_caja) # Blanco, pertenece a la clase