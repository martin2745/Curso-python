---
title: "2.4. Compresión"
weight: 4
---

### 2.4.1. Comprimir

A función `shutil.make_archive(nome_comprimido, formato, dir_a_comprimir)` utilízase para crear un arquivo comprimido que contén todo o contido dun directorio, incluídos os seus subdirectorios e arquivos.

- `nome_comprimido`: o nome base do ficheiro comprimido (obviando a extensión).

- `formato`. o formato do arquivo. Estas son algunhas opcións: 'zip', 'tar', 'gztar', 'bztar', 'xztar'.

- `dir_a_comprimir`. Directorio que se incluirá no ficheiro comprimido. Se non se indica comprímese o directorio actual.

```python
import shutil

directorio_a_comprimir = 'directorio_a_comprimir'

shutil.make_archive('directorio_comprimido', 'zip', directorio_a_comprimir)
```

### 2.4.2. Descomprimir

Para descomprimir utilizamos a función `shutil.unpack_archive(arquivo_comprimido, directorio_saida)`. O directorio de saída é opcional, pódese omitir. Se se omiten os ficheiros descomprimiranse no directorio actual.

```python
import shutil

arquivo_comprimido = 'arquivo_comprimido.zip'

directorio_destino = 'directorio_destino'

shutil.unpack_archive(arquivo_comprimido, extract_dir=directorio_destino)
```



