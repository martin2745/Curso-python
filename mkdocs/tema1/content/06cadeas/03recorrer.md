---
title: "6.3. Recorrer e cortar unha cadea"
weight: 3
---

## 6.3.1. Recorrer unha cadea

Moitos dos cálculos requiren procesar unha cadea carácter por carácter. Frecuentemente comezan dende o inicio, seleccionando cada carácter presente, facendo algo con el, e continuando ata o final. Este patrón de procesamento é chamado **recorrer**. Un xeito de escribir o recorrido é co bucle `while`:

```python
indice = 0
while indice < len(froita):
    letra = froita[indice]
    print(letra)
    indice = indice + 1
```

Este bucle recorre a cadea e imprime cada letra de unha en unha. A condición do bucle é `indice < len(fruta)`, así que cando **indice** é igual ao tamaño da cadea, a condición é falsa, e o código do bucle non se executa. O último carácter é o que ten o índice `len(fruta)-1`, o cal é o último carácter da cadea.

Outra forma de recorrer é co bucle `for`:

```python
for caracter in froita:
	print(caracter)
```

Cada vez que iteramos sobre o bucle, o seguinte carácter na cadea é asignado a variable **caracter**. O ciclo continúa ata que non queden caracteres.

## 6.3.2. Porción dunha cadea (Slicing)

Seleccionar unha porción é similar a seleccionar un carácter:

```python
s = 'Monty Python'
print(s[0:5]) # Imprime: Monty
print(s[6:12]) # Imprime: Python
```

O operador `[n:m]` retorna a parte da cadea dende o "n-ésimo" carácter ata o "m-ésimo" carácter, **incluíndo o primeiro pero excluíndo o último**.

Se omites o primeiro índice (antes dos dous puntos), a porción comeza dende o inicio da cadea. Se omites o segundo índice, a porción vai ata o final da cadea.

```python
froita = 'banana'
froita[:3] # Imprime: 'ban'
froita[3:] # Imprime: 'ana'
```

Se o primeiro índice é maior ou igual que o segundo, o resultado é unha cadea baleira, representado por dúas comiñas:

```python
froita = 'banana'
froita[3:3] # Imprime: ''
```

Unha cadea baleira non contén caracteres e ten un tamaño de 0, pero fora de iso é o mesmo que calquera outra cadea.

Se utilizamos tan só 2 puntos, o que se fará é unha copia completa da cadea:

```python
froita = 'banana'
froita[:] # Imprime: ''
```

## 6.3.3. Slicing terciario

O *slicing* terciario, ou *slicing* estendido é un xeito de engadir un terceiro parámetro coñecido como paso.

A sintaxe é a seguinte:

```python
cadea[inicio:fin:paso]
```

Onde:
- `inicio` é o índice onde comeza o *slicing* (incluído).
- `fin` é o índice onde remata o *slicing* (excluído).
- `paso` é o incremento entre os elementos tomados.

Exemplos:

```python
# Creamos unha lista de exemplo
mi_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Obtenemos oos elementos dende o índice 2 ata o índice 7 cun paso de 2
resultado = mi_lista[2:7:2]
# [2:7] collería a lista [ 2, 3, 4, 5, 6 ]
# O paso 2 significa que collemos de 2 en 2 (ou saltamos 1) comezando no primeiro [2, 4, 6]
print(resultado)  # Saida: [2, 4, 6]

# Obtemos todos os elementos cun paso de 3
# [:] collemos todolos elementos [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Collemos cada 3 elementos (ou saltamos 2) [0, 3, 6, 9]
resultado = mi_lista[::3] 
print(resultado)  # Salida: [0, 3, 6, 9]
```

Podemos utilizar este método para crear unha nova lista invertida do seguinte xeito:

```python
letras = "abcd"
letras_invertidas = letras[::-1]
print(letras_invertidas) # Imprime: "dcba"
```