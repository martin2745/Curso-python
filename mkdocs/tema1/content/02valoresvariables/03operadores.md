---
title: "2.3. Operadores e operandos"
weight: 3
---

Os **operadores** son símbolos especiais que representan cálculos, como a suma ou a multiplicación. Os valores aos cales se aplican estes operadores reciben o nome de **operandos**.

Aquí algúns **operadores aritméticos**:

- `+`: realiza sumas.
- `-`: realiza restas.
- `*`: realiza multiplicacións.
- `/`: realiza divisións.
- `**` realiza potencias.

Exemplos de uso de estes operadores:

```python
20+32
hora-1
hora*60
minuto/60
5**2
(5+9)*(15+7)
```

{{% notice style="info" title="Tipos de división en Python" %}}

En **Python 3**, ao contrario que na versión 2, ao dividir dous enteiros na que a súa división non é exacta o resultado é do tipo **float**. En **Python 2**, ao dividir dous enteiros truncábase o resultado a un enteiro.

```python
minuto = 59
minuto/60 # minuto ten o valor 0.98333333333333
```

Se desexamos facela división e se trunque o resultado a un enteiro como na versión 2, utilízase o operador `//`.

```python
minuto = 59
minuto//60 # minuto ten o valor 0
```

{{% /notice %}}


## 2.3.1. Operador módulo

O **operador módulo** traballa con enteiros e obtén o resto da operación consistente en dividir o primeiro operando polo segundo. En Python, o operador módulo utiliza o signo de porcentaxe `%`. A sintaxe é a mesma que se usa para os demais operadores.

```python
cociente = 7 // 3
print(cociente)  # Imprime: 2
resto = 7 % 3 
print(resto)  # Imprime: 1
```

O resultado da división enteira entre 7 e 3 é 2 e o resto é 1.

O operador módulo resulta ser moi útil. Podes comprobar se un número é divisible por outro. Se o módulo entre os dous números é 0 significa que é divisible.

Tamén so pode obter o díxito máis a dereita dun número. Por exemplo, `x % 10` obtén o díxito máis a dereita de x.

## 2.3.2. Operacións con cadeas

O operador `+` funciona con cadeas, pero non realiza unha suma. En lugar de iso, realiza unha concatenación. Iso quere dicir que une ambas cadeas, enlazando o final dunha co principio da outra. Exemplo:

```python
primeiro = 10
segundo = 15
print(primeiro+segundo)  # Imprime: 25
primeiro = '100'
segundo = '150'
print(primeiro + segundo)  # Imprime: 100150
```

O operador `*` tamén traballa con cadeas multiplicando o contido dunha cadea por un enteiro. Exemplo:

```python
primeiro = 'Test '
segundo = 3
print(primeiro * segundo)  # Imprime: Test Test Test
```

## 2.3.3. Operadores de actualización

En Python existen operadores de actualización de valores de variables. Son os seguintes:

- `+=`: suma e asignación
- `-=`: resta e asignación
- `*=`: multiplicación e asignación
- `/=`: división e asignación
- `//=`: división enteira e asignación
- `%=`: módulo e asignación
- `**=`: exponenciación e asignación

Estes operadores realizan unha operación de actualización sobre a variable da parte esquerda:

```python
x += 3
```

Esta operación actualiza o valor da variable `x` sumándolle 3. Esta é equivalente a:

```python
x = x + 3
```

O resto de operadores funcionan do mesmo xeito pero realizando a operación correspondente.
