---
title: "11.1. Abrir e cerrar un ficheiro"
weight: 1
---

Para abrir un ficheiro debemos utilizar a función de Python `open()`. Deberemos pasarlle como parámetros a ruta do ficheiro e o modo utilizado. Esta función devolve un obxecto que simboliza o ficheiro.

Por último é importante cerrar o arquivo utilizaremos o método `close()` do obxecto devolto. Isto permitirá liberar recursos e evitar posibles problemas de manexo de ficheiros.

No seguinte exemplo abrimos un ficheiro en modo lectura:


```python
# Abrimos o ficheiro en modo lectura
arquivo = open('arquivo.txt', 'r')

# Traballamos co ficheiro...

# Cerramos o ficheiro despois de lelo.
arquivo.close()
```

### 11.1.1. Utilizar a estrutura with

Podemos utilizar a estrutura `with`. Esta garante que o arquivo se cerre correctamente ao saír do bloque de código que abre dita estrutura. A función `open()` débese utilizar dentro da estrutura `with`. Exemplo:


```python
# Abrimos o ficheiro en modo lectura
with open('arquivo.txt', 'r') as arquivo:
    # Traballamos co ficheiro...

# Unha vez rematada a estrutura with o ficheiro cerrase automaticamente
```

### 11.1.2. Modos de apertura dun ficheiro

A función `open()` en Python permite abrir arquivos en diferentes modos de abrir ficheiros de texto. Aquí os máis comúns:

- **'r'**: Modo lectura. É o modo predeterminado se non se indica ningún modo.

- **'w'**: Modo de escritura. Se o arquivo xa existe, bórrase o contido anterior. Se non existe, créao.

- **'a'**: Modo de adición: O punteiro do arquivo posiciónase ao final do arquivo. e non existe, créao.


A continuación podemos ler o contido do ficheiro co método `read()`. Isto almacenará todo o contido nunha variable de tipo `str`.