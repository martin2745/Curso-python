---
title: "13.5. Substituír coincidencias dun patrón"
weight: 5
---

Podemos utilizar a función `re.sub()` para substituír tódalas ocorrencias dun patrón por outro nunha cadea.

Devolve unha nova cadea de texto onde tódalas ocorrencias do patrón foi sido substituida pola cadea de reemprazo. Se o patrón non se atopa, devolve a cadea orixinal sen modificacións.

```python
cadea = "Python é unha linguaxe de programación"
patron = "linguaxe"
reemprazo = "lingua"

nova_cadea = re.sub(patron, reemprazo, cadea)
print("Nova cadea:", nova_cadea)
```

Os argumentos son os seguintes:

- `patrón`: O patrón de expresión regular que desexas buscar na cadea de texto.

- `reemprazo`: A cadea que desexas utilizar para reemprazar as coincidencias encontradas.

- `cadea`: A cadea de texto na que desexas buscar e reemprazar o patrón.
  
- `conteo` (opcional): Un argumento opcional que indica o número máximo de ocorrencias a reemprazar. Se se omite, reemplazaranse tódalas ocorrencias encontradas.

### 13.5.1. Exemplo

Queremos remprazar tódalas vogais dun texto por un guión.


```python
import re

# Texto de entrada
texto = "Este é un exemplo de cómo reemprazar vogais nun texto."

# Patrón para buscar vogais no texto
patron_vogais = r'[aeiouAEIOU]'

# Reemprazar tódalas vogais con guións
texto_modificado = re.sub(patron_vogais, '-', texto)

# Imprimir o texto modificado
print("Texto modificado:")
print(texto_modificado)
```