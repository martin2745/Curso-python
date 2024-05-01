---
title: "4.7. *args e **kwargs"
weight: 7
---

Se desexamos utilizar un número variable de argumentos, podemos utilizar como parámetro a expresión `*args`:

```python
def funcion1 (*args):
    pass
```

Os argumentos que se lle pasen a función almacénanse nunha tupla. Esta pódese recorrer de varias xeitos como veremos máis adiante. Neste exemplo súmanse tódolos argumentos que se lle pasen a función.

```python
def sumar (*args):
    suma = 0
    for elemento in args:
        suma = suma + elemento
```

Podemos entón chamar a función co número de parámetros que desexemos:


```python
a = sumar()
b = sumar(1, 2)
c = sumar(1,2,3,6)
print(a) # Imprime: 0
print(b) # Imprime: 3
print(c) # Imprime: 12
```

En cambio `**kargs` fai referencia aos argumentos definidos mediante palabras clave. Isto permítenos que na utilización da función se nos poidan pasar argumentos mediante palabras clave que non están definidas na función:


```python
def exemplo():
    pass

exemplo(nome="Manuel", apelidos="Varela")
```

Cada un dos parámetros é un conxunto de paras chave-valor na que a chave é o nome do parámetro e o valor o valor que se lle asigna o parámetro na chamada da función. Para acceder os parámetros podemos facelo do seguinte xeito:

```python
def exemplo(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, " : ", valor)

exemplo(nome="Manuel", apelidos="Varela")
# Imprime:
# nome : Manuel
# apelidos : Varela
```

Se queremos utilizar unha mestura deste tipo de argumentos deberemos definilos na función nunha certa orde:

- Parámetros estándar

- `*args`

- `*kwargs`

```python
def funcion(x, y, *args, **kwargs):
    pass
``````
