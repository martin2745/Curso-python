---
title: "1.6. Traballar con directorios e ficheiros"
weight: 6
---

### 1.6.1. Cambiar permisos

A función `os.chmod(path, mode)` utilízase para cambiar os permisos de acceso dun arquivo ou un directorio en **sistemas Unix**. O primeiro argumento é a ruta do ficheiro ou directorio e o segundo son os permisos que se lle aplicarán. Pode especificarse en formato octal ou utilizando constantes do módulo `stat`.

```python
import os

# Establecer permisos 744 para o arquivo
os.chmod("arquivo.txt", 0o744)
```

Neste exemplo establécense os permisos de arquivo 744.

Neste outro exemplo utilízanse constantes do módulo `stat`: 

```python
import os
import stat

# Establecer permisos de só lectura para o propietario e o grupo
os.chmod("arquivo.txt", stat.S_IRUSR | stat.S_IRGRP)

# Establecer permisos de lectura, escritura e execución para o propietario
os.chmod("arquivo.txt", stat.S_IRWXU)
```

Algunhas das constantes máis comúns do módulo `stat` son:

- `stat.S_IRUSR`: Permiso de lectura para o propietario do arquivo.
- 
- `stat.S_IWUSR`: Permiso de escritura para o propietario do arquivo.
- 
- `stat.S_IXUSR`: Permiso de execución para o propietario do arquivo.
- 
- `stat.S_IRGRP`: Permiso de lectura para o grupo do arquivo.
- 
- `stat.S_IWGRP`: Permiso de escritura para o grupo do arquivo.
- 
- `stat.S_IXGRP`: Permiso de execución para o grupo do arquivo.
- 
- `stat.S_IROTH`: Permiso de lectura para outros usuarios.
- 
- `stat.S_IWOTH`: Permiso de escritura para outros usuarios.
- 
- `stat.S_IXOTH`: Permiso de execución para outros usuarios.

### 1.6.2. Cambiar propietario

A función `os.chown(path, uid, gid)` utilízase para **cambiar o propietario e o grupo dun arquivo ou directorio en sistemas tipo Unix**.

Os argumentos que reciben son:

- `path`: A ruta do arquivo ou directorio.

- `uid`: O identificador numérico do novo propietario.

- `gid`: O identificador numérico do novo grupo.


```python
import os

# Cambiar O propietario e o grupo do arquivo
os.chown("arquivo.txt", 1000, 1000)
```

### 1.6.3. Cambiar de nome

A función `os.rename(src, dst)` utilízase para cambiar o nome dun arquivo ou directorio. Se non existe o directorio prodúcese un erro.

```python
import os

# Cambiar o nome do arquivo "antigo_nome.txt" a "novo_nome.txt"
os.rename("antigo_nome.txt", "novo_nome.txt")
```



