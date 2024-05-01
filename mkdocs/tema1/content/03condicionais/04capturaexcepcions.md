---
title: "3.4. Captura de excepcións"
weight: 4
---


Anteriormente vimos fragmentos de código onde usábamos as funcións `input` e `int` para ler e analizar un número enteiro introducido polo usuario. Aquí un exemplo para converter unha temperatura de graos Fahrenheit a graos Celsius:

```python
ent = input('Introduza a Temperatura Fahrenheit:')
fahr = float(ent)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)
```

Se executamos este código e lle damos unha entrada non válida, simplemente fallará cunha mensaxe de erro:

```bash
$ python fahren.py
Introduzca la Temperatura Fahrenheit:72
22.2222222222

$ python fahren.py
Introduzca la Temperatura Fahrenheit:fred
Traceback (most recent call last):
	File "fahren.py", line 2, in <module>
		fahr = float(ent)
ValueError: invalid literal for float(): fred
```

Existen estruturas de execución condicional dentro de Python para manexa este tipo de erros esperados e inesperados, chamadas **try/except**. A idea de `try` e `except` é que se sabe que certa secuencia de instrucións pode xerar un problema, sexa posible engadir certas sentenzas para que sexan executadas en caso de erro. Estas sentenzas extra (o bloque `except`) serán ignoradas se non se produce ningún erro.

Podemos reescribir o noso conversor de temperatura desta forma:

```python
ent = input('Introduza a Temperatura Fahrenheit:')
try:
	fahr = float(ent)
	cel = (fahr - 32.0) * 5.0 / 9.0
	print(cel)
except:
	print('Por favor, introduza un número')
```

![captura3_4_1.png](captura3_4_1.png)


Python comeza executando a secuencia de sentenzas do bloque `try`. Se todo vai ben, saltarase todo o bloque `except` e rematará. Se acontece unha excepción dentro do bloque `try`, Python saltará fora dese bloque e executarase a secuencia de sentenzas do bloque `except`.

```bash
$ python fahren2.py
Introduzca la Temperatura Fahrenheit:72
22.2222222222

$ python fahren2.py
Introduzca la Temperatura Fahrenheit:fred
Por favor, introduzca un número
```

Xestionar unha excepción cunha sentenza `try` recibe o nome de **capturar unha excepción**. Neste exemplo, a cláusula `except` mostra unha mensaxe de erro. En xeral, capturar unha excepción dáche a oportunidade de corrixir o problema, volvelo intentar, ou polo menos, rematar o programa con elegancia.

Dentro da cláusula `except` podemos ter máis dunha sentenza, e esta pode realizar calquera acción:

```python
ent = input('Introduza a Temperatura Fahrenheit:')
try:
	fahr = float(ent)
	cel = (fahr - 32.0) * 5.0 / 9.0
	print(cel)
except:
	print("Aconteceu un erro")
	print('Por favor, introduza un número')
```

![captura3_4_2.png](captura3_4_2.png)

{{% notice style="warning" title="Reversión de sentenzas" %}}

En Python, ao contrario que noutras linguaxes, cando se produce unha excepción nun bloque `try/except`, **as sentenzas anteriores dentro do bloque o punto onde se xerou a excepción non son revertidas**.

Por exemplo:

```python
sen_reversion = 1
try:
	sen_reversion = 2
	erro = 5/0
	sen_reversion = 3
except:
	print("Produciuse un erro")
print(sen_reversion) # Imprime: 2
```

{{% /notice %}} 

## 3.4.1. Else

Nunha captura de excepcións en Python, pódese utilizar a cláusula `else` para definir un **bloque de código que se executará se non se produce ningunha excepción** dentro do bloque `try`.

Aquí hai un exemplo para ilustrar o uso de `else` nun bloque `try`/`except`:

```python
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: Non se pode dividir por cero.")
    else:
        print(f"O resultado de {a} / {b} e: {resultado}")

dividir(10, 2) # Imprime: O resultado de 10 / 2 e: 5.0

dividir(10, 0) # Erro: Non se pode dividir por cero.
```

## 3.4.2. Finally

A cláusula `finally` en Python utilízase para definir **un bloque de código que se executará sempre tras o bloque `try`, producirase unha excepción ou non.**

Exemplo:

```python
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: Non se pode dividir por cero.")
    else:
        print(f"O resultado de {a} / {b} e: {resultado}")
    finally:
        print("Este bloque executase sempre.")

dividir(10, 2)
'''
O resultado de 10 / 2 e: 5.0
Este bloque executase sempre.
'''
dividir(10, 0)
'''
Erro: Non se pode dividir por cero.
Este bloque executase sempre.
'''
```

En este ejemplo, el bloque `finally` imprime un mensaje que se ejecutará siempre, independientemente de si se captura una excepción o no. La cláusula `finally` es útil para realizar tareas que deben realizarse, como limpieza de recursos, independientemente de si se produce una excepción o no.
