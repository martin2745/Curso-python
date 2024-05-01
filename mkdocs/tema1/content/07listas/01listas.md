---
title: "7.1. Definición de listas"
weight: 1
---

Hai varios xeitos de crear unha nova lista; a máis simple é encerrar os elementos en corchetes.

```python
[10, 20, 30, 40]
['manuel', 'miguel', 'gonzalo']
```

O primeiro exemplo é unha lista de 4 enteiros. A segunda é unha lista de tres cadeas. Os elementos de unha lista non ten que ser do mesmo tipo. A seguinte lista contén unha cadea, un flotante, un enteiro e outra lista:

```python
['spam', 2.0, 5, [10, 20]]
```

Unha lista que non contén elementos é chamada lista baleira. Podes crear unha con corchetes baleiros, `[]`. Como podes observar, podes asignar os valores dunha lista a variables:

```python
queixos = ['Cheddar', 'Edam', 'Gouda']
numeros = [17, 123]
vacia = []
print(queixos, numeros, vacia) # Imprime: ['Cheddar', 'Edam', 'Gouda'] [17, 123] []
```

## 7.1.1. Mutabilidade das listas

A sintaxe para acceder a elementos dunha lista é a mesma que para acceder aos caracteres dunha cadea: **o operador corchete**. A expresión dento dos corchetes especifica o índice. Recordemos que os índices comezan en 0.

```python
print(quesos[0]) # Imprime: Cheddar
```

A diferenza das cadeas, as listas son mutables porque poden cambiar a orde dos elementos dunha lista ou reasignar un elemento nunha lista. Cado o operador corchete aparece no lado esquerdo dunha asignación, este identifica o elemento da lista que será asignado:

```python
numeros = [17, 123]
numeros[1] = 5
print(numeros) # Imprime: [17, 5]
```

O elemento na posición un de números, a cal era 123 agora é 5.

Podes pensar nunha lista como unha relación entre índices e elementos. Esta relación é chamada **mapeo**. Cada índice mapea a un dos elementos.

Os índices nunha lista funcionan do mesmo xeito que os índices dunha cadea.

O operador `in` tamén funciona en listas:

```python
queixos = ['Cheddar', 'Edam', 'Gouda']
'Edam' in queixos # Imprime: True
'Brie' in queixos # Imprime: False
```



