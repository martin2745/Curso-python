---
title: "10.2. Importar funcións ou variables concretas"
weight: 2
---

En Python non temos porque importar todo o contido dun módulo, podemos importar tan só os elementos que desexamos utilizar.

Para importar unha función específica debemos utilizar a seguinte sintaxe:


```python
from o_meu_modulo import funcion_concreta
```

Isto importará só a función `funcion_concreta` do módulo `o_meu_modulo`. Para utilizala xa non se debe antepoñer o nome do módulo antes de chamar a función. Por exemplo:

Esto importará solo la función `nombre_de_la_funcion` del módulo `mi_modulo`. Luego, puedes usar la función directamente sin tener que anteponer el nombre del módulo. Por exemplo:

```python
from o_meu_modulo import saudar

saudar("Manuel")
```

Do mesmo xeito podémolo facer cunha variable:


```python
from o_meu_modulo import pi

print(pi)
```

Para importar varios elementos tan só os debemos indicar separándoos con comas:

```python
from o_meu_modulo import saudar, pi

saudar("Manuel")
print(pi)
```