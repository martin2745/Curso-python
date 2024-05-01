---
title: "13.4. Encontrar tódalas coincidencias dun patrón"
weight: 4
---

Podemos utilizar a función `re.findall()` para encontrar tódalas ocorrencias dun patrón nunha cadea.

Devolve unha lista con tódalas coincidencias atopadas na orde na aparecen no texto. Se non hai ningunha coincidencia devolve unha lista baleira.

Se o patrón contén grupos de captura, `re.findall()` devolverá unha lista de tuplas onde cada tupla contén os grupos de captura de cada coincidencia.

```python
cadea = "O patrón do patrón es patrónico"
patron = "patrón"

resultado = re.findall(patron, cadea)
print("Coincidencias:", resultado)
```

Os argumentos da función son os seguintes:

- `patrón`: É o patrón de expresión regular que desexas buscar na cadea de texto.

- `cadea`: A cadea de texto na que desexas buscar o patrón.

## 13.4.1. Exemplo

Supoñamos que queremos encontrar tódalas direccións de correo electrónico nun texto.


```python
import re

# Cadema de texto a buscar
texto = "As miñas direccións de correo electrónico son usuario1@example.com e usuario2@example.com."

# Patrón para buscar emails
patron_correo = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Buscamos todas as ocurrencias
direcciones_encontradas = re.findall(patron_correo, texto)

# Recorremos tódolos emails encontrados na cadea 
for direccion in direcciones_encontradas:
    print(direccion)
```