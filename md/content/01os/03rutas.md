---
title: "1.3. Rutas sistema de ficheiros"
weight: 3
---

### 1.3.1. Compoñer rutas

A función `os.path.join(dir1, dir2, dir3,...)` utilizase para unir un ou máis compoñentes dunha ruta de xeito seguro utilizando o separador de ruta apropiado para o sistema operativo no que se executa o *script*. Isto é útil para construír rutas de arquivos ou directorios e xeito que sexan portables entre diferentes sistemas operativos. 

Esta función toma como argumentos os elementos da ruta que se van a unir.

```python
import os

# Unir elementos de ruta para formar unha ruta completa
ruta_completa = os.path.join("directorio", "subdirectorio", "arquivo.txt")
print("Ruta completa:", ruta_completa)
```

Este código imprimirá "Ruta completa: directorio/subdirectorio/arquivo.txt" en sistemas Unix e "Ruta completa: directorio\subdirectorio\arquivo.txt" en Windows.

### 1.3.2. Obter nome de ficheiro

A función `os.path.basename(ruta)` utilízase para obter o nome dun ficheiro ou directorio a partir dunha ruta. Por exemplo se temos a ruta  "/home/usuario/arquivo.txt" esta función devolverá "arquivo.txt".

```python
import os

ruta = "/home/usuario/arquivo.txt"

nome_arquivo = os.path.basename(ruta)

print("Nome do arquivo:", nome_arquivo)
```

### 1.3.3. Obter directorio contedor

A función `os.path.dirname(ruta)` utilízase para obter un directorio pai dunha ruta de arquivo.

```python
import os

ruta = "/home/usuario/arquivo.txt"

directorio_pai = os.path.dirname(ruta)

print("Directorio pai:", directorio_pai) # Imprime "/home/usuario"
```

### 1.3.4. Obter ruta absoluta

A función `os.path.abspath(ruta)` utilízase para obter a ruta absoluta correspondente a unha ruta relativa.

```python
import os

ruta_relativa = "arquivos/datos.txt"

ruta_absoluta = os.path.abspath(ruta_relativa)

print("Ruta absoluta:", ruta_absoluta) # imprime por exemplo /home/usuario/arquivos/datos.txt
```

 