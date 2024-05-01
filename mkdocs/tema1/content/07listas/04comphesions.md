---
title: "7.4. List Comprehensions"
weight: 4
---

As ***List Comprehensions*** son unha construción concisa e poderosa que permite crear listas de xeito elegante e eficiente. Proporciona un xeito máis compacto de expresar operacións de bucle nunha soa liña. A sintexe básica é:

```python
nova_lista = [expresion for elemento in iterable if condicion]
```

- **expresion:** É a expresión que se avalia e agrega a nova lista.

- **elemento:** Variable que toma cada valor do iterable.

- **iterable:** A secuencia sobre a cual se itera.

- **condicion (opcional):** Unha condición que filtra os elementos que se agregarán a nova lista.

Exemplos:

- Agregar cadrados de números pares

    ```python
    numeros = [1, 2, 3, 4, 5, 6]
    cadrados_pares = [x**2 for x in numeros if x % 2 == 0]
    print(cadrados_pares) # Imprime: [4, 16, 36]
    ```

- Lista de cadrados ata certo límite

    ```python
    limite = 5
    cadrados = [x**2 for x in range(limite)]
    print(cadrados) # Imprime: [0, 1, 4, 9, 16]
    ```
