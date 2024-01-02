#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# Conjuntos

'''
Conjunto (Set):

    Definición: Un conjunto es una colección
    no ordenada y sin elementos duplicados.
    Se define utilizando llaves {} o la función set().

    Ejemplo: mi_conjunto = {1, 2, 3, 4, 4} 
    (en este caso, el conjunto resultante será
    {1, 2, 3, 4}, ya que no se permiten duplicados).
'''

mi_conjunto = set()
mi_otro_conjunto = {}
mi_conjunto = {23, 1.77,  "Martin", "Gil"}

# print(mi_conjunto[0]) Da error ya que es un conjunto no ordenado
print(len(mi_conjunto)) # 4

mi_conjunto.add("Adios")
print(mi_conjunto) 
# Podemos ver que el resultado no es una estructura ordenada 
#{1.77, 23, 'Gil', 'Adios', 'Martin'}

mi_conjunto.add("Adios")
print(mi_conjunto) 
# Un conjunto no admite repetidos a diferencia de listas y tuplas

print(1.77 in mi_conjunto) # True

mi_conjunto.remove("Adios")
print(mi_conjunto) # {1.77, 23, 'Gil', 'Martin'}

mi_conjunto.clear()
print(len(mi_conjunto)) # 0

print("\n------------Operaciones de conjuntos------------")

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}

# Unión
union = conjunto1.union(conjunto2)
# Otra forma: union = conjunto1 | conjunto2
print("Unión:", union) # Unión: {1, 2, 3, 4, 5, 6, 7}

# Intersección
interseccion = conjunto1.intersection(conjunto2)
# Otra forma: interseccion = conjunto1 & conjunto2
print("Intersección:", interseccion) # Intersección: {3, 4, 5}

# Diferencia
diferencia = conjunto1.difference(conjunto2)
# Otra forma: diferencia = conjunto1 - conjunto2
print("Diferencia (conjunto1 - conjunto2):", diferencia) 
# Diferencia (conjunto1 - conjunto2): {1, 2}

# Diferencia simétrica
dif_simetrica = conjunto1.symmetric_difference(conjunto2)
# Otra forma: dif_simetrica = conjunto1 ^ conjunto2
print("Diferencia Simétrica:", dif_simetrica)
# Diferencia Simétrica: {1, 2, 6, 7}