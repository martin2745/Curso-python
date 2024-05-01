---
title: "1.8. Traballar con ficheiros"
weight: 8
---

### 1.8.1. Eliminar ficheiros

A función `os.remove(path)` elimina un ficheiro do sistema de ficheiros. Se non existe o ficheiro prodúcese unha excepción.

```python
import os

# Eliminar o arquivo "arquivo.txt"
os.remove("arquivo.txt")
```

 