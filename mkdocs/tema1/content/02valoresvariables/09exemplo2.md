---
title: "2.9. Exemplo: Conversión de unidades"
weight: 9
---

Escribe un programa que lle pida ao usuario unha temperatura en graos Celsius, a converta a graos Fahrenheit e imprima por pantalla a temperatura convertida.

## 2.9.1. Solución 1

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe un programa que lle pida ao usuario unha temperatura en graos Celsius, a converta a graos Fahrenheit e imprima por pantalla a temperatura convertida.


__author__ = "Manuel Ramón Varela López"

#Pedimoslle ao usuario a temperatura en graos celsius
celsius = input("Indica a temperatura en graos Celsios: ")

#Formula -> Farenheit = (Celsius * 1.8) + 32

#Preimeiro calculamos a parte da parentese, ademais temos que transformar a varaible celsius a decimal
aux1 = float(celsius) * 1.8

#Agora calculamos o resultado do parentese mais 32
farenheit = aux1 + 32

#Construimos a mensaxe para mostrarlle ao usuario, ademais transformamos o valor da temperatura a texto
mensaxe = "A temperatura en graos Farenheit e " + str(farenheit)

#Mostramos a mensaxe ao usuario
print(mensaxe)
```

## 2.9.2. Solución 2

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe un programa que lle pida ao usuario unha temperatura en graos Celsius, a converta a graos Fahrenheit e imprima por pantalla a temperatura convertida.


__author__ = "Manuel Ramón Varela López"

#Pedimoslle ao usuario a temperatura en graos celsius
celsius = input("Indica a temperatura en graos Celsios: ")

#Formula -> Farenheit = (Celsius * 1.8) + 32

#Facemos o calculo  nunha unica expresion utilizando parenteses 
farenheit = (float(celsius) * 1.8) + 32

#Mostramos a mensaxe ao usuario, neste caso xa non gardamos nunha variable o que queremos aprender
print("A temperatura en graos Farenheit e " + str(farenheit))
```