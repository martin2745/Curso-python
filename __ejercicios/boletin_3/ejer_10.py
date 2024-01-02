#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Realiza un programa que calcule el salario de un trabajador.
    El programa recibirá las horas trabajadas al día y los €/hora de ese trabajo.
    A continuación, pregunta al usuario si la tarifa es en bruto o en neto.
    A partir de su respuesta, calcula el salario mensual neto. Los días laborables al mes son 22.
    Si el usuario indica que el costo de la hora es en bruto, indícale 
    al usuario que introduzca el IRPF para poder calcularle el salario neto.
    Deduce el número necesario de funciones e implementa.
'''

__author__ = "Martín Gil Blanco"

def calculo_nota_final(nota_ejer, nota_teo, nota_pra):
    return nota_ejer * 0.15 + nota_teo * 0.20 + nota_pra * 0.65

def comprobar_nota(nota):
    if nota >= 0 and nota <=10:
        return True
    else:
        return False

def nota_numerica_a_texto(nota_numerica):
    if nota_numerica >= 9:
        return "Sobresaliente"
    elif nota_numerica >= 7:
        return "Notable"
    elif nota_numerica >= 6:
        return "Bien"
    elif nota_numerica >= 5:
        return "Suficiente"
    else:
        return "Insuficiente"

try:
    n_ejercicios = float(input("Nota de ejercicios: "))
    n_teoria = float(input("Nota de teoría: "))
    n_practica = float(input("Nota de prácticas: "))
except:
    print("Las notas tienen que ser numéricas")

# Comprobamos se todas as notas son correctas
if comprobar_nota(n_ejercicios) and comprobar_nota(n_teoria) and comprobar_nota(n_practica):
    # Calculamos a nota final e pasamola a texto
    n_final = calculo_nota_final(n_ejercicios,n_teoria,n_practica)
    print("La nota final es:", nota_numerica_a_texto(n_final))
else:
    print("Alguna de las notas no es válida")
