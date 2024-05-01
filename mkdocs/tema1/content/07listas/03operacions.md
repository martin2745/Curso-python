---
title: "7.3. Operacións con listas"
weight: 3
---

## 7.3.1. Concatenación de listas

O operador `+` concatena listas:

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) # Imrpime: [1, 2, 3, 4, 5, 6]
```

De igual xeito, o operador `*` repite unha lista un determinado número de veces:

```python
[0] * 4 # [0, 0, 0, 0]
[1, 2, 3] * 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## 7.3.2. Recortar listas

De igual xeito que cas cadeas, pódense recortar cadeas.

## 7.3.3. Engadir novos elementos

O método `append` agrega un novo elemento ao final dunha lista:

```python
t = ['a', 'b', 'c']
t.append('d')
print(t) # Imrpime: ['a', 'b', 'c', 'd']
```

`extend` toma unha lista como argumento e agrega todos os elementos:

```python
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1) # Imrpime: ['a', 'b', 'c', 'd', 'e']
```

Este exemplo deixa **t2** sen modificar.

Tamén podemos usar o método `insert`. O primeiro parámetros consta da posición na que se quere engadir o elemento e o segundo parámetro é o elemento a engadir:

```python
t1 = ['a', 'b', 'c']
t1.insert(1,"d")
print(t1) # Imprime: ['a', 'd', 'b', 'c']
```

## 7.3.4. Ordenar unha lista

`sort` ordena os elementos dunha lista de maior a menor:

```python
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t) # Imrpime: ['a', 'b', 'c', 'd', 'e']
```

## 7.3.5. Eliminar elementos dunha lista

Para eliminar elementos existen varias formas. Se sabes o índice do elemento que queres, podes usar `pop`:

```python
t = ['a', 'b', 'c']
x = t.pop(1)
print(t) # Imprime: ['a', 'c']
print(x) # Imrpime: b
```

`pop` modifica a lista e regresa o elemento que foi removido. Se non proves o índice, a función elimina e retorna o último o elemento.

Se non necesitas o valor removido, podes usar o operador `del`.

```python
t = ['a', 'b', 'c']
del t[1]
print(t) # Imprime: ['a', 'c']
```

Se sabes que elemento queres remover (pero non sabes o índice), podes usar `remove`:

```python
t = ['a', 'b', 'c']
t.remove('b')
print(t) # Imprime: ['a', 'c']
```

Para eliminar máis dun elemento, podes usar `del` xunto o índice:

```python
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t) # Imrpime: ['a', 'f']
```

Tamén podemos eliminar tódolos elementos dunha lista co método `clear`:


```python
t = ['a', 'b', 'c', 'd', 'e', 'f']
t.clear()
print(t) # Imrpime: []
```
