---
title: "3.9. Exemplo: Xestión de excepcións na entrada de datos"
weight: 9
---


Escribe o programa do apartado anterior realizando captura de excepcións mediante **try** e **except**, de xeito que o programa sexa capaz de xestionar entradas non numéricas con elegancia, mostrando unha mensaxe e saíndo do programa.

## 4.9.1. Solución 1

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe o programa do apartado anterior realizando captura de excepcións mediante **try** e **except**, de xeito que o programa sexa capaz de xestionar entradas non numéricas con elegancia, mostrando unha mensaxe e saíndo do programa.

__author__ = "Manuel Ramón Varela López"

#Pedimoslle ao usuario o numero de horas e gardamolo na variable "horas"
horas = input("Indica o numero de horas? ")

#Pedimoslle ao usario a tarifa por hora e gardamolo na variable "tarifa_hora"
tarifa_hora_texto = input("Introduza a tarifa por hora? ")

try:
	#A variable anterior e unha cadea de texto, necesitamos transformar o valor nun valor enteiro
	horas = int(horas)

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

except:
	#Mostramos a mensaxe de erro
	print("Introduza números enteiros por favor.")
```

## 4.9.2. Solución 2

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe o programa do apartado anterior realizando captura de excepcións mediante **try** e **except**, de xeito que o programa sexa capaz de xestionar entradas non numéricas con elegancia, mostrando unha mensaxe e saíndo do programa.

__author__ = "Manuel Ramón Varela López"
#Pedimoslle ao usuario o numero de horas e gardamolo na variable "horas"
horas = input("Indica o numero de horas? ")

#Pedimoslle ao usario a tarifa por hora e gardamolo na variable "tarifa_hora"
tarifa_hora_texto = input("Introduza a tarifa por hora? ")

try:
	#A variable anterior e unha cadea de texto, necesitamos transformar o valor nun valor enteiro
	horas = int(horas)

	#A variable anterior e unha cadea de texto, necesitamos transformar o valor nun valor decimal
	tarifa_hora= float(tarifa_hora_texto)

except:
	#Mostramos a mensaxe de erro
	print("Introduza números enteiros por favor.")

	#Saimos do programa
	exit()

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