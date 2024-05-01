---
title: "6.1. Inmutabilidade dunha cadea"
weight: 1
---

Pode ser tentador utilizar o operador `[]` no lado esquerdo dunha asignación, coa intención de cambiar un carácter dunha cadea. Por exemplo:

```python
saudo = 'ola, mundo!'
saudo[0] = 'O' # TypeError: 'str' object does not support item assignment
```

O obxecto neste caso é a cadea e o ítem é o carácter que tratamos de asignar. Polo momento, un obxecto é a mesma cousa que un valor, pero vamos redefinir isto máis adiante. Un **ítem** é un dos valores dunha secuencia.

A razón pola cal acontece este erro é que as cadeas son **inmutables**, o cal significa que non podes modificar unha cadea existente. O mellor que podes facer é crear unha nova cadea que sexa unha variación da orixina:

```python
saudo = 'ola, mundo!'
novo_saudo = 'O' + saudo[1:]
print(novo_saudo) # Imprime: Ola, mundo!
```

Este exemplo concatena unha nova letra a unha parte de **saudo**. Isto non ten efecto sobre a cadea orixinal.




