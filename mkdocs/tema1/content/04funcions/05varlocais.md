---
title: "4.5. Ámbito: Variables locais e globais"
weight: 4
---

O ámbito dunha variable **é o contexto no que existe esa variable**. Unha variable existe en dito ámbito dende o momento no que se crea e deixa de existir cando desaparece o seu ámbito. Estas ademais só son accesibles dende o seu propio ámbito.

Os principais ámbitos en Python son:

- **Local**: corresponde co ámbito dunha función. Existe dende que se invoca a función ata que remata a execución. Non se pode acceder a estas variables dende fora da función.

- **Global**: corresponde co ámbito que existe dende o comezo da execución dun programa. Todas as funcións definidas fora de calquera función corresponden ao ámbito global. Pódense acceder a elas dende calquera punto do programa, incluídas as funcións.

## 4.5.1. Variables locais en funcións

Aquelas variables que se utilizan por primeira vez dentro dunha función tan só existen durante a execución da función. Polo tanto, unha vez rematada a execución da función, non poderemos acceder ao valor desa variable. Estas variables coñécense como **variables locais**.

```python
def funcion1(parametro1, parametro2):
    a = 2
    resultado (parametro1 + paramentro2) / a
```

Por exemplo, no caso anterior, a variable `a` tan só pode ser accesible dende dentro da función debido a que é unha variable local.

Os **parámetros dunha función tamén se consideran variables locais**. Isto é porque os valores que se pasan nunha chamada a unha función son copiados dentro das variables dos parámetros. Isto coñécese como **paso por valor**.

```python
def sumador(a, b):
	suma = a + b
	return suma
c = 3
d = 5
x = sumador(c, d)
print(x) # 8
```

No exemplo anterior, cando o valor de `c` copiase no parámetro `a` da función e o `d` copiase en `b`. De feito aínda que cambiemos os valores dos parámetros `a` e `b` dentro da función, as variables `c` e `d` non se modificarán:

```python
def sumador(a, b):
	suma = a + b
    a = 4
    b = 6
	return suma
c = 3
d = 5
x = sumador(c, d)
print(c) # 3
print(d) # 5
```

## 4.5.2. Preferencia de variables

Se existe unha variable local nunha función co mesmo nome que unha variable global, os seus nomes entran en conflito.

**Python busca primeiro no ámbito local para ver se encontra a variable, e senón busca no ámbito global**. É dicir, as variables locais teñen preferencia sobre as globais.

É preferible evitar uso excesivo de variables globais. É mellor pasar parámetros a funciones e devolver resultados.

