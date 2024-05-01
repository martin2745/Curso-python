---
title: "3.1. Expresións booleanas e operadores lóxicos"
weight: 1
---

## 3.1.1. Expresións booleanas

Unha **expresión booleana** é aquela que pode ser verdadeira, **True**, ou falsa, **False**. Os exemplos seguintes usan o operador `==`, que compara dous operandos e devolve verdadeiro se son iguais e falso en caso contrario:

```python
5 == 5 # True
5 == 6 # False
```
{{% notice style="warning" title="Tipo de datos booleano" %}}

**True** e **False** son valores especiais que pertencen ao tipo **bool** (booleano), **non son cadeas**.

{{% /notice %}}


```python
type(True) # <class 'bool'>
type(False) # <class 'bool'>
```

O operador `==` é un dos **operadores de comparación**, os demais son:

```python
x != y			# x é distinto de y?
x > y			# x é maior que y?
x < y			# x é menor que y?
x >= y 			# x é maior ou igual que y?
x <= y			# x é menor ou igual que y?
x is y			# x é o mesmo que y?
x is not y		# x non é o mesmo que y?
```

{{% notice style="note" title="Coidado" %}}

Estas operacións probablemente che resulten familiares, os símbolos en Python son diferentes dos símbolos matemáticos que se utilizan para realizar as mesmas operacións. Un erro común é usar só un símbolo igual `=` en lugar da dobre igualdade `==`. 

`=` é un operador de asignación, e `==` é un operador de comparación. Non existe algo como `=<` ou `=>`.

{{% /notice %}}

## 3.1.2. Operadores Lóxicos

Existen tres **operadores lóxicos**: 

- `and`: e.

- `or`: ou.

- `not`: non.

O significado semántico destas operacións é similar ao seu significado en inglés. Por exemplo: `x > 0 and x < 10` é verdadeiro só cando x é maior que 0 e menor que 10.

Outro exemplo: `n%2 == 0 or n%3` é verdadeiro se calquera das condicións é verdadeira, é dicir, se o número é divisible por 2 ou por 3.

Por último, o operador *not* nega unha expresión booleana, de xeito que `not (x > y)` é verdadeiro se x é maior que y é falso. Ou o que é o mesmo: x é menor ou igual que y.

Estritamente, os operandos dos operadores lóxicos deberían ser expresións booleanas, pero Python non é moi estrito. Calquera número distinto de cero interprétase como verdadeiro.

```python
17 and True # True
```

Esta flexibilidade pode ser útil, pero existen certas sutilezas neste tipo de uso que poden resultar confusas. É posible que prefiras evitar usalo deste modo ata que esteas ben seguro do que estás facendo.

## 3.1.3. Expresións booleanas encadeadas

O encadeamento de operadores de comparación permite combinar mútiples combinacións nunha única expresión. Isto permite non ter que utilizar expresións separadas con operadores lóxicos.

A sintaxe xeral é a seguinte:

```python
valor_minimo < variable < valor_maximo
```
Isto tradúcese en "a variable debe ser maior que `valor_minimo` e menor que `valor_maximo`". Exemplos:

- Verificar se un numero esta nun rango:

    ```python
    numero = 15
    10 < numero < 20 # True
    ```

- Verificar se un carácter é unha letra minúscula

    ```python
    letra = 'b'
    e_minuscula = 'a' <= letra <= 'z' # True
    ```

## 3.1.4. O valor None en expresións booleanas

Podemos utilizar o valor `None` en comparacións para verificar se unha variable ten un valor asignado:

```python
variable = None
variable is None # True
variable2 = 3
variable2 is None # False
```

Este valor tamén se pode avaliar como o valor `False`:

```python
variable = None
not variable # True
```
