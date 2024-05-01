---
title: "6.1. Comandos bash"
weight: 1
---

### 6.1.1. Comando grep

**Utilizando expresións regulares**

```python
import re

patron = r"patron_a_buscar"

with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        if re.search(patron, linea):
            print(linea)
```

**Iterando sobre as liñas do arquivo:**

```python
patron = "patron_a_buscar"

with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        if patron in linea:
            print(linea)
```

### 6.1.2. Sed

```bash
sed 's/patron_a_reemplazar/nuevo_texto/g' archivo.txt
```

```python
import re

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()

contenido_modificado = re.sub(r"patron_a_reemplazar", "nuevo_texto", contenido)

with open("archivo.txt", "w") as archivo:
    archivo.write(contenido_modificado)
```

### 6.1.3. awk

- **Imprimir campos específicos de cada liña:**

```bash
awk '{print $1, $3}' arquivo.txt
```

```python
with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        campos = linha.split()
        print(campos[0], campos[2])
```

- **Filtrar liñas que coinciden cun patrón:**

```bash
awk '/patron/ {print}' arquivo.txt
```

```python
with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        if "patron" in linha:
            print(linea, end="")
```

- **Calcular a suma dunha columna numérica:**

```bash
awk '{suma += $1} END {print suma}' arquivo.txt
```

```python
suma = 0
with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        campos = linha.split()
        suma += int(campos[0])
print(suma)
```

### 6.1.4. find

*1. **Buscar arquivos por nome:**

```bash
find /ruta/ao/directorio -name "patron"
```

```python
import os

directorio = "/ruta/ao/directorio"
patron = "patron"

for raiz, subdirectorios, arquivos in os.walk(directorio):
    for arquivo in arquivos:
        if patron in arquivo:
            print(os.path.join(raiz, arquivo))
```

- **Buscar arquivos**

```bash
find /ruta/ao/directorio -type f
```

```python
import os

directorio = "/ruta/ao/directorio"

for raiz, subdirectorios, arquivos in os.walk(directorio):
    for arquivo in arquivos:
        ruta_completa = os.path.join(raiz, arquivo)
        if os.path.isfile(ruta_completa):
            print(ruta_completa)
```

- **Buscar arquivos por tamaño:**

```bash
find /ruta/ao/directorio -size +10M
```

```python
import os

directorio = "/ruta/ao/directorio"
tamano_limite = 10 * 1024 * 1024  # Tamaño en bytes

for raiz, subdirectorios, arquivos in os.walk(directorio):
    for arquivo in arquivos:
        ruta_completa = os.path.join(raiz, arquivo)
        if os.path.getsize(ruta_completa) > tamano_limite:
            print(ruta_completa)
```