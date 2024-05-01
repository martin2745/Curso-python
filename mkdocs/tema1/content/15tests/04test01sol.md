---
title: "15.4. Test 1 Solucións"
weight: 4
---

1. ¿Cal é a función en Python para ler unha cadea de texto desde o teclado?
   - [x] `input()`
   - [ ] `print()`
   - [ ] `readline()`
   - [ ] `scanf()`

2. ¿Qué función se utiliza en Python para imprimir unha mensaxe na pantalla?
   - [ ] `output()`
   - [ ] `show()`
   - [ ] `display()`
   - [x] `print()`

3. ¿Cal é a forma correcta de ler un número enteiro en Python utilizando `input()`?
   - [ ] `num = input("Introduce un número enteiro: ")`
   - [x] `num = int(input("Introduce un número enteiro: "))`
   - [x] `num = int(input("Introduce un número enteiro: ").strip())`
   - [ ] `num = input.int("Introduce un número enteiro: ")`

4. Que expresión avaliará como Verdadeira en Python?
   - [x] `5 > 3 and 10 < 20`
   - [ ] `not True or False`
   - [ ] `7 == 7 or 3 != 3`
   - [ ] `4 <= 2 and 8 != 8`

5. Cal é o resultado da expresión `not (3 >= 5)`?
   - [x] Verdadeira
   - [ ] Falsa
   - [ ] Non é válida
   - [ ] Nin Verdadeira nin Falsa

6. Que expresión avaliará como Falsa en Python?
   - [x] `not (10 > 5)`
   - [x] `5 == 5 and 5 != 5`
   - [ ] `15 < 20 or 30 < 25`
   - [ ] `True and not False`

7. Que expresión en Python avaliará como Verdadeira?
   - [ ] `3 > 5 or 7 > 10`
   - [x] `5 == 5 and 10 >= 10`
   - [ ] `not True and not False`
   - [ ] `2 * 3 == 6 or 4 + 2 == 7`

8. Que expresión en Python avaliará como Falsa?
   - [x] `7 != 7 and 3 <= 2`
   - [x] `10 > 15 or 20 < 10`
   - [x] `not (5 == 5)`
   - [ ] `True or not True`

9. Cal é o resultado da expresión `not (10 != 10)`?
   - [x] Verdadeira
   - [ ] Falsa
   - [ ] Non é válida
   - [ ] Nin Verdadeira nin Falsa

10. Que expresión avaliará como Verdadeira en Python?
   - [x] `True or False`
   - [ ] `5 >= 5 and 3 <= 2`
   - [ ] `7 == 8 or 8 > 10`
   - [x] `not (10 <= 5)`

11. Que resultado obteremos ao avaliar a expresión `5 != 5 and 10 > 5`?
   - [ ] Verdadeira
   - [x] Falsa
   - [ ] Non é válida
   - [ ] Nin Verdadeira nin Falsa

12. Que expresión en Python avaliará como Verdadeira?
   - [ ] `not (3 != 3)`
   - [x] `5 + 5 == 10 and 10 > 5`
   - [x] `False or True`
   - [ ] `10 <= 5 and 15 != 15`

13. Cal é o resultado da expresión `not (True and False)`?
    - [x] Verdadeira
    - [ ] Falsa
    - [ ] Non é válida
    - [ ] Nin Verdadeira nin Falsa

15. Como se escribiría en Python unha estrutura condicional "if" que imprimise "O número é positivo" se o número é maior que cero?
   - [x] 
     ```python
     if numero > 0:
         print("O número é positivo")
     ```
   - [ ] 
     ```python
     if numero >= 0:
         print("O número é positivo")
     ```
   - [ ] 
     ```python
     if numero == 0:
         print("O número é positivo")
     ```
   - [ ] 
     ```python
     if numero < 0:
         print("O número é positivo")
     ```

16. Cal sería a forma correcta de escribir unha estrutura condicional "if-else" en Python que imprimise "O número é par" se o número é par e "O número é impar" en caso contrario?
   - [x] 
     ```python
     if numero % 2 == 0:
         print("O número é par")
     else:
         print("O número é impar")
     ```
   - [ ] 
     ```python
     if numero % 2 == 0:
         print("O número é par")
     elif numero % 2 != 0:
         print("O número é impar")
     ```
   - [ ] 
     ```python
     if numero / 2 == 0:
         print("O número é par")
     else:
         print("O número é impar")
     ```
   - [ ] 
     ```python
     if numero / 2 == 1:
         print("O número é par")
     else:
         print("O número é impar")
     ```


17. Cal é a estrutura básica en Python para capturar excepcións?
   - [x] 
     ```python
     try:
         # Código que pode xerar unha excepción
     except Exception as e:
         # Manejo da excepción
     ```

   - [ ] 
     ```python
     begin:
         # Código que pode xerar unha excepción
     except Exception as e:
         # Manejo da excepción
     ```

   - [ ] 
     ```python
     test:
         # Código que pode xerar unha excepción
     except Exception as e:
         # Manejo da excepción
     ```

   - [ ] 
     ```python
     try:
         # Código que pode xerar unha excepción
     catch Exception as e:
         # Manejo da excepción
     ```

18. Que tipo de excepción se pode capturar con `except Exception as e` en Python?
   - [x] Todas as excepcións
   - [ ] Só as excepcións de tempo de execución
   - [ ] Só as excepcións de sintaxe
   - [ ] Ningunha, esta sintaxe é incorrecta

19. Que se coloca dentro do bloque `try` en Python?
   - [ ] O código que sempre se executa
   - [ ] O código que se executa despois de manexar unha excepción
   - [x] O código que pode xerar unha excepción
   - [ ] O código que manexa unha excepción

20. Como se captura unha excepción específica en Python?
   - [x] 
     ```python
     try:
         # Código que pode xerar unha excepción
     except ExceptionType:
         # Manejo da excepción
     ```

   - [ ] 
     ```python
     try:
         # Código que pode xerar unha excepción
     except:
         # Manejo da excepción
     ```

   - [ ] 
     ```python
     try:
         # Código que pode xerar unha excepción
     except:
         # Manejo da excepción
     ```

   - [ ] 
     ```python
     try:
         # Código que pode xerar unha excepción
     catch ExceptionType:
         # Manejo da excepción
     ```

21. Que palabra clave se utiliza para executar código despois de que unha excepción foi manexada en Python?
   - [x] `finally`
   - [ ] `end`
   - [ ] `endtry`
   - [ ] `catch`


22. Como se define unha función en Python?
   - [x] 
     ```python
     def
     ```
   - [ ] 
     ```python
     fun
     ```
   - [ ] 
     ```python
     define
     ```
   - [ ] 
     ```python
     function
     ```

23. Como se define unha función en Python con un parámetro chamado "valor"?
   - [x] 
     ```python
     def my_function(value):
         # Código da función
     ```
   - [ ] 
     ```python
     function my_function(value):
         # Código da función
     ```
   - [ ] 
     ```python
     define my_function(value):
         # Código da función
     ```
   - [ ] 
     ```python
     def my_function:
         # Código da función
     ```

24. Como se define unha función en Python con dous parámetros, "x" e "y"?
   - [x] 
     ```python
     def my_function(x, y):
         # Código da función
     ```
   - [ ] 
     ```python
     function my_function(x, y):
         # Código da función
     ```
   - [ ] 
     ```python
     define my_function(x, y):
         # Código da función
     ```
   - [ ] 
     ```python
     def my_function:
         # Código da función
     ```

25. Como se define unha función en Python cun parámetro clave chamado "nome"?
   - [ ] 
     ```python
     def my_function(nome):
         # Código da función
     ```
   - [ ] 
     ```python
     function my_function(nome):
         # Código da función
     ```
   - [ ] 
     ```python
     define my_function(nome):
         # Código da función
     ```
   - [x] 
     ```python
     def my_function(nome=valor):
         # Código da función
     ```

26. Como se define unha función en Python cun parámetro clave chamado "idade" cun valor predeterminado de 18?
   - [x] 
     ```python
     def my_function(idade=18):
         # Código da función
     ```
   - [ ] 
     ```python
     function my_function(idade=18):
         # Código da función
     ```
   - [ ] 
     ```python
     define my_function(idade=18):
         # Código da función
     ```
   - [ ] 
     ```python
     def my_function(idade=):
         # Código da función
     ```

27. Como se chama un parámetro clave ao chamar unha función en Python?
   - [x] 
     ```python
     my_function(key=value)
     ```
   - [ ] 
     ```python
     my_function(value)
     ```
   - [ ] 
     ```python
     my_function(key)
     ```
   - [x] 
     ```python
     my_function(nome=valor)
     ```

28. Que ocorre se se chama unha función en Python sen proporcionar un valor para un parámetro clave cun valor predeterminado?
   - [ ] A función xerará un erro e non se executará.
   - [x] A función utilizará o valor predeterminado especificado para ese parámetro clave.
   - [ ] A función utilizará None como valor para ese parámetro clave.
   - [ ] A función xerará un erro pero seguirá executándose.

29. É posible ter parámetros clave despois dos parámetros posicionais na definición dunha función en Python?
   - [x] Si, Python permite isto.
   - [ ] Non, isto xerará un erro de sintaxe.
   - [ ] Si, pero só se todos os parámetros estiveren presentes ao chamar a función.
   - [ ] Non, só os parámetros posicionais poden estar antes dos parámetros clave.

30. Poden proporcionarse valores para os parámetros clave en calquera orde ao chamar unha función en Python?
   - [x] Si, Python permite isto.
   - [ ] Non, os parámetros clave sempre deben seguir a orde na que se definiron na función.
   - [ ] Si, pero só se todos os parámetros estiveren presentes ao chamar a función.
   - [ ] Non, os parámetros clave sempre deben preceder aos parámetros posicionais.

31. Como se pode definir unha función en Python con parámetros posicionais e parámetros clave simultaneamente?
   - [x] 
     ```python
     def my_function(x, y, clave1, clave2=valor):
         # Código da función
     ```
   - [ ] 
     ```python
     function my_function(x, y, clave1, clave2=valor):
         # Código da función
     ```
   - [ ] 
     ```python
     define my_function(x, y, clave1, clave2=valor):
         # Código da función
     ```

32. Como se define unha función en Python que acepta un número variable de argumentos posicionais utilizando `*args`?
   - [x] 
     ```python
     def my_function(*args):
         # Código de la función
     ```
   - [ ] 
     ```python
     function my_function(*args):
         # Código de la función
     ```
   - [ ] 
     ```python
     define my_function(*args):
         # Código de la función
     ```
   - [ ] 
     ```python
     def my_function(args*):
         # Código de la función
     ```

33. Como se chama un parámetro de lonxitude variable ao chamar a unha función en Python?
   - [x] `my_function(arg1, arg2)`
   - [ ] `my_function(args=valor)`
   - [ ] `my_function(*args)`
   - [ ] `my_function(**kwargs)`

34. Como se define unha función en Python que acepta un número variable de argumentos clave-valor utilizando `**kwargs`?
   - [x] 
     ```python
     def my_function(**kwargs):
         # Código de la función
     ```
   - [ ] 
     ```python
     function my_function(**kwargs):
         # Código de la función
     ```
   - [ ] 
     ```python
     define my_function(**kwargs):
         # Código de la función
     ```
   - [ ] 
     ```python
     def my_function:
         # Código de la función
     ```

35. Que sucede se se intenta chamar a unha función en Python que utiliza `*args` sen pasar ningún argumento?
   - [ ] A función xerará un erro e non se executará.
   - [ ] A función executará correctamente con un valor predeterminado para `args`.
   - [x] A función utilizará `None` como valor para `args`.
   - [ ] A función xerará un erro pero seguirá executándose.

36. Que tipo de estructura de datos se utiliza internamente en Python para almacenar los argumentos variables pasados a una función con `*args`?
   - [ ] Tupla
   - [x] Lista
   - [ ] Diccionario
   - [ ] Conjunto


37. Que palabra clave se utiliza en Python para definir expresións lambda?
   - [ ] 
     ```python
     def
     ```
   - [ ] 
     ```python
     function
     ```
   - [x] 
     ```python
     lambda
     ```
   - [ ] 
     ```python
     expr
     ```

38. Como se define unha expresión lambda en Python que suma dous números?
   - [x] 
     ```python
     lambda x, y: x + y
     ```
   - [ ] 
     ```python
     (x, y) => x + y
     ```
   - [ ] 
     ```python
     lambda(x, y) => x + y
     ```
   - [ ] 
     ```python
     def lambda(x, y): return x + y
     ```

39. Que tipo de obxecto se crea ao definir unha expresión lambda en Python?
   - [ ] Tupla
   - [ ] Lista
   - [x] Función
   - [ ] Diccionario


40. Que ocorre se se define unha expresión lambda sen asignala a ningunha variable en Python?
   - [ ] A expresión lambda xerará un erro de sintaxe.
   - [ ] A expresión lambda asignarase automaticamente a unha variable temporal.
   - [ ] A expresión lambda non se pode definir sen asignala a unha variable.
   - [x] A expresión lambda será ignorada e non se executará.


41. Como se pode utilizar unha expresión lambda en Python para ordear unha lista de tuplas polo segundo elemento de cada tupla?
   - [ ] 
     ```python
     sorted_list = sorted(my_list, lambda x: x[1])
     ```
   - [ ] 
     ```python
     sorted_list = my_list.sort(key=lambda x: x[1])
     ```
   - [ ] 
     ```python
     sorted_list = my_list.sort(lambda x: x[1])
     ```
   - [x] 
     ```python
     sorted_list = sorted(my_list, key=lambda x: x[1])
     ```

42. Como se pode utilizar unha expresión lambda en Python para filtrar os elementos pares dunha lista?
   - [x] 
     ```python
     filtered_list = filter(lambda x: x % 2 == 0, my_list)
     ```
   - [ ] 
     ```python
     filtered_list = lambda x: x % 2 == 0, my_list
     ```
   - [ ] 
     ```python
     filtered_list = my_list.filter(lambda x: x % 2 == 0)
     ```
   - [ ] 
     ```python
     filtered_list = my_list.filter(lambda x: x % 2 == 0, my_list)
     ```

43. Que ocorre se se intenta asignar unha expresión lambda a unha variable e logo chamar a esa variable como unha función en Python?
   - [x] A variable actuará como unha función e executarase correctamente.
   - [ ] Isto xerará un erro porque as expresións lambda non se poden asignar a variables.
   - [ ] Isto xerará un erro porque as expresións lambda non se poden chamar como funcións.
   - [ ] A variable actuará como unha función, pero só se define coa palabra clave `lambda`.

44. ¿Qué palabra chave se utiliza en Python para crear un xerador?
   - [x] `yield`
   - [ ] `return`
   - [ ] `yield from`
   - [ ] `xerador`

45. ¿Que fai a palabra chave `yield` en Python?
   - [ ] Retorna un valor e finaliza a execución da función.
   - [x] Retorna un valor e continúa a execución da función a próxima vez que é chamada.
   - [ ] Retorna múltiples valores de forma iterativa.
   - [ ] Retorna un valor e continúa a execución da función desde o inicio.

46. ¿Cal é a principal diferenza entre unha función que utiliza `yield` e unha que utiliza `return` en Python?
   - [ ] Unha función que utiliza `yield` retorna un valor e finaliza a súa execución, mentres que unha que utiliza `return` continúa a súa execución.
   - [ ] Unha función que utiliza `yield` retorna múltiples valores de forma iterativa, mentres que unha que utiliza `return` retorna só un valor e finaliza a súa execución.
   - [ ] Non hai diferenza, ambas palabras chaves úsanse indistintamente en funcións.
   - [x] Unha función que utiliza `yield` retorna un valor e continúa a súa execución a próxima vez que é chamada, mentres que unha que utiliza `return` retorna un valor e finaliza a súa execución.