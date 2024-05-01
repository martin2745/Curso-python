---
title: "8.3. Alias"
weight: 3
---

Se **a** se refire a un obxecto e ti asignas `b = a`, entón ambas variables refírense ao mesmo obxecto:

```python
a = [1, 2, 3]
b = a
print(b is a) # Imprime: True
```

A asociación dunha variable a un obxecto é chamada **referencia**. Neste exemplo, hai dúas referencias ao mesmo obxecto.

Un obxecto con máis dunha referencia ten máis dun nome, así que dicimos que un obxecto é un **alias**.

Se o alias do obxecto é mutable, **os cambios feitos a un alias afectan ao outro**:

```python
b[0] = 17
print(a) # Imprime: [17, 2, 3]
```

Inda que este comportamento pode ser útil, é propenso a erros. En xeral, é máis seguro evitar usar alias cando estás traballando con obxectos mutables.

## 8.3.1. Copiar un obxecto

Se desexamos realizar unha copia dun **obxecto** podemos utilizar o método `copy()`.

```python
a = [1, 2, 3]
b = a.copy()
```

Neste caso, a variable `b` non será un alias da variable `a`, senón que se realizará unha copia de `a` e asignaráselle a variable `b`.

## 8.3.2. As

A palabra clave `as` utilízase en varios contextos, pero a súa principal función e asignar un alias a un módulo, excepción ou a un nome dunha expresión `import`.

Exemplos:

- **Alias nas excepcións**: É útil cando se manexan varios tipos de excepcións nun bloque `except`:

```python
try:
    # Código que xera unha excepción
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Produciuse un erro: {e}") # Imprime: Produciuse un erro: division by zero
```