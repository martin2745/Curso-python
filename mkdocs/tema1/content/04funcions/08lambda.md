---
title: "4.8. Expresións Lambda"
weight: 8
---

As expresións **lambda** utilízanse cando necesitamos facer algo simple e estamos interesados en facer o traballo rapidamente en lugar de definir unha función. Estas tamén se coñecen como **funcións anónimas**.

As expresións **lambda** son un xeito de declarar función pequenas sen ter que proporcionar un nome. Estas compórtanse como funcións normais coa palabra clave `def`. Son útiles para definir funcións pequenas. Conteñen unha única expresión, polo que son moi indicadas para funcións con instrucións para fluxo de control.

A súa sintaxe é:

```python
lambda argumentos_separados_por_coma: expresión
```

Exemplos:

```python
square = lambda x: x ** 2
print(square(3)) # Imrpime 9
```

Existe unha sintaxe para realizar unha estrutura condicional simple nunha única liña:

```python
valor_se_true if condicion else valor_se_false
```

Esta pode combinarse cunha expresión **lambda** do seguinte xeito:

```python
lambda_func = lambda x: True if x**2 >= 10 else False
print(lambda_func(3)) # Imprime False
print(lambda_func(4)) # Imprime True
```

Tamén so poden utilizar un número variable de parámetros e utilizar `*args` e `*kargs`.

