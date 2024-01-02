#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Escribe un programa que solicite al usuario el nombre de
    usuario y la contraseña. Indica si el inicio de sesión es 
    correcto. El nombre de usuario sería "python" y la contraseña "pip".
    Crea la función "comprobar_login" para realizar esta operación.
'''

__author__ = "Martín Gil Blanco"

def comprobar_login(usuario, contrasenha):
    if (usuario == "python" and contrasenha == "pip"):
        return True
    else:
        return False

usuario = input("Introduzca usuario:")
contrasenha = input("Introduzca contraseña:")

if comprobar_login(usuario,contrasenha):
    print("Login correcto")
else:
    print("Login incorrecto")