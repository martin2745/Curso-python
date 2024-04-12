---
title: "1.2. Variables de contorno"
weight: 2
---

Para acceder a variables de contorno podemos utilizar a función `os.getenv(variable)`. Esta función recibe como argumento unha cadea de caracteres co nome da variable de contorno da que se desexa obter o valor. Se a variable non existe, devolverase o valor `None`.

```python
import os

# Obter o valor da variable de contorno PATH
valor_path = os.getenv("PATH")

print("Valor da variable de contorno PATH:", valor_path)
```

### 1.2.1. Engadir variables de contorno

Para crear unha variable de contorno en Python podemos utilizar a función `os.putenv(variable, valor)`. Esta recibe como primeiro parámetro o valor da variable de contorno e como segundo argumento o valor que se lle desexa asignar.


```python
import os

# Establecer unha variable de contorno chamada "VARIABLE_ PROBA"
os.putenv("VARIABLE_ PROBA", "valor_de_proba")

# Verificar que la variable de entorno se ha establecido correctamente
print("Variable de contorno VARIABLE_ PROBA establecida:", os.getenv("VARIABLE_ PROBA"))
```