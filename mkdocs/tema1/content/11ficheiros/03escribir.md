---
title: "11.3. Escribir nun ficheiro"
weight: 3
---

Para escribir nun arquivo en Python, podemos utilizar a función `open()` en modo de escritura (`'w'`) para abrir o ficheiro.

A continuación utilízase o método `write()` para escribir texto no ficheiro. Cada chamada a `write()` agrega contido ao final do ficheiro.

Exemplo:

```python
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write('Ola, mundo!\n')
    arquivo.write('Este é un exemplo de escritura nun arquivo.')
```

O resultado deste código sería un arquivo de nome `arquivo.txt` co seguinte contido:

```
Ola, mundo!
Este é un exemplo de escritura nun arquivo.
```