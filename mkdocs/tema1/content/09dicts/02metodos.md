---
title: "9.2. Operadores e métodos de dicionarios"
weight: 2
---

## 9.2.1. Operadores para dicionarios

A función `len` funciona nos dicionarios, esta regresa o número de pares chave-valor:

```python
len(eng2sp) # 3
```

O operador `in` funciona en dicionarios, este diche se algo aparece como unha **chave** no dicionario (aparecer como valor non é suficiente).

```python
'one' in eng2sp # True
'uno' in eng2sp # False
```

Para eliminar unha chave, utilizase o comando `del` ao igual que nas listas.

A función `len()` aplicada a un dicionario devolve a cantidade de pares chave-valor que contén.

```python
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(len(dicionario))  # Saida: 3
```

## 9.2.2. Métodos dun dicionario

Para ver se algo aparece como valor nun dicionario, podes usar o método `values()`, o cal retorna os valores como unha lista:

```python
vals = list(eng2sp.values())
```

Tamén se poden obter as claves o método `keys()`:

```python
claves = list(eng2sp.keys())
```

O método `update()` actualiza un dicionario con elementos doutro dicionario. Este método modifica o dicionario orixinal engadindo elementos do dicionario pasado como argumento. Se a clave xa existe, o valor sobrescríbese.

```python
diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'b': 3, 'c': 4}

dicionario1.update(dicionario2)

print(dicionario1)  # Saida: {'a': 1, 'b': 3, 'c': 4}
```

O método `pop()` elimina un elemento do dicionario especificando a súa chave. Devolve o valor de dita chave.

```python
dicionario = {'a': 1, 'b': 2, 'c': 3}
valor_eliminado = mi_diccionario.pop('b')
print("Valor eliminado:", valor_eliminado)  # Saida: 2
print("Dicionario actualizado:", mi_diccionario)  # Salda: {'a': 1, 'c': 3}
```