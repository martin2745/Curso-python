---
title: "11.2. Ler un ficheiro"
weight: 2
---

Para ler arquivos en Python, podemos utilizar varios métodos proporcionados polo obxecto devolto pola función `open()`. Aquí tes os máis comúns:


1. **read()**: Le e devolve o contido completo do arquivo como unha cadea.

```python
with open('arquivo.txt', 'r') as arquivo:
    contido = arquivo.read()
```

2. **readline()**: Le e devolve a próxima liña do arquivo como unha cadea.

```python
with open('arquivo.txt', 'r') as arquivo:
    linha = arquivo.readline()
```

3. **readlines()**: Le e devolve tódalas liñas do arquivo como unha lista de cadeas.

```python
with open('arquivo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
```

4. **for loop**: Podes iterar sobre as liñas do arquivo utilizando un bucle `for`. Isto é útil se queres procesar o arquivo liña por liña.

```python
with open('arquivo.txt', 'r') as arquivo:
    for linha in archivo:
        print(linha)
```