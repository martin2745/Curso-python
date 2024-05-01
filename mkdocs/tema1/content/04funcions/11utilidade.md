---
title: "4.11. Utilidade e organización das funcións"
weight: 11
---

## 4.11.1. Utilidade das funcións

Pode non estar moi claro porque merece a pena molestarse en dividilo programa en funcións. Existen varias razóns:

- Ao crear unha función nova dáche a oportunidade de dar nome a un grupo de sentenzas, o cal fai que o programa sexa máis doado de ler, entender e depurar.

- As funcións poden facer un programa máis pequeno, ao eliminar código repetido. Ademais, se queres realizar calquera cambio no futuro, só terás que facelo nun único lugar.

- Dividir o programa largo en funcións permite depurar partes de unha en unha e logo ensamblas nun única peza.

- As funcións ben deseñadas a miúdo resultan útiles para outros moitos programas. Unha vez que os escribiches e depurando unha, podes volver utilizala.

## 4.11.2. Organización de funcións dentro dun mesmo *script*

Polo xeral, as funcións colócanse tras a cabeceira e descrición dun programa. A continuación escríbese o **programa principal**. Podemos dicir que é onde comeza a execución propiamente do programa e no cal se **controla o fluxo de execución**.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exemplo de estrutura dun programa en Python con funcións

__author__ = "Manuel Ramón Varela López"

##################### Funcións: neste apartado defínense as funcións ###################

....

##################### Programa prinicpal: e execución do programa comeza neste punto ###

....
```

## 4.11.3. Organización de funcións en ficheiros externos

Segundo un *script* se volve máis complexo o seu número de liñas crece rapidamente, polo que se fai realmente complicado o seu mantemento. Polo tanto sería de interese poder dividir o *script* en varios ficheiros. O xeral é dividir o *script* entre un ficheiro que actúa como programa principal `__main__.py` é bastante común como nome do ficheiro aínda que pode ter calquera nome) e outros ficheiros con funcións que implementan diferentes algoritmos.

O **programa principal** é o encargado de controlar o fluxo da aplicación. É dicir, que realizar en cada momento. Este utilizará as funcións que se encontran noutros ficheiros para realizar as operacións necesarias. Estes ficheiros deben atoparse no mesmo directorio que o programa principal.

Vexamos un exemplo. Temos un ficheiro de nome `funcions.py` que implementa as seguintes funcións:

```python
def funcion1():
    return "1"

def funcion2():
    return "2"
```

Para utilizar estas funcións no programa principal `__main__.py` debemos importalas. Para realizar iso debemos utilizar a palabra clave **import** e indicar o nome do ficheiro sen a extensión ".py". Exemplo de programa principal que utiliza as funcións anteriores:

```python
import funcions

print(funcions.funcion1())
print(funcions.funcion2())
```

