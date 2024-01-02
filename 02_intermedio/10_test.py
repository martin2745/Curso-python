#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Test de unidad

import unittest
import operaciones

class TestOperaciones(unittest.TestCase):

    def test_sumar_numeros_positivos(self):
        resultado = operaciones.sumar(3, 5)
        self.assertEqual(resultado, 8)

    def test_sumar_numeros_negativos(self):
        resultado = operaciones.sumar(-2, -7)
        self.assertEqual(resultado, -9)

    def test_sumar_numero_positivo_y_negativo(self):
        resultado = operaciones.sumar(10, -3)
        self.assertEqual(resultado, 7)
