---
title: "11.5. Ficheiros JSON"
weight: 5
---

Supoñamos o seguinte ficheiro en formato JSON `datos.json`:

```json
{
  "nome": "Manuel",
  "idade": 35,
  "cidade": "Santiago"
}
```

### 11.5.1. Ler ficheiros JSON

Podemos ler este ficheiro do seguinte xeito en transformalo nun `dict`:


```python
# Importamos a librería json
import json

# Abre o ficheiro en modo lectura
with open('datos.json', 'r') as arquivo_json:
    # Carga os datos do ficheiro JSON nun dicionario
    datos = json.load(arquivo_json)

# Accede aos datos cargados
print(datos["nome"])  # Imprimirá "Manuel"
print(datos["idade"])    # Imprimirá 35
print(datos["cidade"])  # Imprimirá "Santiago"
```

### 11.5.2. Diferencia entre load() e loads()

A diferencia entre `json.load()` e `json.loads()` radica no tipo de entrada que cada unha acepta:

- `json.load()`: Utilízase para cargar datos dende un ficheiro aberto.

- `json.loads()`: Utilízase para cargar datos dende unha cadea.

O exemplo anterior utilizando a función `json.loads()`:


```python
# Importamos a librería json
import json

# Abre o ficheiro en modo lectura
with open('datos.json', 'r') as arquivo_json:
    # Lemos o contido do ficheiro nunha cadea de texto
    contido = arquivo_json.read()

# Transformamos a cadea de texto nun dicionario
datos = json.loads(contido)

# Accede aos datos cargados
print(datos["nome"])  # Imprimirá "Manuel"
print(datos["idade"])    # Imprimirá 35
print(datos["cidade"])  # Imprimirá "Santiago"
```

### 11.5.3. Escribir un ficheiro JSON

Podes escribir un arquivo JSON en Python utilizando a biblioteca estándar `json`. Aquí tes un exemplo básico de como facelo:

```python
# Importamos a librería
import json

# Dicionario a escribir no ficheiro
datos = {
    "nome": "Manuel",
    "idade": 35,
    "cidade": "Santiago"
}

# Abre o ficheiro en modo escritura
with open('datos.json', 'w') as arquivo_json:
    # Escribimos o dicionario como un JSON no ficheiro
    json.dump(datos, arquivo_json)
```

### 11.5.4. Diferencia entre dump() e dumps()

A diferencia principal entre `json.dump()` e `json.dumps()` radica no tipo de saída que xeran:

- `json.dump()`: Esta función utilízase para escribir datos JSON nun arquivo aberto en modo escritura.

- `json.dumps()`: Esta función utilízase para converter un dicionario nunha cadea en formato JSON.

O exemplo anterior utilizando `json.dumps()`:

```python
# Importamos a librería
import json

# Dicionario a escribir no ficheiro
datos = {
    "nome": "Manuel",
    "idade": 35,
    "cidade": "Santiago"
}

# Transformamos o dicionario nunha cadea en formato JSON
dict_str = json.dumps(datos)

# Abre o ficheiro en modo escritura
with open('datos.json', 'w') as arquivo_json:
    # Escribimos unha cadea de texto nun ficheiro
    jrquivo_json.write(dict_str)
```