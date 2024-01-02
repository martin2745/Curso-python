#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    La evaluación de este módulo es la siguiente:
    15% tareas, 20% examen teórico y 65% examen práctico.
    El programa le pedirá al usuario sus tres notas sobre 10
    e indicará por pantalla su nota final sobre 10.
'''

__author__ = "Martín Gil Blanco"

tarea = float(input("Introduzca la nota recibida por las tareas entregadas: "))
teorico = float(input("Introduzca la nota recibida en el examen teórico: "))
practico = float(input("Introduzca la nota recibida en el examen práctico: "))

not_tarea = (tarea * 15) / 100
not_teorico = (teorico * 20) / 100
not_practico = (practico * 65) / 100
nota_final = not_tarea + not_teorico + not_practico

print("La nota final a recibir en este módulo es ",nota_final)