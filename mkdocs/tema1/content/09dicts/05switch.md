---
title: "9.5. Simular estrutura switch con dicionarios"
weight: 5
---

En Python, non existe unha construción equivalente a `switch-case` doutras linguaxes. Sen embargo, pódese emular o comportamento utilizando dicionarios.

No seguinte exemplo asignamos un valor dependendo da chave:

```python
switch_dict = {
    'a': case_a,
    'b': case_b,
    'c': case_c
}

resultado = switch_dict(caso, default_case)
print(resultado)
```

Podemos complicar isto almacenando funcións en variables dentro do dicionario.

```python
def case_a():
    #...

def case_b():
    #...

def case_c():
    #...

def default_case():
    #...


switch_dict = {
    'a': case_a,
    'b': case_b,
    'c': case_c
}

funcion_case = switch_dict.get(caso, default_case)
resultado = funcion_case()
return resultado
```

