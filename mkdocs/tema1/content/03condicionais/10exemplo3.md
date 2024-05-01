---
title: "3.10. Exemplo: Cualificación en modo texto"
weight: 10
---


Escribe un programa que solicite a puntuación entre 0 e 10 e indique a cualificación de xeito textual. Por exemplo se tes entre un 9 e un 10 "Sobresaliente". Se o valor indicado está fora do rango indica que hai un erro.

## 4.10.1. Solución 1

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe un programa que solicite a puntuación entre 0 e 10 e indique a cualificación de xeito textual. Por exemplo se tes entre un 9 e un 10 "Sobresaliente". Se o valor indicado está fora do rango indica que hai un erro.

__author__ = "Manuel Ramón Varela López"
#Pedimoslle ao usuario a nota do alumno
nota_str = input("Cal é a nota do alumno? ")

try:
	#Intentamos pasar as horas a un float
	nota = float(nota_str)
except:
	#Mostramos unha mensaxe de erro
	print("Por favor, introduce un número.")

	#Saimos do programa
	exit()

#Imprimimos a nota correspondente segundo a nota
if nota > 10 or nota < 0:
	print("Por favor, introduce un numero entre 0 e 10")
elif nota >= 9 and nota <= 10:
	print("Sobresaliente")
elif nota >= 7 and nota < 9:
	print("Notable")
elif nota >= 6 and nota < 7:
	print("Ben")
elif nota >= 5 and nota < 6:
	print("Suficiente")
elif nota >= 0 and nota < 5:
	print("Insuficiente")
```

## 4.10.2. Solución 2

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe un programa que solicite a puntuación entre 0 e 10 e indique a cualificación de xeito textual. Por exemplo se tes entre un 9 e un 10 "Sobresaliente". Se o valor indicado está fora do rango indica que hai un erro.

__author__ = "Manuel Ramón Varela López"
#Pedimoslle ao usuario a nota do alumno
nota_str = input("Cal é a nota do alumno? ")

try:
	#Intentamos pasar as horas a un float
	nota = float(nota_str)
except:
	#Mostramos unha mensaxe de erro
	print("Por favor, introduce un número.")

	#Saimos do programa
	exit()

#Imprimimos a nota correspondente segundo a nota
if nota > 10 or nota < 0:
	print("Por favor, introduce un numero entre 0 e 10")
elif nota >= 9:
	print("Sobresaliente")
elif nota >= 7:
	print("Notable")
elif nota >= 6:
	print("Ben")
elif nota >= 5:
	print("Suficiente")
else:
	print("Insuficiente")
```