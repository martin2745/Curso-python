---
title: "12.2. Decorar unha función"
weight: 2
---

A sintaxe básica para decorar unha función é a seguinte:

```python
@funcion_decoradora
def funcion_a_decorar():
    pass
```

Ao usar `@funcion_decoradora` antes de definir a función `funcion_a_decorar`, estamos aplicando o decorador `funcion_decoradora` a `funcion_a_decorar`.

Isto significa que cando chamemos a función `funcion_a_decorar()`, en realidade estamos invocando a función `funcion_a_executar(*args, **kwargs)`.
