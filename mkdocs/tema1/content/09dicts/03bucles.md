---
title: "9.3. Recorrer dicionarios"
weight: 3
---

## 9.3.1. Iterar sobre claves

Se utilizas un dicionario como unha secuencia para unha sentencia `for`, esta recorre as chaves do dicionario. Este bucle imprime cada chave e o seu valor correspondente:

```python
contadores = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for clave in contadores:
	print(clave, contadores[clave])
```

Isto imprime:

```bash
jan 100
chuck 1
annie 42
```

De novo, as chaves non están en ningunha orde en particular. O bucle `for` itera a través das chaves do dicionario, así que debemos utilizar o operador índice para obter o valor correspondente para cada chave.


## 9.3.2. Iterar sobre pares clave-valor

Utilizando o método `ìtems()`podemos iterar o dicionario obtendo para cada clave o seu valor.

```python
dicionario = {'a': 1, 'b': 2, 'c': 3}

for clave, valor in dicionario.items():
    print(clave, valor)
```

## 9.3.3. Iterar sobre valores

Utilizando o método `values()` obtemos unha lista cos valores do dicionario. Podemos iterar sobre esta lista ca cláusula `for`:

```python
dicionario = {'a': 1, 'b': 2, 'c': 3}

for valor in dicionario.values():
    print(valor)
```