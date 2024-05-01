---
title: "10.4. Recoller datos de parámetros do script"
weight: 4
---

En Python para recoller os datos pasados por parámetro ao *script* necesítase utilizar o módulo `sys`.

Este módulo contén un atributo `argv` que é unha lista na que o primeiro elemento é o nome do *script*, e os seguintes son os argumentos que se pasaron ao *script*. Exemplo:

```python
import sys

# Exemplo de execucion: "python3 script.py argumento1 argumento2"
# Collemos o primeiro argumento
argumento1 = sys.argv[1]
# Collemos o segundo argumento
argumento2 = sys.argv[2]

# Imprimimos os argumentos
print("Argumento 1:", argumento1)
print("Argumento 2:", argumento2)
```