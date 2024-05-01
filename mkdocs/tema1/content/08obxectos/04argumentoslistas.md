---
title: "8.4. Obxectos como argumentos de funcións"
weight: 4
---

A distinción entre obxectos mutables e inmutables toma importancia cando estes se pasan como argumentos a funcións por exemplo. Cando se pasa un obxecto mutable a unha función e a función modifica este obxecto, eses cambios reflectiranse fora da función. 

Por exemplo, cando pasas unha lista a unha función, a función obtén un apuntador a lista. Se a función modifica un parámetro da lista, o código que chamou a función tamén se verá o cambio. Por exemplo, `remover_primero` elimina o primeiro elemento dunha lista:

```python
def remover_primeiro(t):
	del t[0]
```

Aquí está o exemplo de como se usa:

```python
letras = ['a', 'b', 'c']
remover_primeiro(letras)
print(letras) # Imprime:[ 'b', 'c']
```

O parámetro **t** e a variable **letras** son alias para o mesmo obxecto.

En cambio cando pasas un obxecto inmutable, se a función modifica o valor da variable, este non se reflicte fora:

```python
def cambio_valor(x):
	x = 5

a = 1
cambio_valor(a)
print(a) # Imprime: 1
```

## 8.4. As listas como argumentos de funcións

É importante distinguir entre operacións que modifican listas e operacións que crean novas listas. Por exemplo, o método `append` modifica unha lista, pero o operador `+` crea unha nova lista:

```python
t1 = [1, 2]
t2 = t1.append(3)
print(t1) # Imrpime: [1, 2, 3]
print(t2) # Imprime: None

t3 = t1 + [3]
print(t3) # Imprime: [1, 2, 3]
t2 is t3 False
```

Esta diferenza é importante cando escribes funcións que non están destinadas a modificar listas. Por exemplo, esta función non elimina o primeiro elemento dunha lista:

```python
def mal_eliminar_primero(t):
	t = t[1:] # ¡EQUIVOCADO!
```

O operador `recortar` crea unha nova lista e a asignación fai que **t** apunte a unha lista, pero nada disto ten efecto na lista que foi pasada como argumento.

```python
lista = [1,2,3]
mal_eliminar_primero(lista)
print(lista) # Imprime: [1,2,3]
```

Unha alternativa é escribir unha función que cree e regrese unha nova lista. Por exemplo, **cola** regresa todo excepto o primeiro elemento dunha lista:

```python
def cola(t):
	return t[1:]
```

Esta función deixa a lista orixinal sen modificar. Aquí está como é que se usa:

```python
letras = ['a', 'b', 'c']
resto = cola(letras)
print(resto) # Imprime: ['b', 'c']
```

