---
title: "4.1. Funcións internas"
weight: 1
---

Python proporciona un número importante de funcións internas, que poden ser usadas sen necesidade de ter que definilas previamente. Os creadores de Python escribiron un conxunto de funcións para resolver problemas comúns e incluíronas en Python para que as poidamos utilizar.

## 4.1.1. Funcións max, min e len

As funcións `max` e `min` devolven o valor e maior dunha lista:

```python
max("Ola, mundo!") # 'u'
min("Ola, mundo!") # ' '
```

A función `max` dinos cal é o carácter máis grande da cadea de texto, mentres que a función `min` móstranos o carácter máis pequeno. 

{{% notice style="info" title="ASCII" %}}

Cada carácter ten asociado un valor numérico. Estes valores numéricos están establecidos polos códigos [ASCII](https://es.wikipedia.org/wiki/ASCII).

Para obter o código ASCII dun caracter utilizamos a función `ord`.

```python
caracter = 'a'
codigo = ord(caracter)
```

{{% /notice %}}


Outra función interna moi común é `len`, que nos di cantos elementos hai no argumento. Se o argumento de `len` é unha cadea, devólvenos o número de caracteres que hai na cadea.

```python
>>> len("Ola, mundo")
11
```

 Estas funcións non se limitan a buscar en cadeas. Poden operar con calquera conxunto de valores.

O nome das funcións internas trátanse como se foran palabras reservadas. Polo tanto `max` non se pode usar como nome para unha variable.

- [max](https://docs.python.org/3/library/functions.html?highlight=max#max)

- [min](https://docs.python.org/3/library/functions.html?highlight=min#min)

- [len](https://docs.python.org/3/library/functions.html?highlight=len#len)

## 4.1.2. Funcións para conversión de tipos

Python tamén proporciona funcións internas que converten valores dun tipo a outro. A función `int` toma calquera valor e convérteo a un enteiro, se pode, e se non queixase:

```python
int('32') # 32
int('Hola') # ValueError: invalid literal for int() with base 10: 'Hola'
```

`int` pode converter valores en punto flotante a enteiros, pero non os redondea; simplemente corta e descarta a parte decimal:

```python
int(3.99999) # 3
int(-2.3) # -2
```

`float` converte enteiros e cadeas en números de punto flotante:

```python
float(32) # 32.0
float('3.14159') # 3.14159
```

Por último, `str` converte o seu argumento nunha cadea:

```python
str(32) # '32'
str(3.14159) # '3.14159'
```

## 4.1.3. Funcións matemáticas

Python ten un módulo matemático (**math**), que proporciona a maioría das funcións matemáticas habituais. Antes de que poidamos utilizar o módulo, deberemos importalo.

```python
import math
```

Esta sentenza crea un *obxecto módulo* chamado **math**.

O obxecto módulo contén as funcións e variables definidas no módulo. Para acceder a unha desas funcións, é necesario especificar o nome do módulo e o nome da función, separados por un punto.

```python
relacion = int_senal / int_ruido
decibelios = 10 * math.log10(relacion)
radianes = 0.7
altura = math.sin(radianes)
```

O primeiro exemplo calcula o logaritmo en base 10 da relación sinal-ruído. O módulo **math** tamén proporciona unha función chamada `log` que calcula logaritmos en base e.

O segundo exemplo calcula o seno da variable *radianes*. O nome da variable é unha pista de que `sin` e outras funcións trigonométricas (`cos`, `tan`,etc.) toman argumentos en radiáns. Para converter de grados a radiáns, hai que dividir por 360 e multiplicar por 2 por pi.

```python
grados = 45
radianes = grados / 360.0 * 2 * math.pi
print(math.sin(radianes))
0.7071067811865476
```

A expresión **math.pi** toma a variable pi do módulo *math*. O valor desta variable é unha aproximación de pi, cunha precisión duns 15 díxitos.

Tamén é posible importar só unhas poucas funcións dun módulo. Por exemplo no seguinte exemplo importamos só as funcións `tan` e `sin` e a variable **pi**.

```python
from math import tan,sin, pi
```

Ao importar só unha parte das funcións que ten o módulo *math*, xa non é necesario indicar o nome do módulo e a función separada por un punto. O exemplo anterior teriamos que realizalo así:

```python
grados = 45
radianes = grados / 360.0 * 2 * pi
sin(radianes)
0.7071067811865476
```

- [Módulo math](https://docs.python.org/3/library/math.html?highlight=math#module-math)

## 4.1.4. Funcións para números aleatorios

A partir das mesmas entradas, a maioría de programas xerarán as mesmas saídas cada vez, é o que chamamos comportamento **determinista**. O determinismo xeralmente é algo bo, xa que esperamos que a mesma operación proporcione sempre o mesmo resultado. Para certas aplicacións, sen embargo, queremos que o resultado sexa impredicible. Os xogos son un exemplo obvio, pero hai máis.

Conseguir que un programa sexa realmente non-determinista non resulta sinxelo. Pero hai dous modos de facer que o pareza. Un deles é usar algoritmos que xeren números **pseudoaleatorios**. Os números pseudoaleatorios non son verdadeiramente aleatorios, xa que son xerados por unha operación determinista, pero se só nos fixamos nos números resulta case imposible distinguilos dos aleatorios de verdade.

O módulo **random** proporciona funcións que xeran números pseudoaleatorios. A partir de agora referirémonos a eles como aleatorios inda que non o sexan.

A función `random` devolve un número en coma flotante aleatorio entre 0.0 e 1.0 (inclúese 0.0 pero non 1.0). Cada vez que se chama a `random`, obtense o número seguinte de unha longa serie. Creamos un bucle e executámolo:

```python
import random

for i in range(10):
	x = random.random()
	print(x)
   
0.11132867921152356
0.5950949227890241
0.04820265884996877
0.841003109276478
0.997914947094958
0.04842330803368111
0.7416295948208405
0.510535245390327
0.27447040171978143
0.028511805472785867
```

A función `random` soamente é unha das moitas que traballan con números aleatorios. A función `randint` toma parámetros *inferior* e *superior*, e devolve un enteiro entre inferior e superior(incluíndo ambos extremos).

```python
random.randint(5, 10) # 5
random.randint(5, 10) # 9
```

- [Módulo random](https://docs.python.org/3/library/random.html?highlight=random#module-random)