---
title: "1.4. Comprobacións sistema de ficheiros"
weight: 4
---

### 1.4.1. Comprobar a existencia

A función  `os.path.exists(path)` utilízase para verificar se unha ruta existe nun sistema de arquivos. Devolve verdadeiro se existe e falso en caso contrario.

```python
import os

# Verificar se o arquivo "arquivo.txt" existe
if os.path.exists("arquivo.txt"):
    print("O arquivo existe.")
else:
    print("O arquivo non existe.")
```

### 1.4.2. Comprobar se é un ficheiro

Podemos utilizar a función `os.path.isfile(path)` para verificar se unha ruta dada é un arquivo. Esta función devolve verdadeiro en caso que así sexa e falso en caso contrario.

```python
import os

# Ruta do arquivo que se desexa verificar
ruta = "/ruta/al/arquivo.txt"

# Verificar si la ruta es un archivo
if os.path.isfile(ruta):
    print("A ruta corresponde é un archivo.")
else:
    print("A ruta non se corresponde cun archivo.")
```

### 1.4.3. Comprobar se é un directorio

Para verificar se unha ruta é un directorio podemos utilizar a función `os.path.isdir(path)`. Esta función devolve `True` en caso afirmativo e `False` en caso negativo.

```python
import os

# Ruta do directorio que se desexa verificar
ruta = "/ruta/ao/directorio"

# Verificar se a ruta é un directorio
if os.path.isdir(ruta):
    print("A ruta corresponde a un directorio.")
else:
    print("A ruta non corresponde a un directorio.")
```

### 1.4.4. Comprobar se é un enlace simbólico

A función `os.path.islink()` é unha función que determina se unha ruta é un enlace simbólico. Esta función devolve `True` en caso afirmativo e `False` en caso negativo.


```python
import os

ruta = "/ruta/enlace"

if os.path.islink(ruta):
    print(f"{ruta} e un enlace simbólico.")
else:
    print(f"{ruta} non e un enlace simbólico.")
```

