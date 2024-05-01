---
title: "2.6. Saída de datos por pantalla"
weight: 6
---

Como definición base, podemos identificar a función `print()` de Python como unha utilidade orientada a mostrar por pantalla aquela información desexada, xa sexa dende unha simple presentación do programa que executarán as nosas liñas de código ou mostra ao usuario o realizado polas mesmas.

## 2.6.1. Argumentos da función print

A estrutura base de `print` é:

```python
print(value, sep, end, file, flush)
```

Os tres primeiros argumentos son os máis interesantes. Esta é a súa utilidade:

- **value**: Enténdese como os valores que vamos a mostrar en pantalla. Este pode ser un texto definido entre comiñas, variables, etc. 

- **sep**: Con isto, definimos como se van separar os valores definidos anteriormente, podendo definir dende un simple espacio en branco a case calquera cousa. Por defecto é un espazo.

- **end**: Sírvenos para definir que desexamos que apareza ao final da cadea de texto que aparece por pantalla. Por defecto é o carácter "\n" (salto de liña).

## 2.6.2. Uso simple

Para o uso máis simple existente xa temos exemplos en anteriores apartados. Sen embargo, a estrutura para concatenar múltiples textos é a seguinte:  

```python
print("Texto 1 " + "Texto 2 " + "Texto 3")
```

Mostraría por pantalla o seguinte:

```bash
Texto 1 Texto 2 Texto 3
```

Esta podería alargarse tanto como quixeramos. Sen embargo, presenta varios problemas que poden afectarnos. Primeiro, as separacións debemos definilas dentro das cadeas de texto e ademais debemos asegurándonos de que as variables sexan de tipo **string**. Se unha variable é numérica ou de calquera outro valor, esta sintaxe non función producirá un erro.

Podemos concatenar texto para que se mostre por pantalla indicando cada cadea como un argumento distinto. Deste xeito, as variables non necesitan ser de tipo numérico. **Esta é a forma recomendada**.

```python
var_string = 'Texto 2'
var_numerica = 6
print("Texto 1", var_string, var_numerica)
```

Mostraría por pantalla o seguinte:

```bash
Texto 1 Texto 2 6
```
Como podemos observar, utilízase como separador de cada cadea o espazo e ao finalizar a cadea introdúcese un salto de liña.

Podemos modificar o argumento **sep** producindo os seguintes resultados.

```python
print("Texto1","Texto2",variable,sep=(","))
```

produciría:

```bash
Texto1,Texto2
```

```python
print("Hola", "mundo", sep="-")
```

produciría:

```bash
Hola-mundo
```

{{% notice style="note" title="Tabulacións" %}}

Para separalos mediante tabulación, emprégase o carácter "\t".

```python
print("Hola", "mundo", sep="\t")
```

produciría:


```bash
Hola    mundo
```

{{% /notice %}}


Tamén podemos modificar o argumento **end**. Se o modificamos recordade que non se engade salto de liña. 

```Python
print("Texto 1","Texto 2",variable,sep=(","),end=(". Y se acabó.\n")
```

produciría:

```bash
Texto 1,Texto 2. Y se acabo.
```

## 2.6.3. Cadeas f

O método `format()` permite substituír o interior duns corchetes por variables ou cadeas. Este método pode executarse engadindo unha `f` antes da definición da cadea.

```python
anos = 20
print(f"ti tes {anos} anos")
```

produciría:

```bash
ti tes 20 anos
```

Tamén se pode utilizar do seguinte xeito: 

```python
print('O xeado de {sabor} é o meu {adxectivo}.'.format (sabor='pistacho', adxectivo='favorito'))
```

produciría:

```bash
O xeado de pistacho é o meu favorito.
```

Este método é tal vez algo máis complexo, polo que afondamos na súa explicación:

A base a entender sería:
```python
str.format()
```
O que vén significando que antes da *"fórmula"* haberá un **string**, e despois desta uns parénteses que encher. **Como se fai isto?** 

1. O primeiro é saber que se quere dicir, no caso do exemplo anterior o que se busca e decidir de que sabor é o xeado e se gusta ou non, polo que os ocos a encher serían *sabor* e o *adxectivo*.

2. Unha vez decidido dáselle un significado a eses dous **campos de formato**. esta operación executarase ao final dentro do parénteses, e nela especificamos a que é igual o sabor e a que o formato. 

{{% notice style="info" title="Nota" %}}

É importante destacar tamén que non fai falla especificar tanto, poderíase poñer un valor "0" ou un valor "1" cos que encher os ocos tamén.

{{% /notice %}}

## 2.6.4. Aliñar texto

Pódese aliñar texto usando o parámetro `{:>Numero}.format`.

Por exemplo:

```python
print( "{:>30}".format("palabra") )
```
Isto significa que aliña "palabra" 30 caracteres a dereita.

```bash
                             palabra
```

## 2.6.5. Engadir liñas en branco:

A función `print` tamén pode ser utilizada para engadir liñas en branco de forma sinxela e facer o programa mais lexible.

```python
print("Texto")
print()
print("mais texto")
```
```bash
Texto

mais texto
```

## 2.6.6. Decimais coa función print

Tamén se pode especificar os decimais cos que queremos que se mostre unha operación. Para isto utilízase a seguinte simboloxía `:0.3f` indicaranos os ":" a edición de formato "." para formato decimal e "3" o número de decimais que ten que mostrarnos por pantalla, o "f" o final indícanos o tipo, neste caso de punto fixo.  
Exemplo:  

```python
pi = 3.141595
print("o valor de pi e: {pi:0.4f}")
```

```bash
o valor de pi e: 3.1415
```

{{% notice style="warning" title="Nota" %}}

Non se lle aplica redondeo ao número con este método.

{{% /notice %}}
