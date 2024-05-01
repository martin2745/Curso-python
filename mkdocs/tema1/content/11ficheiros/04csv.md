---
title: "11.4. Ficheiros CSV"
weight: 4
---


Supoñamos que timos un arquivo CSV chamado `datos.csv` co seguinte contido:

```csv
nome,idade,cidade
Manuel,35,Santiago
Laura,34,Arzúa
Antía,22,A Coruña
```

### 11.3.1. Ler un ficheiro CSV

Podemos ler un ficheiro `csv` do seguinte xeito:

```python
# Abreimos o ficheiro en modo lectura
with open('datos.csv', 'r') as arquivo_csv:
    
    # Lemos todas as linhas do ficheiro
    # Isto devolve unha lista de str
    linhas = arquivo_csv.readlines()
    
    # Iteramos sobre as linhas
    for linha in linhas:
        # Eliminamos os caracteres de nova liña ao final desta
        linha = linha.strip()
        
        # Divide a liña nunha lista de cadeas a partir do separador que se pasa como argumento
        # Neste caso o delimitador é a coma
        lista_de_valores = linha.split(',')
        
        # Imprimimos unha fila do ficheiro como unha lista de str
        print(lista_de_valores)
```

### 11.3.2. Ler un ficheiro CSV obviando a cabeceira

Podemos obviar a primeira liña se esta contén unha liña que funciona como cabeceira:

```python
# Abreimos o ficheiro en modo lectura
with open('datos.csv', 'r') as arquivo_csv:
    
    # Lemos todas as linhas do ficheiro
    # Isto devolve unha lista de str
    linhas = arquivo_csv.readlines()

    # Salta a primeira linha
    linhas = linhas[1:]
    
    # Iteramos sobre as linhas
    for linha in linhas:
        # Eliminamos os caracteres de nova liña ao final desta
        linha = linha.strip()
        
        # Divide a liña nunha lista de cadeas a partir do separador que se pasa como argumento
        # Neste caso o delimitador é a coma
        lista_de_valores = linha.split(',')
        
        # Imprimimos unha fila do ficheiro como unha lista de str
        print(lista_de_valores)
```

### 11.3.3. Ler un ficheiro CSV coa librería csv

Podemos ler un ficheiro `csv` coa librería do mesmo nome:

```python
# Importamos a librería
import csv

# Abre o ficheiro CSV en modo lectura
with open('datos.csv') as arquivo_csv:
    # Crea un obxecto lector de CSV
    lector_csv = csv.reader(arquivo_csv)
    
    # Recorremos cada fila do ficheiro
    for fila in lector_csv:
        # Imprimimos cada fila que é unha lista de str
        print(fila)
```

Se en vez do método `reader()` utilizamos `DictReader()` cada fila en lugar dunha lista de cadeas será un dicionario, onde as claves son os nomes das columnas.

```python
# Importamos a librería
import csv

# Abre o ficheiro CSV en modo lectura
with open('datos.csv') as arquivo_csv:
    # Crea un obxecto lector de CSV
    lector_csv = csv.DictReader(arquivo_csv)
    
    # Recorremos cada fila do ficheiro
    for fila in lector_csv:
        # Acceder a unha columna especifica da fila polo nome da columna
        print(fila['nome'])
```


### 11.3.4. Escribir un ficheiro CSV

Escribimos nun ficheiro CSV como se fora un ficheiro de texto:

```python
# Datos a escribir no ficheiro
datos = [
    ['nome', 'idade', 'cidade'],
    ['Manuel', 35, 'Santiago'],
    ['Laura', 34, 'Arzúa']
]

# Abre o arquivo en modo escritura
with open('datos.csv', 'w') as arquivo_csv:
    
    # Escribe as filas de datos incluida a cabeceira
    for fila in datos[1:]:
        # Creamos unha cadea de caracteres por cada fila cos datos correspondentes
        fila_str = ""
        for dato in fila:
            fila_str += str(dato) + ","
        # Eliminamos a ultima coma
        fila_str = fila_str[:-1]

        # Escribimos a fila no ficheiro e engadimos unha nova liña
        arquivo_csv.write(fila_str + '\n')
```

### 11.3.5. Escribir un ficheiro CSV coa librería csv

O exemplo anterior utilizando a librería `csv` simplifícase de xeito significativo.


```python
import csv

# Datos a escribir no ficheiro
datos = [
    ['nome', 'idade', 'cidade'],
    ['Manuel', 35, 'Santiago'],
    ['Laura', 34, 'Arzúa']
]

# Abre o arquivo en modo escritura
with open('datos.csv', 'w') as arquivo_csv::
    
    # Crea un obxecto escritor de CSV
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escribe os datos no ficheiro CSV
    for fila in datos:
        escritor_csv.writerow(fila)
```

Tamén existe a clase `DictWriter` que se utiliza para escribir ficheiros CSV a partir de dicionario.

```python
import csv

# Datos en forma de lista de dicionarios
datos = [
    {'nome': 'Juan', 'idade': 25, 'cidade': 'Madrid'},
    {'nome': 'María', 'idade': 30, 'cidade': 'Barcelona'},
    {'nome': 'Pedro', 'idade': 35, 'cidade': 'Valencia'}
]

# Nomes das columnas do CSV
nomes_columnas = ['nome', 'idade', 'cidade']

# Abrimolo arquivo
with open('datos.csv', 'w', newline='') as arquivo_csv:
    # Crea o escritor DictWriter especificando o arquivo CSV e os nomes das columnas
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=nomes_columnas)

    # Escribimos a primeira columna
    escritor_csv.writeheader()

    # Escribimos os datos dende un dicionario
    for fila in datos:
        escritor_csv.writerow(fila)
```
