---
title: "9.1. Dicts"
weight: 1
---

Vamos a construír un dicionario que asocia palabras en Inglés a Galego, así que todas as chaves e valores son cadeas.

## 9.1.1. Definición de un dicionario

A función `dict` crea un novo dicionario sen elementos. Debido a que **dict** e o nome dunha función interna, non deberías usalo como nome dunha variable.

```python
eng2gal = dict()
print(eng2gal) # Imprime: {}
```

As chaves, `{}`, representan un dicionario vacío. Tamén se pode crear un dicionario baleiro do seguinte xeito:

```python
eng2gal = {}
```

## 9.1.2. Agregar pares chave-valor nun dicionario

Para agregar elementos a un dicionario, podes utilizar corchetes:

```python
eng2gal['one'] = 'un'
```

Este liña crea un elemento asociando a chave 'one' ao valor 'un'. Se imprimimos o dicionario de novo, vamos a ver un par chave-valor con dous puntos entre a chave e o valor:

```python
print(eng2gal) # Imrpime: {'one':'un'}
```

Este formato de saída tamén é un formato de entrada. Por exemplo, podes crear un novo dicionario con tres elementos. Pero se imprimes **eng2gal**, vaste sorprender:

```python
eng2gal = {'one': 'un', 'two': 'dous', 'three': 'tres'}
print(eng2gal) # Imprime: {'one': 'un', 'three': 'tres', 'two': 'dous'}
```

A orde dos pares chave-elemento non é o mesmo. De feito, se escribes este mesmo exemplo no teu ordenador, poderías obter un resultado diferente.

## 9.1.3. Acceso a valores dun dicionario a través da súa chave

Pero ese non é un problema porque os elementos dun dicionario nunca son indexados con índices enteiros. En lugar diso, utilizas as chaves para encontrar os valores correspondentes:

```python
print(eng2gal['two']) # Imrpime: 'dous'
```

A chave "two" sempre se asocia ao valor "dous", así que a orde dos elementos non importa.

Se a chave non está no dicionario, obterás unha excepción:

```python
print(eng2gal['four']) # Obtense a excepción: KeyError: 'four'
```

Os dicionario ao igual que as listas son **mutables**. Se un dicionario é modificado dentro dunha función, o contido tamén se modifica no resto do programa.

O método `get()` é unha forma segura de obter o valor asociado a unha clave nun diccionario sen xerar unha excepción se a clave non está presente. A sintaxe básica é a siguinte:

```python
valor = dicionario.get(clave, valor_por_defecto)
```

- `dicionario`: o dicionario do cal queres obter o valor.

- `clave`: a clave que estás buscando no dicionario.

- `valor_por_defecto` (opcional): é o valor que se devolverá se a clave non está presente no dicionario. Se este argumento non se proporciona, `None` utilizarase como valor por defecto.

Exemplo:

```python
dicionario = {'a': 1, 'b': 2, 'c': 3}

valor = dicionario.get('b', 'Non encontrado')
print(valor) # Imprime: 2

valor_non_encontrado = dicionario.get('z', 'Non encontrado')
print(valor_non_encontrado) # Imprime: No encontrado

valor_non_encontrado = dicionario.get('z')
print(valor_non_encontrado) # Imprime: None
```

## 9.1.4. Declarar dicionario baleiro

Para declarar un dicionario baleiro podemos utilizar este código:

```python
dicionario = {}
```

## 9.1.5. Crear dicionario a partir de dúas listas

A función `zip()` tema dúas listas e combinas nunha secuencia de tuplas. Cada tupla contén elementos correspondentes aos iterables orixinais. Esta resultado pode transformarse nun dicionario de xeito simple:

```python
nomes = ['Alice', 'Bob', 'Charlie']
idades = [25, 30, 35]

# Utiliza zip() para combinar as listas nunha secuencia de tuplas
tuplas_combinadas = zip(nomes, idades)

# Converte a secuencia de tuplas nun dicionario
dicionario_persoas = dict(tuplas_combinadas)

print(dicionario_persoas) # Imprime: {'Alice': 25, 'Bob': 30, 'Charlie': 35}
```

Neste exemplo, `zip(nomes, idades)` crea unha secuencia de tuplas onde cada tupla contén un nome e a súa correspondente idade. Despois, `dict(tuplas_combinadas)` converte esa secuencia de tuplas nun dicionario.

É importante ter en conta que si as lonxitudes dos iterables proporcionados a `zip()` non son iguais, a lonxitude do resultado estará determinada polo iterable máis curto. Os elementos adicionais nos iterables máis longos ignoraranse.

## 9.1.6. Dict Comprehension

***Dict Comprehension*** é unha construción sintática que permite crear diccionarios de xeito conciso e eficiente nunha única liña de código. E similar a *List Comprehension*, pero creando dicionarios en lugar de listas.

A estrutura xeral dun *Dict Comprehension* é a siguente:

```python
{nova_clave: novo_valor for elemento in iterable}
```

- `nova_clave`: a expresión determina a clave do nuevo par clave-valor.

- `novo_valor`: a expresión que determina o valor asociado a clave.

- `elemento`: variable que toma os valores do iterable.

- `iterable`: a secuencia sobre a cal se está iterando.

Exemplos:

- Crear un dicionario de cadrados de números

    ```python
    cadrados = {numero: numero**2 for numero in range(1, 6)}
    print(cadrados) # Imprime: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    ```



