#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Pedir al usuario su salario bruto e indicarle su salario neto. 
    Utiliza la siguiente fórmula para el cálculo: 
        salario_neto = salario_bruto - (salario_bruto * IRPF). 
    Solicítale también al usuario el porcentaje de retención del 
    IRPF que desea utilizar. Muestra el resultado por pantalla.
'''

__author__ = "Martín Gil Blanco"

salario_bruto = float(input("Ingrese su salario mensual bruto: "))
irpf = float(input("Ingrese su porcentaje de IRPF: "))
salario_neto = round(salario_bruto - (salario_bruto * irpf/100), 2)
print("El salario neto del trabajador es:", salario_neto)