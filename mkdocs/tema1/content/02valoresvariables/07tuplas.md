---
title: "2.7. Tuplas e conxuntos"
weight: 7
---

## 2.7.1. Tuplas

As **tuplas** é un **conxunto de datos ordenado e inmutable de elementos do mesmo tipo ou diferente**. Estas **non poden ser modificadas unha vez declaradas**.

Inicialízanse con parénteses:

```python
tupla = (1, 2, 3)
print(tupla) # Imprime: (1, 2, 3)
```

Tamén poden declararse sen `()`, separando por `,` tódolos elementos.

```python
tupla = 1, 2, 3
print(type(tupla)) # Imprime: <class 'tuple'>
print(tupla)       # Imprime: (1, 2, 3)
```

## 2.7.2. Conxuntos

O tipo `set` é un tipo de datos que permite representar conxuntos. Un **conxunto é unha colección desordenada de elementos do mesmo tipo ou diferente únicos**, é dicir, que non se repiten.

Inicialízanse con corchetes:

```python
conxunto = {1, 3, 2, 9, 3, 1}
print(conxunto) # Imprime: {1, 3, 2, 9, 3, 1}
```

Ao igual que as tuplas, son inmutables.