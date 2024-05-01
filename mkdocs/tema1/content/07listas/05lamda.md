---
title: "7.5. Programación funcional e listas"
weight: 5
---

A programación funcional é un paradigma de programación na que as funcións poden ser pasadas como argumentos a outras funcións, devoltas como valores de outras funcións ou asignadas a variables. Isto último xa o vimos nas expresións **lambda**.

Neste apartado veremos como pasar funcións a outras funcións para manipular listas. **Todas as funcións que imos a ver non modifican as listas orixinais, senón que crean unha nova lista.**

## 7.5.1. Realizar unha operación sobre cada elemento dunha lista

Se queremos realizar unha operación sobre cada elemento dunha lista podemos utilizar a función `map()`. A súa sintaxe é a seguinte:

```python
map(función, lista)
```

Esta devolve un obxecto `map` polo que é necesario pasalo a unha lista utilizando a función `list`.

Se a función tan só ten unha expresión, podemos utilizar unha expresión **lambda**. Neste caso tan só temos un parámetro, que se pode expresar con calquera nome de parámetro pero xeralmente utilízase a variable `x`.

Por exemplo, queremos multiplicar por 2 os elementos dunha lista de números utilizando a función `map()`:

```python
numeros = [1,2,3]
obxecto_map = map(lambda x: x*2 , numeros) # Obtemos o obxecto de tipo map
novos_numeros = list(obxecto_map) # Pasamos o obxecto tipo map a unha lista


numeros = list(map(lambda x: x*2 , numeros)) # Deste xeito sobrescribimos a lista orixinal nunha unica liña
```

## 7.5.2. Filtrar elementos dunha lista

Para iso podemos utilizar a función `filter()`. A sintaxe é igual que a función `map()`. Neste caso se a expresión lambda realizase sobre cada elemento. Se o resultado desta devolve `True` o elemento estará na nova lista, e se devolve `False` non estará. Neste exemplo filtramos tan só os números pares:

```python
numeros = [1,2,3,4]
pares = list(filter(lambda x: x%2 == 0 , numeros)) # Deste xeito temos unha lista tan só cos números pares
```

## 7.5.3. Outras funcións con expresións lambda

- A función `sorted` permítenos ordenar elementos dunha lista na orde que desexemos: https://docs.python.org/3/howto/sorting.html

- Función `reduce`: https://docs.python.org/3.0/library/functools.html

