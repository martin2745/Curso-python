#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

class FiguraGeometrica:
    def __init__(self, lado1, lado2):
        self.__lado1 = lado1
        self.__lado2 = lado2

    @property
    def lado1(self):
        return self.__lado1

    @lado1.setter
    def lado1(self, valor):
        self.__lado1 = valor

    @property
    def lado2(self):
        return self.__lado2

    @lado2.setter
    def lado2(self, valor):
        self.__lado2 = valor

    @property
    def area(self):
        return self.__lado1 * self.__lado2

    def __str__(self):
        return f"FiguraGeometrica: Lado1={self.__lado1}, Lado2={self.__lado2}"

    @staticmethod
    def info():
        print("Esta es una clase base para representar figuras geométricas.")

