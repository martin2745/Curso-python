---
title: "3.2. Obxecto POPEN"
weight: 2
---

Tamén se pode utilizar a función `subprocess.Popen()` para executar comandos. Este proporciona maior control sobre o proceso. Este e especialmente útil se é necesario interactuar co proceso ou se este se necesita executar en segundo plano.

```python
import subprocess

# Comando a executar
comando = ["ls", "-l"]

# Crea un obxecto Popen para executar o comando
proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Obtense a saida e erros do proceso
saida, erros = proceso.communicate()

# Imprimir la salida y errores
print("Saida do comando:")
print(saida)

print("\nErros do comando:")
print(erros)
```

Os argumentos `stdout=subprocess.PIPE` y `stderr=subprocess.PIPE` utilízanse para obter a saída e os erros dos procesos.

### 3.2.1. Interactividade co comando

A función `subprocess.Popen()` xunto coa redirección da entrada/saída estándar do proceso para enviar respostas dende un *script* de Python. 

Aquí un exemplo de como agregar un usuario nun sistema Linux utilizando o comando `adduser`:

```python
import subprocess

# Solicitar ao usuario o nome do novo usuario
novo_usuario = input("Ingrese o nome do novo usuario: ")

# Comando para agregar un usuario
comando = ["sudo", "adduser", novo_usuario]

# Crea un obxecto Popen para executar o comando
proceso = subprocess.Popen(comando, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Pide ao usuario que ingrese o contrasinal para o novo usuario
contrasinal = input(f"Ingrese o contrasinal para o usuario {novo_usuario}: ")

# Enviamos o contrasinal ao proceso
proceso.stdin.write(novo_usuario + '\n')
# Aseguramos de que a entrada se envía correctamente
proceso.stdin.flush() 

# Obtén a salída e os erros do proceso
saida, erros = proceso.communicate()

# Cerra a entrada estándar do proceso
proceso.stdin.close()

# Imprimir la salida y errores
print("Salida del proceso:")
print(saida)

print("\nErrores del proceso:")
print(erros)
```

