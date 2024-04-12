---
title: "2.2. Eliminar"
weight: 2
---

A función `shutil.rmtree(directorio)` utilízase para eliminar un directorio e todo o seu contido de xeito recursivo. É dicir, elimina o directorio especificado e tódolos arquivos e directorios que contén.

```python
import shutil

directorio_a_eliminar = 'directorio_a_eliminar'

shutil.rmtree(directorio_a_eliminar)
```