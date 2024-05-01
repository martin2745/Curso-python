---
title: "3.5. Tipos de excepcións"
weight: 5
---

En **Python**, e na maioría de linguaxes que utilizan excepcións, hai diferentes tipos de excepcións. O tipo imprímese como parte da mensaxe de erro. Algúns dos máis comúns son:

- **ZeroDivisionError**: prodúcese cando se intenta realizar unha división entre 0.
- **TypeError**: acontece cando unha operación ou función aplícase a un valor de tipo non válido. Por exemplo cando queremos concatenar cadeas de texto con números.
- **ValueError**: xérase cando unha operación ou función recibe un argumento que ten o tipo correcto pero un valor non apropiado.


O tipo é o nome da excepción que aconteceu. Esto é válido para todas as excepcións predefinidas polo intérprete como para aquelas que son definidas polos usuarios. Os nomes das excepcións tamén actúan como palabras reservadas pola linguaxe.

Xunto co nome da excepción, xeralmente aportase máis información da causa de esta excepción.

Neste enlace podemos encontrar as excepcións predefinidas e porque se producen: https://docs.python.org/es/3/library/exceptions.html#bltin-exceptions

## 3.5.1. Captura específica de unha determinada excepción

No anterior punto vimos como capturar calquera excepción. Neste caso, procederemos a capturar a un tipo de excepción concreto.

Para iso, tras a cláusula `except` engadimos o tipo de excepción que queremos capturar:

```python
try:
    x = int(input("Introduce un número: "))
except ValueError:
    print("O valor introducido non se corresponde cun valor numérico")
```

Neste caso, so se capturaran erros dentro do bloque `try` de tipo `ValueError`.

Unha declaración `try` pode ter máis dunha cláusula `except`, para especificar diferentes xestións para diferentes excepcións:

```python
try:
    x = int(input("Introduce un número: "))
    z = 10 / x
except ValueError:
    print("O valor introducido non se corresponde cun valor numérico")
except ZeroDivisionError:
    print("Produciuse unha división entre 0")
```

Como máximo, só se executará un bloque `except`. Cando un destes se executa, directamente se salta todo o bloque `try` con seus correspondentes `except`.

Ademais unha cláusula `except` tamén pode xestionar varias excepcións engadíndoas nun paréntese e separadas por comas tras a directiva `except`:

```python
try:
    x = int(input("Introduce un número: "))
    z = 10 / x
except (ValueError, ZeroDivisionError):
    print("O valor introducido non se corresponde cun valor numérico ou se produciu unha división entre 0")
```


