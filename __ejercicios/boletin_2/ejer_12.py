#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribe un programa que solicite al usuario el nombre de usuario y la contraseña.
    Indica si el inicio de sesión es correcto.
    El nombre de usuario sería "python" y la contraseña "pip".
'''

__author__ = "Martín Gil Blanco"

username = input("Introduce el nombre de usuario: ")
password = input("Introduce la contraseña: ")

if username == "python" and password == "pip":
    print("Bienvenido!")
else:
    print("Las credenciales introducidas son incorrectas")