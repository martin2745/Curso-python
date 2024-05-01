---
title: "5.5. Exemplo: lector de números"
weight: 5
---

Escribe un programa que lea repetidamente números ata que o usuario introduza a palabra "fin". Unha vez introducido, mostra por pantalla o total, a cantidade de números e a media deses números. Se o usuario introduce calquera outra cousa que non sexa un número, detecta o erro usando `try` y `except`, mostra unha mensaxe de erro e pasa ao número seguinte.

## 5.5.1. Solución 1

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe un programa que lea repetidamente números ata que o usuario introduza a palabra "fin". Unha vez introducido, mostra por pantalla o total, a cantidade de números e a media deses números. Se o usuario introduce calquera outra cousa que non sexa un número, detecta o erro usando `try` y `except`, mostra unha mensaxe de erro e pasa ao número seguinte.

__author__ = "Manuel Ramón Varela López"

#Inicializamos as variables
numero_variables = 0
suma_total = 0

#Creamos unha bandeira para saber cando sair do bucle
flag = True
while(flag):

	#Lemos os datos do usuario
	palabra = input("Introduce un numero:")

	# Se o usuario introduce fin, poñemos a bandeira a falso para sair do bucle
	if palabra == 'fin':
		flag = False

	#Senon, seguimos procesando o dato que introduciu o usuario
	else:
		#Collemos a excepcion se o introducido non e un numero
		try:
			numero = int(palabra)
			#Imos gardando o numero de variables e a suma total
			numero_variables = numero_variables + 1
			suma_total = suma_total + numero
		#Indicamos que non se introduciu un numero
		except:
			print("Non se introduciu un numero")

#Tras sair do bucle, calculamos a media
media = suma_total / numero_variables

#Mostrase por pantalla a solucion
print("Numeros introducidos:",numero_variables)
print("Suma de numeros:",suma_total)
print("Media:",media)


```

## 5.5.2. Solución 2

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe un programa que lea repetidamente números ata que o usuario introduza a palabra "fin". Unha vez introducido, mostra por pantalla o total, a cantidade de números e a media deses números. Se o usuario introduce calquera outra cousa que non sexa un número, detecta o erro usando `try` y `except`, mostra unha mensaxe de erro e pasa ao número seguinte.

__author__ = "Manuel Ramón Varela López"

#Inicializamos as variables
numero_variables = 0
suma_total = 0

#So saimos do bucle se se executa un break
while(True):

	#Lemos os datos do usuario
	palabra = input("Introduce un numero:")

	# Se o usuario introduce fin, saimos do bucle con break
	if palabra == 'fin':
		break

	#Collemos a excepcion se o introducido non e un numero
	try:
		numero = int(palabra)
		#Imos gardando o numero de variables e a suma total
		numero_variables = numero_variables + 1
		suma_total = suma_total + numero
	#Indicamos que non se introduciu un numero
	except:
		print("Non se introduciu un numero")

#Tras sair do bucle, calculamos a media
media = suma_total / numero_variables

#Mostrase por pantalla a solucion
print("Numeros introducidos:",numero_variables)
print("Suma de numeros:",suma_total)
print("Media:",media)
```