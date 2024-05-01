---
title: "6.2. Tamaño dunha cadea"
weight: 2
---

`len` é unha función nativa que devolve o número de caracteres dunha cadea:

```python
froita = 'banana'
len(froita) # Imprime: 6
```

Para obter a última letra dunha cadea, poderías estar tentado a probar algo como isto:

```python
tamanho = len(froita)
ultima = froita[tamanho] # IndexError: string index out of range
```

A razón de que haxa un **IndexError** é que aí non hai ningunha letra en "banana" co índice 6. Posto que comezamos a contar dende cero, as seis letras están enumeradas dende 0 ata 5. para obter o último carácter, tes que restar 1 a **tamanho**.

```python
ultima = froita[tamanho-1]
print(ultima) # Imrpime: a
```

Alternativamente, podes usar índices negativos, os cales contan cara atrás dende o final da cadea. A expresión `froita[-1]` devolve a última letra, `froita[-2]` a penúltima letra, e así sucesivamente.

