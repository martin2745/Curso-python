---
title: "10.1. Definir e importar un módulo"
weight: 1
---

### 10.1.1. Definir un módulo

Para crear un módulo de nome `o_meu_modulo` tan só debemos definir un ficheiro de nome `o_meu_modulo.py`. Dentro deste definir funcións e declarar variables:

```python
# o_meu_modulo.py

pi = 3.14
def saudar(nome):
    print("Ola", nome)
```

### 10.1.2. Importar un módulo

Pódese importar **todo un módulo** utilizando a palabra clave `import` seguida do nome do módulo. Por exemplo:


```python
import o_meu_modulo
```

Isto importará todo o contido do módulo `o_meu_modulo`. A partir de aí poderase acceder as funcións e variables definidas nese módulo.

### 10.1.3. Utilizar funcións ou variables dun módulo

Para acceder por exemplo a unha función dun módulo debemos seguir a seguinte sintaxe: `nome_do_modulo.funcion()`.

Por exemplo:

```python
import o_meu_modulo

o_meu_modulo.saudar("Manuel")
```

Para acceder por exemplo a unha variable dun módulo debemos seguir a seguinte sintaxe: `nome_do_modulo.variable`.

Por exemplo:

```python
import o_meu_modulo

print(o_meu_modulo.pi)
```

### 10.1.4. Importar un módulo dun subdirectorio

Para importar un módulo que está nun subdirectorio en Python, podemos utilizar a notación de punto `.` para indicar a ubicación relativa do módulo en relación co arquivo dende o que se está importando. Supoñamos a seguinte estrutura:


```
o_meu_proxecto/
│
├── subdirectorio/
│   └── o_meu_modulo.py
│
└── main.py
```

Para importar `o_meu_modulo.py` dende `main.py` debemos:

```python
from subdirectorio import o_meu_modulo
```

