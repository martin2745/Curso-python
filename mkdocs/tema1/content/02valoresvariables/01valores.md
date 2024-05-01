---
title: "2.1. Valores, variables e nomes"
weight: 1
---

## 2.1.1. Valores

Un **valor** é una das cousas básicas que utiliza un programa, como unha letra ou un número. Estes valores poden ser de tipos distintos. Por exemplo 1 e 2 son valores de tipo enteiro, **int** e "Ola mundo!" é unha cadea de caracteres, **string**. As cadeas de caracteres van encerradas entre comiñas.

A sentencia `print` xa a vimos en apartados anteriores. Servía para mostrar por pantalla texto. Esta sentencia funciona con **string** pero tamén con **int**.

```python
print(4) # Imprime: 4
```

Se non estás seguro de que tipo é un valor, a función `type()` indícanos cal é o seu tipo.

```python
print(type("Ola mundo"))  # Imprime: <class 'str'>
print(type(17))  # Imprime: <class 'int'>
```

Os números con decimais son do tipo **float**. Isto é debido a que internamente estes son representados no formato *coma flotante*.

```python
print(type(3.2))  # Imprime: <class 'float'>
```

{{% notice style="warning" title="Números como cadeas de texto" %}}

Se os valores numéricos van entre comiñas, non se interpretan como números senón que como cadeas de texto.

```python
print(type("17"))  # Imprime: <class 'str'>
print(type("3.2") ) # Imprime: <class 'str'>
```

{{% /notice %}}

Cando escribes un número grande, pode que intentes usar comas ou puntos para separalo por grupos de tres díxitos. Por exemplo: 1.000.000 ou 1,000,000. Isto non é posible en Python nin na maioría de linguaxes de programación. O **separador de decimais** en Python, tal e como xa vimos, **é o punto**.

## 2.1.2. Tipo de datos

Na seguinte táboa realizase un resumo do tipo de datos existente en Python:

| Tipo/clase | Categoría | Notas | Exemplo |
| --- | --- | --- | --- |
| int | Números | Número enteiro de precisión fixa | 42 |
| long | Números | Número enteiro en caso de *overflow* | 42L ou 456966786151987643L |
| float | Números | Número en coma flotante |  3.1415927 |
| bool | Booleano | Só existen os dous valores lóxicos  | **True** e **False** |
| str | Cadea | Cadea de caracteres | "Ola mundo" |

{{% notice style="info" title="Carácteres e ASCII" %}}

Cada carácter dun **string** ten asociado un valor numérico. Estes valores numéricos están establecidos polos códigos [ASCII](https://es.wikipedia.org/wiki/ASCII).

{{% /notice %}}

Existe un tipo de datos que representa a ausencia dun valor ou a falta dun valor dado: `None`. É moi utilizado para indicar que unha variable ou unha expresión non ten un valor definido.

Pode ser útil cando se desexa inicializar unha variable antes de asignarlle un valor específico.

```python
variable_sin_valor = None
```

## 2.1.3. Variables

Unha das características máis potentes dunha linguaxe de programación é a capacidade de manipular **variables**. Unha variable é un nome que se refire a un valor.

Unha **sentencia de asignación** crea variables novas e dálles valores utilizando o operador de asignación `=`. O lado esquerdo do operador conten a variable e o lado dereito o valor que se lle asigna a variable.

```python
mensaxe = "Nova mensaxe"
n = 17
pi= 3.1415
```

Neste exemplo facemos tres asignacións. Na primeira asignamos unha cadea de texto a unha variable nova chamada *mensaxe*; na segunda asignamos o enteiro 17 a *n*; e na terceira o valor aproximado de pi a *pi*.

Podemos mostrar por pantalla o valor dunha variable coa sentenza `print()`.

```python
print(n)  # Imprime: 17
print(pi)  # Imprime: 3.1415
```

O tipo da variable, é o tipo do valor que está gardado nesa variable.

```python
type(mensaxe)  # Tipo: <class 'str'>
type(n) # Tipo: <class 'int'>
type(pi)  # Tipo: <class 'float'>
```

## 2.1.4. Nomes de variables e palabras clave

Os programadores xeralmente elixen nomes para as súas variables que teñan sentido e documenten para que se usa a variable.

Os nomes das variables poden ser largos. Poden conter tanto letras como números, pero non poden comezar por un número. Pódense usar letras maiúsculas, pero é boa idea comezar o nome das variables con letra minúscula.

O carácter guión baixo (_) pode utilizarse nun nome de variable. Utilizase a miúdo en nomes con múltiples palabras. Por exemplo: *o_meu_nome*. Os nomes das variables poden comezar co carácter guío baixo, pero xeralmente evitase usalo. Úsase cando se está escribindo código para librerías que logo utilizarán outros. Este estilo de nomenclatura coñecese como ***snake_case***

Se se lle da a unha variable un nome non permitido, obtense un erro de sintaxe:

```python
76trombons = "gran desfile" # Obtemos o erro: SyntaxError: invalid syntax
more@ = 1000000 # Obtemos o erro: SyntaxError: invalid syntax
class = 'Teorema avanzado' # Obtemos erro
```

`76trombons` é incorrecto porque comeza por un número. `more@` é incorrecto porque contén un carácter non permitido: `@`.

A nome de variable `class` tamén é incorrecto porque é unha **palabra clave** de Python. O intérprete utiliza palabras clave para recoñecer a estrutura do programa e esas palabras non poden ser utilizadas como variables. Esas palabras reservadas son as seguintes:

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

Como curiosidade podemos atopar unha linguaxes cun vocabulario "especial": https://www.xataka.com/servicios/lenguajes-programacion-para-partirse-caja-que-funcionan