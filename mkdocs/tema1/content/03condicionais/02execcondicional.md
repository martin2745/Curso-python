---
title: "3.2. Execución condicional e alternativa"
weight: 2
---

## 3.2.1. Execución condicional

Para poder escribir programas útiles, case sempre vamos a necesitar a capacidade de comprobar condicións e cambiar o comportamento do programa de acordo a elas. As **sentenzas condicionais** proporciónannos esa capacidade. A forma máis sinxela é a sentencia `if`:

```python
if x > 0 :
    print("x e positivo")
```

A expresión booleana despois da sentenza `if` recibe o nome de **condición**. A sentenza `if` finaliza co carácter 2 puntos (:) e a(s) liña(s) que van dentro do bloque `if` van indentadas ( é dicir, tabuladas).

Se a condición lóxica é verdadeira, a sentenza ou sentenzas indentadas serán executadas. Se a condición é falsa, a sentenza ou sentenzas indentada serán omitidas.

![captura3_2_1.png](captura3_2_1.png)

Non hai límite no número de sentenzas que poden aparecer no corpo, pero debe haber polo menos unha. Ocasionalmente, pode resultar útil ter un corpo sen sentenzas (xeralmente como emprazamento reservado para código que non se escribiu de momento). Neste caso, pódese usar a sentenza `pass`, que non fai nada.

```python
if x < 0:
    pass		# necesito xestionar os numeros negativos
```

## 3.2.2. Execución alternativa

A segunda forma da sentenza `if` é a **execución alternativa** na cal existen dúas posibilidades e a condición determina cal delas será executada. A sintaxe é similar a esta:

```python
if x%2 == 0:
    print("x e par")
else :
    print("x e impar")
```

Se ao dividir x por 2 obtemos como resto 0, entón sabemos que x é par, e o programa mostra unha mensaxe a tal efecto. Se esta condición e falsa, execútase o segundo conxunto de sentenzas.

![captura3_2_2.png](captura3_2_2.png)

Dado que a condición debe ser obrigatoriamente verdadeira ou falsa, soamente unha das alternativas será executada.

