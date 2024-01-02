#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribir un programa que almacene el abecedario en una lista,
    elimine de la lista las letras que ocupen posiciones múltiplos
    de 3, y muestre por pantalla la lista resultante.
'''

__author__ = "Martín Gil Blanco"

# Almacenar el abecedario en una lista
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Eliminar las letras en posiciones múltiplos de 3
abecedario_filtrado = [letra for i, letra in enumerate(letras) if (i + 1) % 3 != 0]

# Mostrar la lista resultante
print(abecedario_filtrado)