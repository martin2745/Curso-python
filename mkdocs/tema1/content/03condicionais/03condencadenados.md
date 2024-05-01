---
title: "3.3. Condicionais encadeados e aniñados"
weight: 3
---


## 3.3.1. Condicionais encadeados

Algunhas veces hai máis de dúas posibilidades, de xeito que necesitamos máis de dúas ramas. Unha forma de expresar unha operación como esa é usar un **condicional encadeado**:

```python
if x < y :
    print ('menor')
elif x > y:
    print ('maior')
else:
    print('igual')
```

`elif` é unha abreviatura para *else if*. Neste caso tamén será executada unicamente unha das ramas.

![captura3_3_1.png](captura3_3_1.png)

No hai límite para o número de sentenzas `elif`. Se hai unha cláusula `else`, ten que ir o final, pero tampouco é obrigatorio que exista.

```python
if resposta == 'a':
	print('Respuesta incorrecta')
elif resposta == 'b':
	print('Respuesta correcta')
elif resposta == 'c':
	print('Casi, pero non e correcto')
```

{{% notice style="warning" title="Coidado" %}}

Cada condición é comprobada en orde. Se a primeira é falsa, compróbase a seguinte e así cas demais. Se unha delas é verdadeira, execútase a rama correspondente, e a sentenza acaba. **Incluso se hai máis dunha condición que é verdadeira, só se executa a primeira que se encontra.**

{{% /notice %}}


## 3.3.2. Condicionais aniñados

Un condicional pode tamén estar aniñado dentro doutro. Poderíamos escribir o exemplo do apartado anterior deste xeito:

```python
if x == y:
	print('x e y son iguales')
else:
	if x < y:
		print('x es menor que y')
	else:
		print('x es mayor que y')
```

O condicional exterior ten dúas ramas. A primeira executa unha sentenza simple. A segunda contén outra sentenza `if`, que ten a súa vez as súas propias dúas ramas. Esas dúas ramas son ambas sentenzas simples, pero poderían ter sido sentenzas condicionais tamén.

![captura3_3_2.png](captura3_3_2.png)

A pesar de que o indentado das sentenzas fai que a estrutura estea clara, os **condicionais aniñados** poden volverse difíciles de ler rapidamente. En xeral, é boa idea evitalos se se pode.

Os operadores lóxicos a miúdo proporcionan un modo de simplificar as sentenzas condicionais aniñadas. Por exemplo, o código seguinte pode ser escrito usando un único condicional.

```python
if 0 < x:
	if x < 10:
		print('x e un número positivo cun un so dixito.')
```

A sentenza `print` execútase soamente se se cumpren as dúas condicionais anteriores, así que en realidade podemos conseguir o mesmo efecto co operador `and`:

```python
if 0 < x and x < 10:
	print('x e un número positivo cun un so dixito.')
```