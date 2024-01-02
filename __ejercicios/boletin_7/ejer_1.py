#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea una clase padre llamada FiguraGeometrica con los siguientes atributos privados:
    __lado1 (lado 1 de la figura)
    __lado2 (lado 2 de la figura)
    Implementa los métodos getters y setters para los atributos privados.
    Utiliza el método @property para crear una propiedad llamada area que devuelva el
    área de la figura geométrica (puedes implementar la fórmula según el tipo de figura
    que desees).
    Implementa el método __str__ para la clase FiguraGeometrica que imprima una representación
    legible de la figura.
    Crea una clase hija llamada Triangulo que herede de FiguraGeometrica. Añade un atributo
    adicional privado llamado __altura para representar la altura del triángulo.
    Implementa los métodos get_altura, set_altura como getters y setters para el atributo
    privado __altura.
    Sobrescribe el método area en la clase Triangulo para calcular el área del triángulo
    utilizando la fórmula correspondiente.
    En la clase padre FiguraGeometrica, añade un método estático llamado info que imprima
    información general sobre figuras geométricas.
    En tu programa principal, crea instancias de la clase Triangulo, asigna valores a sus
    atributos y muestra la información sobre el área utilizando el método area.

'''

__author__ = "Martín Gil Blanco"

from ejer_1_FiguraGeometrica import FiguraGeometrica
from ejer_1_Triangulo import Triangulo

FiguraGeometrica.info()

triangulo = Triangulo(lado1=5, lado2=8, altura=4)
print(triangulo)
print(f"Área del triángulo: {triangulo.area}")