---
title: "2.3. Mover"
weight: 3
---

A función `shutil.move(src, dst)` utilízase para mover arquivos ou directorios dunha localización noutra.

```python
import shutil

arquivo_a_mover = 'arquivo_a_mover.txt'

nova_ubicacion = 'nova_ubicacion/arquivo_a_mover.txt'

shutil.move(arquivo_a_mover, nova_ubicacion)
```