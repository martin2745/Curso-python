---
title: "12.1. Crear un decorador"
weight: 1
---

Os decoradores son útiles para agregar funcións como validación de datos, control de acceso, etc. de xeito modular e reutilizable.

A súa sintaxe é esta:

```python
# Función decoradora
def funcion_decoradora(funcion_a_decorar):
    # Estes son os argumentos da funcion a decorar, podemos utilizamos
    def funcion_a_executar(*args, **kwargs):
        
        # Código adicional antes de chamar a función
        # ...
        
        # Executamos a funcion a decorar
        resultado_da_funcion_a_decorar = funcion_a_decorar(*args, **kwargs)

        # Código adicional despois de chamar a función
        ...

        return resultado_da_funcion_a_decorar # Pode ser que a función a decorar non devolva nada, polo que se pode omitir
    return funcion_a_executar
```


### 12.1.1. Utilización da librería functools

A función `wraps` de `functools` é comunmente utilizada ao definir decorador en Python por varias razóns:

- **Preservar a información de metadatos da función orixinal**.

- **Facilita a depuración e análise de código**

- **Compatible con outras ferramentas e bibliotecas**

O exemplo anterior utilizando dita librería é similar:

```python
# Importamos a funcion wraps
from functools import wraps


# Función decoradora
def funcion_decoradora(funcion_a_decorar):
    
    # Dita funcion wraps tamén é unha función decoradora
    @wraps(funcion_a_decorar)
    def funcion_a_executar(*args, **kwargs):
        
        # Código adicional antes de chamar a función
        # ...
        
        # Executamos a funcion a decorar
        resultado_da_funcion_a_decorar = funcion_a_decorar(*args, **kwargs)

        # Código adicional despois de chamar a función
        ...

        return resultado_da_funcion_a_decorar # Pode ser que a función a decorar non devolva nada, polo que se pode omitir
    return funcion_a_executar
```