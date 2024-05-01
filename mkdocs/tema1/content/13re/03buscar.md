---
title: "13.3. Buscar un patrón"
weight: 3
---

Podemos utilizar a función `re.search()` para buscar un patrón nunha cadea. 

Devolve un obxecto `match` se encontra unha coincidencia, ou `None` en caso contrario.


```python
cadea = "Python é unha linguaxe de programación"
patron = "linguaxe"

resultado = re.search(patron, cadea)
if resultado:
    print("Encontrado:", resultado.group())
else:
    print("Non encontrado")
```

- `patrón`: É o patrón de expresión regular que desexas buscar na cadea de texto.

- `cadea`: A cadea de texto na que desexas buscar o patrón.

## 13.3.1. Obxecto match

Podes acceder a coincidencia encontrada utilizando métodos como `group()` o `groups()` do obxecto `match`devolto.

Se o patrón contén grupos de captura, podes acceder aos grupos individuais utilizando `group(n)` onde `n` é o índice do grupo de captura.

- **`group()`**: este método devolve a cadea de texto correspondente ca coincidencia ou un grupo de captura dentro da expresión regular. Se non se lle pasa ningún argumento devolve a cadea de texto completa da coincidencia. Se se lle pasa un número enteiro como argumento, devolve a cadea de texto correspondente ao grupo de captura con ese número.

- **`groups()`**: devolve unha tupla que contén tódalas cadeas de texto correspondentes aos grupos de captura dentro da expresión regular. Non ten argumentos. Se a expresión non ten grupos de captura, devolve unha tupla baleira.

## 13.3.2. Exemplo

Neste exemplo indicamos se na cadea se atopa un número de teléfono móbil.

```python
import re

# Texto de entrada
texto = "Mi número de teléfono es 612 345 678."

"""
Este patrón busca un número de teléfono que comeza por 6 (\b6), seguido de dous díxitos (\d{2}), logo un espazo, despois tres díxitos, a continuación outro espazo e por último outros 3 números.
O uso de \b asegura que o número de teléfono esté delimitado polo principio e fin dunha palabra.
A letra "r" antes dunha cadea en Python indica que é unha cadea sen formato. Isto indica que os caracteres de escape, como '\' se interpreten literalmente. Neste contexto, é moi útil porque simplifica o patrón. 
"""
patron = r'\b6\d{2} \d{3} \d{3}\b'

# Buscamos a coincidencia
coincidencia = re.search(patron, texto)

# Comprobamos se hai coincidencia
if coincidencia:
    numero_telefono = coincidencia.group()  # Obtemos a cadea da coincidencia
    print("Número de teléfono encontrado:", numero_telefono)
else:
    print("No se atopu ningún teléfono")
```

