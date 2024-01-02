#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Realiza un programa que calcule el salario de un trabajador. 
    El programa recibirá las horas trabajadas al día y los €/hora de ese trabajo. 
    A continuación, pregunta al usuario si la tarifa es en bruto o en neto. 
    Los días laborables al mes son 22. Si el usuario indica que el costo de la 
    hora es en bruto, indícale al usuario que introduzca el IRPF para poder 
    calcular el salario neto.
'''

__author__ = "Martín Gil Blanco"

dias_laborales_mes = 22 

print("Elige una de las opciones:")
print("\t1) Cálculo sueldo neto")
print("\t2) Cálculo sueldo bruto")
print("\tCualquier otro caracter para salir")
eleccion = input("> ")

# Opcion 1: sueldo neto
if eleccion == "1":
    try:
        horas_dia = int(input("Introduce las horas trabajadas al día: "))
        tarifa_hora = float(input("Introduce los euros que se pagan por hora: "))
    except:
        print("Introduzca valores numéricos")
        exit()
    salario = horas_dia * tarifa_hora * dias_laborales_mes
    print("El salario a cobrar es de ", salario, "€")

# Opción 2: sueldo bruto
elif eleccion == "2":
    try:
        horas_dia = int(input("Introduce las horas trabajadas al día: "))
        tarifa_hora = float(input("Introduce los euros que se pagan por hora: "))
        irpf = float(input("Introduce el IRPF en %: "))
    except:
        print("Introduzca valores numéricos")
        exit()

    salario_bruto = horas_dia * tarifa_hora * dias_laborales_mes
    irpf = irpf/100
    salario = salario_bruto * (1-irpf)
    print("El salario a cobrar es de ", salario, "€")

else:
    print("Adios")


