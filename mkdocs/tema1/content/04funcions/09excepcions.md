---
title: "4.9. Lanzar excepcións"
weight: 9
---

En apartados anteriores vimos que dentro das función podían producirse erros e que estes se podían controlar mediante **captura de excepcións**. Neste capítulo veremos como se indica dentro dunha función que se produciu un erro. Isto coñécese como **lanzar unha excepción**.

A declaración `raise` permite ao programador forzar a que aconteza unha excepción específica.

Imaxinemos que creamos unha función que calcula a raíz cadrada dun número que se pasa como argumento. Se o número proporcionado é un número negativo podemos lanzar unha excepción de tipo **ValueError**. Exemplo:

```python
def raiz_cadrada(numero):
    if numero < 0:
        raise ValueError
    else:
        return numero ** 1/2
```

Unha vez que se executa unha sentenza `raise` remata de executarse a función, polo que non se executan máis sentenzas da función. Se no programa principal non se captura dite excepción cando se fai a chamada a función, o programa rematará indicando o erro cometido se se chega a lanzar a excepción.

Polo tanto, cando se realiza unha función que lanza algún tipo de excepción debe de indicarse nos comentarios e documentación da función.

Se non queremos indicar ningunha excepción particular, podemos utilizar a excepción **Exception**.


