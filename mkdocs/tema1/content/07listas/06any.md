---
title: "7.6. Funcións any e all"
weight: 6
---

As funcións `any()` e `all()` son funcións incorporadas que operan sobre listas e devolven valores booleanos.

## 7.6.1. Any

A función `any()` devolve **`True` se polo menos un dos elementos da secuencia é avaliado como verdadeiro**. Se todos os elementos son avaliados como falso ou a secuencia esta baleira, devolve falso.

```python
lista = [1, 0, -3, 4, 5]
resultado = any(x > 0 for x in lista)
print(resultado) # Imprime: True
```
Neste exemplo, avaliase se polo menos un dos números é maior que 0.


## 7.6.2. All

A función `all()` **devolve `True` se tódolos elementos dunha secuencia son avaliados como verdadeiro**. Se polo menus un dos elementos é `False` ou se a lista está baleira, devolve falso.


```python
numeros = [2, 4, 6, 8, 10]
resultado = all(n % 2 == 0 for n in numeros)
print(resultado) # Imprime: True
```

Neste exemplo, `all()` avalíase se tódolos números na lista son pares.