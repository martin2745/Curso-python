---
title: "4.13. Exemplo: Calculo de cualificación con funcións"
weight: 13
---

Adapta o programa de cálculo de cualificacións utilizando unha función chamada `calcula_calificacion`, que reciba a puntuación como parámetro e devolva unha cualificación como cadea.

## 4.13.1. Solución 1

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Adapta o programa de cálculo de cualificacións utilizando unha función chamada `calcula_calificacion`, que reciba a puntuación como parámetro e devolva unha cualificación como cadea.

__author__ = "Manuel Ramón Varela López"

#Funcion que devolve a nota en texto a partir da nota numerica
# Parametro nota: valor numerico da nota
# Retorna: cadea de texto ca nota en texto, None se a nota de entrada non e valida
def calcula_calificacion (nota):
	#Segundo a nota devolvemos a calificacion en texto
	if nota > 10 or nota < 0:
		return None
	elif nota >= 9:
		return "Sobresaliente"
	elif nota >= 7:
		return "Notable"
	elif nota >= 6:
		return "Ben"
	elif nota >= 5:
		return "Suficiente"
	else:
		return "Insuficiente"


#Pedimoslle ao usuario a nota do alumno
nota_str = input("Cal e a nota do alumno? ")

try:
	#Intentamos pasar as horas a un float
	nota_numero = float(nota_str)
except:
	#Mostramos unha mensaxe de erro
	print("Por favor, introduce un numero.")

	#Saimos do programa
	exit()

#Imprimimos a nota correspondente segundo a nota
nota_texto = calcula_calificacion(nota_numero)
print(nota_texto)
```

## 4.13.2. Solución 2: engadindo lanzamento de excepcións na función

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Adapta o programa de cálculo de cualificacións utilizando unha función chamada `calcula_calificacion`, que reciba a puntuación como parámetro e devolva unha cualificación como cadea.

__author__ = "Manuel Ramón Varela López"

#Funcion que devolve a nota en texto a partir da nota numerica
# Parametro nota: valor numerico da nota
# Excepcions: lánzase "ValueError" se a nota non está entre 0 e 10.
# Retorna: cadea de texto ca nota en texto, None se a nota de entrada non e valida
def calcula_calificacion (nota):
	#Segundo a nota devolvemos a calificacion en texto
	if nota > 10 or nota < 0:
		raise ValueError
	elif nota >= 9:
		return "Sobresaliente"
	elif nota >= 7:
		return "Notable"
	elif nota >= 6:
		return "Ben"
	elif nota >= 5:
		return "Suficiente"
	else:
		return "Insuficiente"


#Pedimoslle ao usuario a nota do alumno
nota_str = input("Cal e a nota do alumno? ")

try:
	#Intentamos pasar as horas a un float
	nota_numero = float(nota_str)
except:
	#Mostramos unha mensaxe de erro
	print("Por favor, introduce un numero.")

	#Saimos do programa
	exit()

#Imprimimos a nota correspondente segundo a nota
try:
	nota_texto = calcula_calificacion(nota_numero)
	print(nota_texto)
except ValueError:
	print("A nota introducida non é valida")
```