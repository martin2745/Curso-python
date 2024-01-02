#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Listas

'''
Lista (List):

    Definición: Una lista es una colección ordenada
    y modificable de elementos. Puedes almacenar
    elementos de diferentes tipos en una lista, y
    esta se define utilizando corchetes [].

    Ejemplo: mi_lista = [1, 2, 3, "cuatro"]
'''

mi_lista = list()
mi_otra_lista = []
mi_lista = [23,24,62,52,30,30,17]

print(type(mi_lista))
print(mi_lista)
print(len(mi_lista))

mi_otra_lista = [23, 1.77,  "Martin", "Gil"]
print(type(mi_otra_lista))

print(mi_otra_lista[0]) # 23
print(mi_otra_lista[1]) # 1.77
print(mi_otra_lista[-1]) # Gil
print(mi_otra_lista[-3]) # 1.77
print(len(mi_otra_lista)) # 4
print(mi_lista.count(30)) # 2 Retorna el número de ocurrencias de un valor del mismo tipo

uno, dos, tres, cuatro = mi_otra_lista
print(uno) # 23
print(dos) # 1.77
print(tres) # Martin
print(cuatro) # Gil

print(mi_lista + mi_otra_lista)

print([0] * 4) # [0, 0, 0, 0]
print([1, 2, 3] * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

mi_otra_lista.append("otro") # Inserto elemento al final
print(mi_otra_lista)

mi_otra_lista.insert(1, 'nuevo') # Inserto en una posición concreta
print(mi_otra_lista)

mi_otra_lista.insert(2, 'nuevo') # Inserto en una posición concreta
print(mi_otra_lista)

mi_otra_lista.remove('nuevo') # Elimino la primera ocurrencia detectada
print(mi_otra_lista)

print(mi_otra_lista.pop()) # Consigo el último elemento que elimino de la lista
print(mi_otra_lista)

print(mi_otra_lista.pop(1)) # Decido que elemento extraer
print(mi_otra_lista)

del mi_otra_lista[2] # Elimino por índice sin extraer el elemento
print(mi_otra_lista)

del mi_otra_lista[1:3] # Elimino desde la posición 1 a la 3 sin incluir
print(mi_otra_lista)

mi_otra_lista.clear() # Elimina el cotenido de la lista
print(mi_otra_lista)

mi_lista.reverse() # Le da la vuelta a los elementos de la lista
print(mi_lista)

mi_lista.sort() # Ordena los elementos de la lista
print(mi_lista)

t1 = ['a', 'b', 'c']
t2 = ['c' ,'d', 'e']
t1.extend(t2) # Concatena t2 en t1
print(t1)

'''
IMPORTANTE

Si no utilizas .copy() y simplemente asignas una lista a
otra como en lista_tres = lista_dos, ambas variables 
(lista_dos y lista_tres) estarán haciendo referencia a la
misma lista en la memoria. Esto significa que cualquier
cambio que hagas en una de las listas se reflejará en la
otra, ya que ambas apuntan a la misma ubicación de memoria.

Por otro lado, si utilizas lista_tres = lista_dos.copy(),
estás creando una copia independiente de la lista, por lo
que después de ejecutar lista_dos.clear(), la lista original
se vaciará, pero la copia lista_tres seguirá conteniendo los
elementos originales sin cambios.
'''

print("\n------------Referencias a memoria------------")
lista_dos = [1,2,3]
lista_tres = lista_dos
lista_dos.clear()
print(lista_tres)
print("Referencia en memoria de lista_dos:  ", id(lista_dos))
print("Referencia en memoria de lista_tres: ", id(lista_tres))

lista_dos = [1,2,3]
lista_tres = lista_dos.copy()
lista_dos.clear()
print(lista_tres)
print("Referencia en memoria de lista_dos:  ", id(lista_dos))
print("Referencia en memoria de lista_tres: ", id(lista_tres))


print("\n-------------Sublistas o Slicing-------------")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Obtener los elementos desde el índice 2 hasta el índice 5 (excluido)
resultado = lista[2:5]
print(resultado)  # Resultado: [3, 4, 5]

# Obtener los primeros 3 elementos
resultado = lista[:3]
print(resultado)  # Resultado: [1, 2, 3]

# Obtener los elementos desde el índice 5 hasta el final
resultado = lista[5:]
print(resultado)  # Resultado: [6, 7, 8, 9]

# Obtener la lista invertida
lista_invertida = lista[::-1]
print(lista_invertida)

# Obtener una copia completa de la lista almacenada en una nueva posición de memoria
copia = lista[:]
print(copia)  # Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Referencia en memoria de lista: ", id(lista_dos))
print("Referencia en memoria de copia: ", id(lista_tres))