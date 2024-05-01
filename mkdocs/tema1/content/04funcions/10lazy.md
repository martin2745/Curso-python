---
title: "4.10. Funcións lazy"
weight: 10
---

O termo ***lazy*** utilízase a miúdo para describir a avaliación perezosa ou diferida. No contexto de funcións, isto refírese a idea de que os valores non se calculan ou xeran ata que son necesarios.

Noutras palabras, as funcións *lazy* pospoñen a execución ou xeración de valores ata que se solicitan explicitamente. Isto pode ser beneficioso en termos de eficiencia de recursos, sobre todo cando se traballa con datos grandes ou secuencias infinitas, xa que non é necesario calcular ou xerar tódolos valores de antemán.

Un exemplo son as funcións coa cláusula `yield`. Esta utilízase para suspender a execución dunha función ata que se solicite o próximo valor. Estas chámanse funcións xeradoras.

No lugar de devolver un único valor con `return`, estas funcións utilizan `yield` para xerar unha secuencia de valores. Cada vez que se alcanza un `yield`, a función párase e devolve o valor indicado. Cando se solicita o seguinte valor, a execución da función reiníciase xusto despois do último `yield`, mantendo o seu valor interno.

Exemplo:

```python
def contador(maximo):
    contador_actual = 0
    while contador_actual < maximo:
        yield contador_actual
        contador_actual += 1

# Uso da función xeradora
generador = contador(5)

for valor in generador:
    print(valor)
```

Neste exemplo, `contador` é unha función xeradora que produce unha secuencia de números dende 0 ata `maximo - 1`. Cada vez que se solicita o próximo valor, a función execútase ata chegar ao `yield`, onde devolve o valor actual.

Estas funcións son eficientes en termos de memoria, xa que só manteñen o estado interno e non xerar toda a secuencia de valores dunha vez.

No seguinte exemplo, utilizamos a función `next()` para obter un novo valor, porque creamos unha función xeradora infinita.

```python
def numeros_pares_infinitos():
    numero = 0
    while True:
        yield numero
        numero += 2

# Uso da función xeradora "lazy"
xenerador_pares = numeros_pares_infinitos()

# Imprimos os 5 primeiros pares
for i in range(5):
    print(next(xenerador_pares))
```

neste exemplo, a función `numeros_pares_infinitos` produce infinitos números pares, pero só se calculan e xerar a medida que se solicitan. A función xera un novo número cando se executa a función `next()`