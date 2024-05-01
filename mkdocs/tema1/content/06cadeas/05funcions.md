---
title: "6.5. Métodos de cadeas"
weight: 5
---

Algunha das funcións e métodos máis utilizados por cadeas en Python preséntanse a continuación. **Tanto os métodos como funcións crean sempre unha nova cadea, debido a que as cadeas son inmutables.**

## 6.5.1. Minúsculas e maiúsculas

Os métodos **`str.upper()` e `str.lower()`** converten a cadea a maiúsculas ou a minúsculas segundo o caso. En cambio os métodos **`str.capitalize()` e `str.title()`** poñen a primeira letra da cadea en maiúsculas e o resto en minúsculas.

```python
texto = "Python"
maiusculas = texto.upper()
minusculas = texto.lower()
```

## 6.5.2. Eliminar espazos en branco ao inicio ou final

Os métodos **`str.strip()`**, **`str.lstrip()`** e **`str.rstrip()`** eliminan espazos ao inicio, final ou a ambos lados da cadea.

```python
texto = "   Ola, mundo!   "
sen_espazos = texto.strip()
```

## 6.5.3. Buscar posición

**`str.find(subcadena)`** y **`str.index(subcadena)`** encontran a posición da primeira aparición dunha subcadea na cadea.

```python
texto = "Python e divertido"
posicion = texto.find("div")
```

## 6.5.4. Substitución

**`str.replace(antiguo, nuevo)`** substitúe tódalas ocorrencias dunha subcadea con outra.

```python
texto = "Ola, mundo!"
modificado = texto.replace("mundo", "Python")
```

## 6.5.5. Dividir

**`str.split(separador)`** divide a cadea nunha lista de subcadeas utilizando o separador indicado.

```python
texto = "Python e divertido"
palabras = texto.split(" ")
```

## 6.5.6. Máis métodos e funcións

Pódense atopar máis métodos no seguinte enlace [enlace ](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).