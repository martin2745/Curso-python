---
title: "3.11. Exemplo: Crear menú"
weight: 11
---


Crear un menú con 4 opcións.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crear un menú con 4 opcións.

__author__ = "Manuel Ramón Varela López"

# Creamos o menu
print("Elixe unha das seguintes opcions.")
print("\t1. Opcion A")
print("\t2. Opcion B")
print("\t3. Opcion C")
print("\t4. Opcion D")
print("\tOutro caracter. Sair")

#Obtemos a opcion seleccionado polo usuario
opcion = input(">")

#Levamos a cabo a seleccion elixida polo usuario
if opcion == '1':
    print("Elixiuse a opcion 1")
elif opcion == '2':
    print("Elixiuse a opcion 2")
elif opcion == '3':
    print("Elixiuse a opcion 3")
elif opcion == '4':
    print("Elixiuse a opcion 4")
else:
    print("Saimos do programa...")
	
```