---
title: "2.8. Exemplo: Calculo salario bruto"
weight: 8
---

Escribe un programa que que calcule o salario bruto dunha persoa a partir das horas traballadas e o que cobra en € por cada hora. Os datos introdúcense mediante consola.

## 2.8.1. Solución 1

```python

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe un programa que que calcule o salario bruto dunha persoa a partir das horas traballadas e o que cobra en € por cada hora. Os datos introdúcense mediante consola.


__author__ = "Manuel Ramón Varela López"

#Pedimoslle ao usuario o numero de horas e gardamolo na variable "horas"
horas = input("Indica o numero de horas? ")

#A variable anterior e unha cadea de texto, necesitamos transformar o valor nun valor enteiro
horas = int(horas)

#Pedimoslle ao usario a tarifa por hora e gardamolo na variable "tarifa_hora"
tarifa_hora_texto = input("Introduza a tarifa por hora? ")

#A variable anterior e unha cadea de texto, necesitamos transformar o valor nun valor decimal
tarifa_hora= float(tarifa_hora_texto)

#Calculamos o salario multiplicando as horas polo salario de cada hora
salario = horas * tarifa_hora

#A variable salario e un float, necesitamos convertilo nunha cadea de texto para poder concatenalo cunha mensaxe
salario_texto = str(salario)

#Concatenamos o texto que queremos imprimir co salario calculado no apartado anterior
mensaxe = "O salario bruto e " + salario_texto

#Imprimimos a mensaxe indicando o salario
print(mensaxe)

```

## 2.8.2. Solución 2

```python

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe un programa que que calcule o salario bruto dunha persoa a partir das horas traballadas e o que cobra en € por cada hora. Os datos introdúcense mediante consola.

__author__ = "Manuel Ramón Varela López"

#Pedimoslle ao usuario o numero de horas e gardamolo na variable "horas"
horas = input("Indica o numero de horas? ")

#Pedimoslle ao usario a tarifa por hora e gardamolo na variable "tarifa_hora"
tarifa_hora= input("Introduza a tarifa por hora? ")

#Calculamos o salario multiplicando as horas polo salario de cada hora
salario = int(horas) * float(tarifa_hora)

#Concatenamos o texto que queremos imprimir co salario calculado no apartado anterior
mensaxe = "O salario bruto e " + str(salario)

#Imprimimos a mensaxe indicando o salario
print(mensaxe)
```