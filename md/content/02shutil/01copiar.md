---
title: "2.1. Realizar copias"
weight: 1
---

A función `copy(orixe, destino)` utilízase para copiar un arquivo dende a localización de orixe a a localización destino. Se o ficheiro destino existe será substituído.
localización
Esta copia o contido do arquivo, pero non copia nin os permisos de arquivo nin os tempos de modificación. Se queremos manter estes metadatos debemos de utilizar a función `copy2(orixe, destino)`.

```python
import shutil

src_file = 'arquivo_orixe.txt'
dst_file = 'arquivo-destino.txt'

shutil.copy(src_file, dst_file)
```

### 2.1.1. Copia recursiva

A función `shutil.copytree(src, dst)` utilizase para copiar todo unha árbore de directorios, incluídos tódolos arquivos e subdirectorios. É moi útil cando se quere copiar un directorio completo xunto o seu contido.

```python
import shutil

src_dir = 'directorio_orixe'
dst_dir = 'directorio_destino'

shutil.copytree(src_dir, dst_dir)
```