#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Crea un menú para seleccionar la acción que desea realizar el usuario. En este caso, tenemos tres opciones:
        Sumar 2 números introducidos por teclado.
        Restar 2 números introducidos por teclado.
        Multiplicar 2 números introducidos por teclado. 
        
    Realiza la operación que seleccione el usuario. 
    
    Debes definir 4 funciones:
        La función mostrar_menu que solo muestra el menú.
        suma_numeros
        resta_numeros
        multiplica_numeros
'''

__author__ = "Martín Gil Blanco"

def mostra_menu():
    print("Seleccione una de las seguintes opciones:")
    print("\t1) Sumar 2 números")
    print("\t2) Restar 2 números")
    print("\t3) Multiplicar 2 números")
    print("\tCualquier otro caracter para salir")

def sumar_numeros(a, b):
    return a+b

def restar_numeros(a, b):
    return a-b

def multiplicar_numeros(a, b):
    return a*b

mostra_menu()
opcion = input(">")

try:
    num1 = int(input("Indicame el primer número:"))
    num2 = int(input("Indicame el segundo número:"))
except:
    print("Introduza números, por favor")
    exit()

# Opción 1: sumar
if opcion == '1':
    suma = sumar_numeros(num1, num2)
    print("La suma es:",suma)

# Opción 2: restar
elif opcion == '2':
    restar = restar_numeros(num1, num2)
    print("La resta es:", restar)

# Opción 3: restar
elif opcion == '3':
    mult = multiplicar_numeros(num1, num2)
    print("LA multiplicación es:", mult)