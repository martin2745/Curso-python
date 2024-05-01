---
title: "3.6. Avaliación de expresións lóxicas"
weight: 6
---

Cando Python está procesando unha expresión lóxica, como `x>=2 and (x/y > 2)`, avalía a expresión de esquerda a dereita. Debido a definición de `and`, se x é menor de 2, a expresión `x>=2` resulta ser falsa. De xeito que a expresión completa xa vai ser falsa, independentemente de se `(x/y) > 2` se avalía como verdadeira e falsa.

Cando Python detecta que non se gaña nada avaliando o resto dunha expresión lóxica, detén a súa avaliación e non realiza o cálculo do resto da expresión. Cando a avaliación dunha expresión lóxica se detén debido a que xa se coñece o valor final, iso é coñecido como **cortocircuitar** a avaliación.

A pesar de que isto poida parecer ser fiar moi fino, este funcionamento descóbrenos unha enxeñosa técnica coñecida como **patrón gardián**.

```python
x = 6
y = 2
x >= 2 and (x/y) > 2 # True
x = 1
y = 0
x >= 2 and (x/y) > 2 # False
x = 6
y = 0
x >= 2 and (x/y) > 2
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

A terceira operación falla porque Python intentou avaliar `(x/y)` e y era cero, o cal provoca un erro en tempo de execución. Pero o segundo exemplo non errou porque a primeira parte da expresión foi avaliada como falsa, e polo tanto `(x/y)` non chegou executarse debido a regra do curtocircuíto.

É posible construír expresións lóxicas colocando estratexicamente unha avaliación como **gardián** xusto antes da avaliación que podía causar un erro, como se mostra a continuación:

```python
x = 1
y = 0
x >= 2 and y != 0 and (x/y) > 2 # False
x = 6
y = 0
x >= 2 and y != 0 and (x/y) > 2 # False
x >= 2 and (x/y) > 2 and y != 0
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Na primeira expresión lóxica, `x>=2` é falsa, así que a avaliación detense no primeiro *and*. Na segunda expresión lóxica, `x >= 2` é verdadeira, pero `y != 0` é falsa, de xeito que nunca se alcanza `(x/y)`.

Na terceira expresión lóxica, o `y != 0` avaliase despois do cálculo `(x/y)`, de xeito que a expresión falla.

Na segunda expresión, dise que `y != 0` actúa como gardián para garantir que só se execute `(x/y)` no caso de que y non sexa cero.