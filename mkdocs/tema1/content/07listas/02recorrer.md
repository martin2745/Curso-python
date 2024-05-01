---
title: "7.2. Recorrer listas"
weight: 2
---

O xeito máis común de recorrer os elementos dunha lista é cun bucle `for`. A sintaxe é a mesma que para cadeas:

```python
for queixo in queixos:
	print(queixo)
```

Isto funciona ben se soamente necesitar ler os elementos da lista. Pero se queres escribir ou actualizar os elementos, necesitas os índices. Unha forma común de facer isto é combinando as funcións `range` e `len`.

```python
for i in range(len(numeros)):
	numeros[i] = numeros[i] * 2
```

Este bucle recorre a lista e actualiza cada elemento. `len` regresa o número de elementos dunha lista. `range` regresa unha lista de índices dende 0 ata n-1, onde n é a lonxitude da lista. Cada vez que pasa a través do recorrido, i obtén o índice do seguinte elemento. A sentencia de asignación dentro do bucle utiliza **i** para ler o valor orixinal do elemento e asignar un novo valor.

Un bucle **for** a través dunha lista baleira nunca executa o código contido no corpo:

```python
for x in vacia:
	print('Isto nunca sucede.')
```

Inda que unha lista pode conter outra lista, as listas aniñadas seguen contando como un só elemento. O tamaño desta lista é 4:

```python
['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
```

{{% notice style="warning" title="Recorrer tuplas e conxuntos" %}}

A sentenza `for` tamén nos permite recorrer os elementos dunha tupla ou un conxunto.

{{% /notice %}}

## 7.2.2. Break, continue e else

Ao igual que cláusula `while`, podemos utilizar `break` `continue` e `else` dentro dunha iteración creado con `for`.

## 7.2.1. Enumerate

A función `enumerate()` en Python utilízase para iterar sobre unha secuencia e proporciona tanto o índice como o valor do elemento actual. O sintaxe é:

```python
for indice, valor in enumerate(lista):
    # Código que utiliza o índice e el valor
```

Exemplo:

```python
lista = ['a', 'b', 'c', 'd']

for indice, valor in enumerate(lista):
    print(f"Índice: {indice}, Valor: {valor}")
```

El resultado será:

```bash
Índice: 0, Valor: a
Índice: 1, Valor: b
Índice: 2, Valor: c
Índice: 3, Valor: d
```

En cada iteración do bucle, `enumerate()` devolve unha tupla `(índice, valor)` correspondente ao elemento actual da lista. P