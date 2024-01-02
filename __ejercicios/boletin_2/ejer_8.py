#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea un menú para seleccionar la acción que desea realizar el usuario. En este caso,
    tenemos tres opciones:
        Sumar 2 números introducidos por teclado.
        Restar 2 números introducidos por teclado.
        Multiplicar 2 números introducidos por teclado. Realiza la operación que
        seleccione el usuario.
'''

__author__ = "Martín Gil Blanco"

print("Elige una de las opciones:")
print("\t1) Sumar dos número")
print("\t2) Restar dos número")
print("\t3) Multiplicar dos número")
print("\tCualquier otro caracter para salir")
eleccion = input("> ")

# Opcion 1: suma
if eleccion == "1":
    try:
        num1 = int(input("Introduce el primeiro número: "))
        num2 = int(input("Introduce el segundo número: "))
    except:
        print("Se ha producido un error, introduza valores numéricos.")
        exit()

    print("Suma: ",num1 + num2)

# Elección 1: resta
elif eleccion == "2":
    try:
        num1 = int(input("Introduce el primeiro número: "))
        num2 = int(input("Introduce el segundo número: "))
    except:
        print("Se ha producido un error, introduza valores numéricos.")
        exit()

    print("Resta: ", num1 - num2)

# Elección 3: multiplicación
elif eleccion == "3":
    try:
        num1 = int(input("Introduce el primeiro número: "))
        num2 = int(input("Introduce el segundo número: "))
    except:
        print("Se ha producido un error, introduza valores numéricos.")
        exit()

    print("Multiplicacion: ", num1 * num2)

else:
    print("Adios")

