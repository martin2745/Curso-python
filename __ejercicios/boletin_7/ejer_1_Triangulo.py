#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

from ejer_1_FiguraGeometrica import FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2, altura):
        super().__init__(lado1, lado2)
        self.__altura = altura

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        self.__altura = valor

    @property
    def area(self):
        return 0.5 * self.lado1 * self.lado2 * self.__altura
