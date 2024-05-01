---
title: "4.12. DocString"
weight: 12
---

Un **docstring** é unha cadea de texto que se encontra na parte superior dunha función (ou tamén nunha clase, método ou módulo) que proporciona documentación sobre o seu propósito e uso. Estes son unha forma de documentación en liña e son utilizados para describir a funcionalidade do compoñente.

A convención máis común para escribir os *docstrings* é utilizar triples comillas (`'''` o `"""`) para delimitar o texto.

```python
def funcion_documentada(parametro):
    """
    Esta e a descripción da función.

    :param parametro: Descrición do parámetro.
    :return: Descrición do valor de retorno.
    """
    # Corpo da función
    return resultado
```

Neste exemplo, o *docstring* esta colocado xusto debaixo da definición da función e contén información sobre o propósito da función, os parámetros que acepta e o valor que devolve.

Conta cos seguintes compoñentes:

- **Descrición da función**: proporciona unha descrición concisa do propósito da función.

- **Sección de parámetros**(`:param`): enumera os parámetros que acepta a función, xunto cas súas descricións.

- **Sección de valor de retorno** (`:return`): describe o valor que devolve a función. Se non devolve ningún valor esta sección pode omitirse.

- **Outros compoñentes opcionais**: dependendo da complexidade, podes incluír outras seccións como `:raises` para as excepcións que pode xerar a función, ou `:Example` para proporcionar exemplos de uso.

Os *docstrings* son accesibles como o atributo `__doc__` da función. Podes acceder a eles programaticamente para obter información de documentación.

```python
print(funciona_documentada.__doc__)
```

Ademais, utilizar os *docstrings* permiten aos IDEs acceder a esta información e proporcionar axuda mentres programamos.
