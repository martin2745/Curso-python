#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Realiza un programa que calcule el salario de un trabajador.
    El programa recibirá las horas trabajadas al día y los €/hora de ese trabajo.
    A continuación, pregunta al usuario si la tarifa es en bruto o en neto.
    A partir de su respuesta, calcula el salario mensual neto. 
    Los días laborables al mes son 22. Si el usuario indica que el costo de
    la hora es en bruto, indícale al usuario que introduzca el IRPF para 
    poder calcularle el salario neto. Deduce el número necesario de funciones
    e implementa.
'''

__author__ = "Martín Gil Blanco"

def calculo_salario_mensual(horas_jornada, tarifa_jornada):
    return horas_jornada * tarifa_jornada * 22

def calculo_salario_mensual_bruto(horas_jornada, tarifa_jornada,irpf):
    salario_bruto = calculo_salario_mensual(horas_jornada,tarifa_jornada)
    return salario_bruto - (salario_bruto * (irpf/100))

print("Seleccione una opción")
print("\t1) Cálculo sueldo neto")
print("\t2) Cálculo sueldo bruto")

try:
    opcion = int(input(">"))
except:
    print("Selecciona una opción válida.")
    exit()

# Datos netos
if opcion == 1:
    try:
        horas = int(input("Horas trabajadas diarias: "))
        tarifa = float(input("Sueldo por hora: "))
    except:
        print("Introduza valores numericos")
        exit()

    if horas < 0:
        print("As horas tenhen que ser positivas")
        exit()
    elif tarifa < 0:
        print("O prezo por hora ten que ser maior que 0")
        exit()

    salario = calculo_salario_mensual(horas, tarifa)
    print("El salario mensual es", salario)

# Datos en bruto
elif opcion == 2:
    try:
        horas = int(input("Horas trabajadas diarias: "))
        tarifa = float(input("Soldo por hora: "))
        irpf = float(input("IRPF: "))
    except:
        print("Introduzca valores numéricos")
        exit()

    if horas < 0:
        print("Las horas tienen que ser positivas")
        exit()
    elif tarifa < 0:
        print("El precio por hora tiene que ser mayor que 0")
        exit()
    elif irpf < 0:
        print("El IRPF por hora tiene que ser mayor que 0")
        exit()

    salario = calculo_salario_mensual_bruto(horas, tarifa, irpf)
    print("El salario mensual es", salario)

else:
    print("Selecciona una opción válida.")
