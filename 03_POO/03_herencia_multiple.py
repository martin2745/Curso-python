
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Herencia múltiple

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo")

    def tipo(self):
        return "Animal"

    def que_soy(self):
        print(f"Soy un Animal")


class Volador:
    def __init__(self, altura_maxima):
        self.altura_maxima = altura_maxima

    def volar(self):
        print(f"Volando a una altura máxima de {self.altura_maxima} metros")

    def tipo(self):
        return "Volador"


class Pajaro(Animal, Volador):
    def __init__(self, nombre, altura_maxima, tipo_pico):
        Animal.__init__(self, nombre)
        Volador.__init__(self, altura_maxima)
        self.tipo_pico = tipo_pico

    def cantar(self):
        print(f"{self.nombre} está cantando")

    def tipo(self):
        return "Pajaro"
    
    def que_soy(self):
        super().que_soy()  # Llama al método de Animal
        print(f"Soy un Pajaro")


# Crear una instancia de la clase Pajaro
pajaro1 = Pajaro(nombre="Loro", altura_maxima=100, tipo_pico="Curvo")

# Acceder a métodos de las clases base
pajaro1.comer()
pajaro1.volar()

# Acceder a métodos de la clase derivada
pajaro1.cantar()

# Acceder a atributos de la clase derivada
print(f"Clase de pico: {pajaro1.tipo_pico}")

# Acceder al método tipo()
print(f"Tipo: {pajaro1.tipo()}")

# Acceder al método nuevo_metodo() de la clase Pajaro
pajaro1.que_soy()