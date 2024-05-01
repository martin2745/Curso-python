---
title: "3.8. Exemplo: Calculo soldo con horas extra"
weight: 8
---

Escribe un programa no que se introducen as horas traballadas nunha semana por unha persoa e o seu soldo en € por hora. As horas traballadas que superen as 40, considéranse horas extras. Por cada hora extra, o traballador cobrará un 50% máis. 


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe un programa no que se introducen as horas traballadas nunha semana por unha persoa e o seu soldo en € por hora. As horas traballadas que superen as 40, considéranse horas extras. Por cada hora extra, o traballador cobrará un 50% máis. 

__author__ = "Manuel Ramón Varela López"

#Pedimoslle ao usuario o numero de horas e gardamolo na variable "horas"
horas = input("Indica o numero de horas? ")

#A variable anterior e unha cadea de texto, necesitamos transformar o valor nun valor enteiro
horas = int(horas)

#Pedimoslle ao usario a tarifa por hora e gardamolo na variable "tarifa_hora"
tarifa_hora_texto = input("Introduza a tarifa por hora? ")

#A variable anterior e unha cadea de texto, necesitamos transformar o valor nun valor decimal
tarifa_hora= float(tarifa_hora_texto)

#Definimos a variable salario
salario = 0

#Comprobamos se as horas son maiores a 40
if horas > 40:
	
	#Calculamos as horas extra
	horas_extra = horas - 40

	#Calculamos o salario base
	salario_base = 40 * tarifa_hora

	#Calculamos a parte do salario das horas extra
	salario_extra = horas_extra * (tarifa_hora * 1.5)

	#Calculamos o salario total
	salario = salario_base + salario_extra

#Se as horas son iguais ou menores, realizamos o calculo normal
else:

	#Calculamos o salario multiplicando as horas polo salario de cada hora
	salario = horas * tarifa_hora

#Imprimimos o resultado
print("O salario total e de",salario, "€")

```