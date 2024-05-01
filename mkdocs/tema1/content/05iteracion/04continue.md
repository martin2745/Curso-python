---
title: "5.4. Finalizar iteracións con continue"
weight: 4
---

Algunhas veces, estando dentro dun bucle necesítase rematar coa iteración actual e saltar a seguinte de xeito inmediato. Neste caso podes utilizar a sentenza `continue` para pasar a seguinte iteración sen rematar a execución do corpo do bucle para a actual.

A continuación móstrase un exemplo dun bucle que repite o que recibe como entrada ata que o usuario escribe "fin", pero trata as liñas que empezan polo carácter *almohadilla* como liñas que non deben mostrarse por pantalla.

```python
while True:
    linea = input("> ")
    if linea[0] == '#' :
        continue
    if linea == 'fin':
        break
    print(linea)
print('¡Terminado!')
```

![captura5_4_1.png](captura5_4_1.png)


Aquí unha execución de exemplo dese novo programa coa sentenza `continue` engadida.

```vim
> ola a todos
ola a todos
> # non imprimas esto
> ¡imprime esto!
¡imprime esto!
> fin
¡Terminado!
```

Todas as liñas imprímense en pantalla, excepto a que comeza co símbolo de *almohadilla*, xa que nese caso execútase `continue`, finaliza a iteración actual e salta de volta a sentenza `while` para comezar a seguinte iteración, de xeito que se omite a sentenza `print`.

Nos bucles tamén se pode utilizar a cláusula `else` ao final do bloque iterativo. **O código dentro desta cláusula só se executará se o bucle non remata debido a un `break`.**


A estrutura xeral dun bucle coa cláusula `else` é a seguinte:

```python
for variable in iterable:
    if condición:
        break
else:
    # Código a executar senon se produce un break
```