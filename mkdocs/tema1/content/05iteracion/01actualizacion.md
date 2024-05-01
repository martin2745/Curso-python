---
title: "5.1. Actualización de variables"
weight: 1
---

Un dos usos habituais de sentenzas de asignación consiste en realizar unha actualización sobre unha variable, na cal o valor novo desa variable depende do antigo.

```python
x = x + 1
```

Isto quere dicir: toma o valor actual de x, engádelle 1, e logo actualiza x co novo valor.

Se intentas actualizar unha variable que non existe, obterás un erro, xa que Python avalía o lado dereito antes de asignar o valor de x.

```python
x = x + 1 # NameError: name 'x' is not defined
```

Antes de que poidas actualizar unha variable, debes **inicializala**, xeralmente mediante unha asignación.

```python
x = 0
x = x + 1
```

Actualizar unha variable engadíndolle 1 chámaselle **incrementar**; restarlle 1 recibe o nome de **decrementar**.
