---
title: "5.2. A sentenza while"
weight: 2
---

Os ordenadores utilízanse a miúdo para automatizar tarefas repetitivas. Repetir tarefas idénticas ou moi similares sen cometer erros é algo que as máquinas se lles da ben e en cambio as persoas non. Como as iteracións resultan tan habituais, Python proporciona varias características na sua linguaxe para facelas sinxelas. 

Unha forma de iteración en Python é a sentenza `while`. Aquí un programa sinxelo que conta cara atrás dende cinco e logo di "¡Despegue!".

```python
n = 5
while n > 0:
    print(n)
    n = n - 1
print('¡Despegue!')
```

Case se pode ler a sentenza `while` como se estivera en inglés. Significado: mentres **n** sexa menor que 0, mostra o valor de **n** e logo reduce o valor de **n** nunha unidade. Cando chegues a 0, sal da sentenza `while` e mostra a palabra "¡Despegue!".

Este e o fluxo de execución da sentenza `while`, explicado dun xeito máis formal.

1. Avaliase a condición, obtendo **Verdadeiro** ou **Falso**.

2. Se a condición e falsa, sáese da sentenza `while` e continúase a execución na seguinte sentencia.

3. Se a condición é verdadeira, executase o corpo de `while` e logo volvese ao paso 1.

![captura5_2_1.png](captura5_2_1.png)

Este tipo de fluxo recibe o nome de **bucle**, xa que o terceiro paso enlaza de novo co primeiro. Cada vez que se executa o corpo do bucle dise que realizamos unha iteración. para o bucle anterior, poderíamos dicir que tivo cinco iteracións, o que significa que o corpo do bucle executouse cinco veces.

O corpo do bucle debe cambiar o valor dunha ou máis variables, de xeito que a condición poida en algún momento avaliarse como falsa e o bucle remate. A variable que cambia cada vez que o bucle se executa e controla cando remata este, recibe o nome de **variable de iteración**. Se non hai variable de iteración, o bucle repetirase para sempre, resultando así un **bucle infinito**.