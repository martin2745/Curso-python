---
title: "4.4. Parámetros e argumentos"
weight: 4
---

Algunhas funcións internas que vimos necesitan argumentos. Por exemplo, cando se chama a `math.sin`, pásaselle o número como argumento. Algunhas funcións necesitan máis dun argumento: `math.pow` por exemplo toma dous, a base e o expoñente.

Dentro das funcións, **os argumentos son asignados a variables chamadas parámetros**. A continuación mostramos un exemplo de unha función definida polo usuario que recibe un argumento:

```python
def mostra_duas_veces(nome):
    print(nome)
    print(nome)
```

Esta función asigna o argumento a un parámetro chamado **nome**. Cando a función é chamada, imprime o valor do parámetro (sexa este o que sexa) dúas veces.

Esta función funciona con calquera valor que poida ser mostrada en pantalla.

```python
mostra_duas_veces('Spam')
'''
Spam
Spam
'''
mostra_duas_veces(17)
'''
17
17
'''
mostra_duas_veces(math.pi)
'''
3.14159265359
3.14159265359
'''
```

As mesmas regras de composición que se aplican a funcións internas, tamén se aplican as funcións definidas polo usuario, de xeito que podemos usar calquera tipo de expresión como argumento para `mostra_duas_veces`.

```python
mostra_duas_veces('Spam '*4)
'''
Spam Spam Spam Spam
Spam Spam Spam Spam
'''
mostra_duas_veces(math.cos(math.pi))
'''
-1.0
-1.0
'''
```

O argumento é avaliado antes de que a función sexa chamada, así que nos exemplos, a expresión `Spam*4` e `math.cos(math.pi)` son avaliadas unha vez.

Tamén se pode usar unha variable como argumento:

```python
miguel = 'Miguel'
mostra_duas_veces(miguel)
'''
Miguel
Miguel
'''
```

O nome da variable que pasamos como argumento, **miguel** non ten nada que ver co nome do parámetro, **nome**. Non importa como se chame o valor en orixe (na chamada); dentro de `mostra_duas_veces` sempre se chamará **nome**.

## 4.5.1. Funcións con máis dun parámetro

As funcións poden ter dende ningún a parámetro ao número que desexemos. Polo xeral as funcións non deberían ter un número moi elevado de parámetros, aínda que iso depende do caso particular de cada problema.

Para definir unha función con máis dun parámetros, estes parámetros defínense dentro das parénteses separado por comas:

```python
def funcion1(parametro1, parametro2, parametro3, ...)
```

Cando se realiza a chamada a estas funcións, a orde dos parámetros é importante, dado que o primeiro valor dentro da paréntese da chamada a función corresponderase co primeiro parámetro da función. O segundo valor, co segundo parámetro, etc.

```python
funcion1(valor_para_parametro1, valor_para_parametro2, valor_para_parametro3, ...)
```

## 4.5.2. Funcións con parámetros clave

Xeralmente en Python utilízanse os parámetros por posición, é dicir que cando se chama a unha función a posición indica que parámetro e cada argumento. Pero tamén temos a posibilidade de non seguir ese orde se utilizamos parámetros con palabras clave.

Consideramos a definición seguinte función:

```python
def funcion1(a, b, c)
```

Se realizamos a seguinte chamada a función:

```python
funcion1(1, 2, 3)
```

Dentro da función `función1`, a variable `a` tomará o valor 1, a variable `b` o valor 2, e a variable `c` o valor 3. Pero nos podemos modificar esta orde na chamada da función se indicamos na chamada da función para tódolos parámetros cal é o seu valor:

```python
funcion1(b=1, c=2, a=3)
```

Neste caso, dentro da función `función1`, a variable `a` tomará o valor 3, a variable `b` o valor 1, e a variable `c` o valor 2. Na chamada a función xa non é necesario seguir a orde de definición dos parámetros.

Na propia definición da función podemos utilizar os parámetros por palabra clave e asignarlle un valor por defecto a un parámetro:


```python
def funcion1(a=1, b=2, c=3)
```

Isto fai que os parámetros que teñen un valor por defecto, non é necesario pasarlles un valor na chamada da función. Realizamos esta chamada a función:

```python
funcion1()
```

Dentro da función `función1`, a variable `a` tomará o valor 1, a variable `b` o valor 2, e a variable `c` o valor 3. Pero podemos sobrescribir estes valores. Podemos sobrescribir o número de valores que queiramos realizando unha chamada por parámetros con palabras clave:


```python
funcion1(a=5, b=7)
```

Neste caso, dentro da función `función1`, a variable `a` tomará o valor 5, a variable `b` o valor 2, e a variable `c` o valor 3.

