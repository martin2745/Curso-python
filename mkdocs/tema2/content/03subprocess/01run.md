---
title: "3.1. Función run()"
weight: 1
---

Coa función `run` podemos executar procesos:

```python
import subprocess

# Executar un comando de Bash
resultado = subprocess.run(["ls", "-l"], capture_output=True, text=True)

# Imprimir a saida do comando
print("Saída do comando:")
print(resultado.stdout)
```

Este código executa o comando `ls -l`. Como vemos, a entrada do comando e unha lista cás diferentes partes do comando (o comando propiamente dito e as súas opcións). Por último imprime por consola.

O exemplo anterior executouse o comando en Bash. Podemos facelo mesmo en PowerShell:

```python
import subprocess

# Executar un comando de PowerShell
resultado = subprocess.run(["powershell", "-Command", "Get-ChildItem"], capture_output=True, text=True)

# Imprimir a saida do comando
print("Saida del comando:")
print(resultado.stdout)
```

O argumento `capture_output` utilízase para indicar se se debe capturar a saída estándar e de error do proceso secundario. Deste xeito podemos acceder a saída estándar no atributo `stdout` e a saída de erro no atributo `stderr`. Se se establece a `False` non se captura dita saída.

O argumento `text=True` utilízase para especificar que a entrada e saída do proceso secundario debe ser en formato texto en lugar de formato de bytes.

No seguinte exemplo proporcionamos unha función que obtén unha lista de arquivos en calquera dos dous sistemas operativos:

```python
import subprocess
import os

def ls():
    if os.name == 'nt':  # Windows
        comando = ['dir', '/B']
    elif os.name == 'posix':  # Linux o macOS
        comando = ['ls']
    else:
        print("Sistema operativo non compatible.")
        return None

    try:
        resultado = subprocess.run(comando, capture_output=True, text=True)
        lista = resultado.stdout.splitlines()
        return lista
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o comando:", e)
        return None
```