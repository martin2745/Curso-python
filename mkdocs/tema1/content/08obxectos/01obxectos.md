---
title: "8.1. Obxectos e valores"
weight: 1
---

En Python, **tódolos valores de calquera tipo de datos son obxectos**. Isto inclúe tamén a funcións. Este enfoque de que "todo é un obxecto" é unha característica fundamental do deseño de Python e contribúe a súa flexibilidade e capacidade para traballar con obxectos de xeito dinámico.

Se executamos as seguintes sentencias de asignación:

```python
a = 'banana'
b = 'banana'
```

sabemos que ambos **a** e **b** se refiren a unha cadea, pero non sabemos se se refiren ou apuntan a mesma cadea. Hai dous estados posibles:

![captura8_1_1.png](captura8_1_1.png)

Por un lado, **a** e **b** refírense a dous obxectos diferentes que teñen o mesmo valor. Por outro lado, apuntan ao mesmo obxecto.

Para revisar se as dúas variables apuntan ao mesmo obxecto, podes utilizar o operador `is`.

```python
>>> a = 'banana'
>>> b = 'banana'
>>> a is b
True
```

Neste exemplo, Python soamente creou un obxecto de cadea, e ambas variables apuntan a el.

Pero cando creas dúas listas, tes dous obxectos diferentes:

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a is b
False
```

Neste caso poderíamos dicir que as dúas listas son equivalentes, porque teñen os mesmo elementos, pero non *idénticas*, porque non son o mesmo obxecto. Se dous obxectos son idénticos, son tamén equivalentes, pero se son equivalentes, non necesariamente idénticos.

Ata agora, utilizamos "obxecto" e "valor" de xeito intercambiable, pero é máis preciso dicir que un obxecto ten un valor. Se executas `a = [1,2,3]`, **a** refírese a unha lista de obxectos no que o seu valor é unha secuencia de elementos. Se outra lista ten os mesmos elementos, diríamos que ten o mesmo valor.
