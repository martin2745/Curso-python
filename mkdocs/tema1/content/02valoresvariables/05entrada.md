---
title: "2.5. Entrada de datos por teclado"
weight: 5
---

A veces necesitaremos que sexa o usuario quen nos proporcione o valor para unha variable a través do teclado. Python proporciona unha función interna chamada `input` que recibe a entrada dende o teclado. Cando se chama a esta función, o programa detense e espera a que o usuario escriba algo. Cando o usuario pulsa a tecla *Enter*, o programa continúa e `input` devolve a cadea co que escribiu o usuario.

```python
entrada = input()  # Escribimos: Calquera cousa ridícula
print(entrada)  # Imprime: Calquera cousa ridícula
```

Antes de recibir calquera dato dende o usuario, é boa idea escribir unha mensaxe explicándolle o que debe introducir. Pódeselle pasar unha cada a `input`, que será mostrada ao usuario antes de que o programa se deteña para recibir a súa entrada.

```python
nome = input('Como te chamas?\n')  # Imprime: Como te chamas? | Escribimos: Manuel
print(nome)  # Imprime: Manuel
```

O carácter "\n" ao final da mensaxe representa un **newline** (nova liña), que é un carácter especial que provoca un salto de liña. Por iso a entrada do usuario aparece debaixo da nosa mensaxe.

Se esperas que o usuario escriba un enteiro, podes intentar converter o valor de retorno a **int** utilizando a funcións `int()`.

```python
prompt = 'Cal é a velocidade actual?\n'
velocidade = input(prompt) # Imprime: Cal é a velocidade actual? | Escribimos: 17
int(velocidade) # Obtense o valor numerico 17
int(velocidade) + 5# Obtense o valor numerico 22
```

Pero si o usuario escribe algo que non sexa unha cadea de díxitos obterás un erro.

```python
velocidade = input(prompt) # Imprime: 'Cal é a velocidade actual? | Escribimos: A que velocidade te refires?
int(velocidade) # Obtense o erro: ValueError: invalid literal for int()
```

{{% notice style="warning" title="Captura de excepcións" %}}

Veremos máis adiante como controlar estes erros utilizando captura de excepcións.

{{% /notice %}}

