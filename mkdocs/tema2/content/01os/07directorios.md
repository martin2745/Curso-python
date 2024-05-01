---
title: "1.7. Traballar con directorios"
weight: 7
---

### 1.7.1. Cambiar directorio de traballo

A función `os.chdir(ruta)` cambia o directorio de traballo do *script*. se a ruta non existe ou non ten permisos produce unha excepción. Esta función é equivalente a `cd` en Bash e `Set-Location` en PowerShell.

Por outro lado, a función `os.getcwd()` devolve o directorio de traballo do *script*. Esta función é equivalente a `pwd` en Bash e `Get-Location` en PowerShell.

```python
import os

# Cambiar o directorio de traballo a "directorio"
os.chdir("directorio")

# Verificar o cambio de directorio de traballo
print("Directorio actual:", os.getcwd())
```

### 1.7.2. Listar directorio

`os.listdir(ruta)` utilízase para obter unha lista de nomes de arquivos e directorios dunha ruta especificada. Se non se proporciona ningunha ruta, devolve a lista de arquivos do directorio actual.

```python
import os

# Obter unha lista de nomes de arquivos e directorios no directorio actual
arquivos = os.listdir()
print("Arquivos no directorio actual:", arquivos)

# Obtener unha lista de nomes de arquivos e directorios nunha ruta específica
ruta = os.path.join("ruta","de","proba")
print("Arquivos noutro directorio:", ruta)
```

Podemos combinar esta función con `os.path.isfile(path)` e `os.path.isdir(path)` para diferenciar entre directorios e ficheiros.

Esta función é similar en Bash a `ls` e en PowerShell a `Get-ChildItem` e os seus alias `dir` e `ls`.


### 1.7.3. Listar directorio e subidrectorios

A función `os.walk(path)` utilízase para recorrer directorios de xeito recursivo. Permite iterar sobre un directorio e os seus subdirectorios.

Esta función devolve un xerador que produce tuplas de tres elementos en cada iteración. Estes elementos son:

- O nome do directorio actual que está sendo examinado.

- Unha lista de nomes de subdirectorios dentro do directorio actual.

- Unha lista de nomes de arquivos dentro do directorio actual.

```python
import os

for directorio_actual, subdirectorios, arquivos in os.walk(directorio):
    pass
```


### 1.7.4. Crear directorio

A función `os.mkdir(path)` utilízase para crear un novo directorio. O argumento que recibe é a ruta do directorio a crear.

```python
import os

# Crea un novo directorio chamado "novo_directorio"
os.mkdir("novo_directorio")
```

A función `os.makedirs(ruta)` utilízase para crear un directorio e todos os seus directorio pais se non existen. Similar a `mkdir -p ruta` en Bash.

```python
import os

# Crear un novo directorio xunto cos directorios parentais
os.makedirs("novo_directorio/novo_subdirectorio")
```

### 1.7.5. Eliminar directorio

A función `os.rmdir()` utilízase para eliminar un directorio **baleiro**. Se non está baleiro prodúcese unha excepción.

```python
import os

# Elimina o directorio "directorio_baleiro"
os.rmdir("directorio_baleiro")
```