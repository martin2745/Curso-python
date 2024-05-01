---
title: "5.3. Bucles infinitos e break"
weight: 3
---

A veces non se sabe se hai que rematar un bucle ata que se recorreu a metade do corpo do mesmo. Nese caso pódese crear un bucle infinito a propósito e usar a sentenza `break` para saír fora del cando se desexe.

O bucle seguinte é, obviamente, un bucle infinito, porque a expresión lóxica da sentenza `while` é sempre certa.

```python
n = 10
while True:
    print(n, end=' ')
    n = n - 1
print('¡Terminado!')
```

![captura5_3_1.png](captura5_3_1.png)

Se cometes o erro de executar este código, aprenderás rapidamente como deter un proceso de Python bloqueado polo sistema, ou terás que localizar onde se encontra o botón de apagado do teu equipo. Este programa funcionará para sempre, ou ata que a batería do equipo remate, xa que a expresión lóxica ao principio do bucle sempre é certa.

A pesar de que este é un caso de bucle infinito inútil, pódese usar ese deseño para construír bucles útiles, sempre que se teña precaución de engadir código no corpo do bucle para saír explicitamente, usando `break` cando se alcance a condición de saída.

Por exemplo, supón que queres recoller entradas de texto de usuario ata que este escriba fin. Poderías escribir:

```python
while True:
    linea = input("> ")
    if linea == "fin":
    	break
    print(linea)
print("¡Terminado!")
```

![captura5_3_2.png](captura5_3_2.png)

A condición do bucle é **True**, o cal é verdadeiro sempre, así que o bucle repetirase ata que se execute a sentenza `break`.

Cada vez que se entra no bucle, pídeselle texto ao usuario. Se o usuario escribe "fin", a sentenza `break` fará que se saia do bucle. En calquera outro caso, o programa repetirá calquera cousa que o usuario escriba e volverá ao principio do bucle. Este é un exemplo do seu funcionamento:

```python
> ola a todos
ola a todos
> acabei
acabei
> fin
¡Terminado!
```

Este modo de escribir bucles `while` é habitual, xa que así pódese comprobar a condición en calquera punto do bucle (non só ao principio), e pódese expresar a condición de parada afirmativamente ("detente cando aconteza...") en vez de ter que facelo ca lóxica negativa ("sigue facéndoo ata que aconteza...").

A sentenza `break` podemos utilizala cando pedimos un número ao usuario e este non o ingresa.

```python
while True:
    try:
    	numero_str = input("Introduce un numero: ")
        numero = int(numero_str)
        break
    except:
        print("Produciuse un erro, o valor introducido non e un numero.")
print(numero)
```

![captura5_3_3.png](captura5_3_3.png)




