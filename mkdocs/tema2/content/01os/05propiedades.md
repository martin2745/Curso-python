---
title: "1.5. Propiedades sistema de ficheiros"
weight: 5
---

### 1.5.1. Obter data de modificación do ficheiro

A función `os.path.getmtime(path)` utilízase para obter a data de modificación dun arquivo ou directorio en forma de *timestamp*.

Con `datetime.fromtimestamp()` podemos converter ese valor a un obxecto `datetime`.

```python
import os
from datetime import datetime

ruta_arquivo = 'arquivo.txt'

data_modificacion = os.path.getmtime(ruta_arquivo)

data_modificacion_dt = datetime.fromtimestamp(data_modificacion)
```

Para obter a fecha de creación en Windows podémolo facer con `os.path.getctime()`. En sistemas Linux ou macOS a data de creación non está directamente dispoñible, pero podemos utilizar `os.path.getmtime()` como un substituto aproximado para a data de creación.

### 1.5.2. Obter tamaño

A función `os.path.getsize(path)` utilízase para obter o **tamaño en bytes** dun ficheiro.

```python
import os

ruta_arquivo = 'archivo.txt'

tamano_arquivo_bytes = os.path.getsize(ruta_arquivo)
```

Se se lle pasa a **ruta dun directorio**, obterase o tamaño de tódolos ficheiros de ese directorio e de tódolos seus directorios de xeito recursivo.

### 1.5.3. Obter propiedades

Para obter as propiedades dun ficheiro ou directorio podemos utilizar a función `os.stat(path)`. Este devolve un obxecto de tipo `os.stat_result`.


```python
import os

info_archivo = os.stat('arquivo.txt')

print(info_arquivo)

tamaño_arquivo = info_archivo.st_size
print(f"Tamaño do arquivo: {tamaño_archivo} bytes")

permisos_arquivo = info_arquivo.st_mode
print(f"Permisos do arquivo en octal: {oct(permisos_archivo)}")
```

O obxecto `os.stat_result` conta cas seguintes propiedades.

- `st_mode`: Permisos del arquivo ou directorio.

- `st_uid`: O UID do usuario propietario do arquivo ou directorio.

- `st_gid`: O GID do grupo propietario do arquivo ou directorio.

- `st_size`: O tamaño en bytes do arquivo.

- `st_atime`: O tempo de último acceso del arquivo (en timestamp).

- `st_mtime`: O tempo de última modificación del arquivo (en timestamp).
