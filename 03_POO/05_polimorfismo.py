#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Polimorfismo

class Vehiculo:
    def hacer_sonar(self):
        pass

class Coche(Vehiculo):
    def hacer_sonar(self):
        return "Beep beep!"

class Moto(Vehiculo):
    def hacer_sonar(self):
        return "Broom Broom!"

# Un mismo método puede comportarse de manera diferente 
# según el tipo de objeto que lo esté ejecutando
def hacer_sonar_vehiculo(vehiculo):
    return vehiculo.hacer_sonar()

coche = Coche()
moto = Moto()

print(hacer_sonar_vehiculo(coche))  # Salida: Beep beep!
print(hacer_sonar_vehiculo(moto))   # Salida: Vroom vroom!
