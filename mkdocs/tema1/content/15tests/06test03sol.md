---
title: "15.6. Test 3 Solución"
weight: 6
---

1. ¿Cal é a forma correcta de crear un dicionario baleiro en Python?
   - [x] `diccionario = {}`
   - [ ] `diccionario = []`
   - [ ] `diccionario = ()`
   - [ ] `diccionario = None`

2. ¿Qué método se utiliza para engadir un elemento a un dicionario en Python?
   - [ ] `add()`
   - [ ] `append()`
   - [ ] `insert()`
   - [x] `update()`

3. ¿Cal é o resultado de `len(diccionario)` se `diccionario = {"a": 1, "b": 2, "c": 3}` en Python?
   - [ ] 0
   - [ ] 1
   - [x] 3
   - [ ] 6

4. ¿Qué operador se utiliza para acceder ao valor dunha chave nun dicionario en Python?
   - [x] `[]`
   - [ ] `()`
   - [ ] `{}`
   - [ ] `<>`

5. ¿Qué método se utiliza para eliminar un elemento dun dicionario en Python?
   - [ ] `remove()`
   - [x] `pop()`
   - [ ] `delete()`
   - [ ] `discard()`

6. ¿Cal é a forma correcta de acceder ao valor asociado á clave "b" no dicionario `diccionario = {"a": 1, "b": 2, "c": 3}` en Python?
   - [x] `diccionario["b"]`
   - [ ] `diccionario(b)`
   - [x] `diccionario.get("b")`
   - [ ] `diccionario.value("b")`

7. ¿Qué método se utiliza para obter unha lista con todas as chaves dun dicionario en Python?
   - [x] `keys()`
   - [ ] `values()`
   - [ ] `items()`
   - [ ] `all_keys()`

8. ¿Cal é o resultado de `diccionario.get("d", 0)` se `diccionario = {"a": 1, "b": 2, "c": 3}` en Python?
   - [x] 0
   - [ ] 1
   - [ ] 2
   - [ ] 3

9. ¿Qué método se utiliza para obter unha lista con todos os valores dun dicionario en Python?
   - [ ] `keys()`
   - [x] `values()`
   - [ ] `items()`
   - [ ] `all_values()`

10. ¿Cal é o resultado de `diccionario.pop("b")` se `diccionario = {"a": 1, "b": 2, "c": 3}` en Python?
    - [ ] `2`
    - [x] `{"a": 1, "c": 3}`
    - [ ] `{"a": 1, "b": 2}`
    - [ ] `{"c": 3}`

11. ¿Qué método se utiliza para iterar sobre as chaves dun dicionario en Python?
   - [x] `for key in diccionario.keys():`
   - [ ] `for key in diccionario.items():`
   - [ ] `for key in diccionario.values():`
   - [ ] `for key in diccionario:`

12. ¿Cal é a saída do seguinte código en Python?

   ```python
   diccionario = {"a": 1, "b": 2, "c": 3}
   for key, value in diccionario.items():
       print(key, value)
   ```

   - [x] `a 1`, `b 2`, `c 3`
   - [ ] `1 a`, `2 b`, `3 c`
   - [ ] `a`, `b`, `c`
   - [ ] `1`, `2`, `3`

13. ¿Qué función se utiliza para comprobar se unha clave está presente nun dicionario en Python?
   - [ ] `find()`
   - [ ] `exists()`
   - [ ] `contains()`
   - [x] `in`

14. ¿Cal é a saída do seguinte código en Python?

   ```python
   diccionario = {"a": 1, "b": 2, "c": 3}
   for key in diccionario:
       print(key)
   ```

   - [x] `a`, `b`, `c`
   - [ ] `1`, `2`, `3`
   - [ ] `a`, `1`, `b`, `2`, `c`, `3`
   - [ ] `a 1`, `b 2`, `c 3`

15. ¿Qué método se utiliza para obter unha lista de tuplas que conteñen pares chave-valor nun dicionario en Python?
   - [ ] `keys()`
   - [ ] `values()`
   - [x] `items()`
   - [ ] `pairs()`

16. ¿Cuál es la forma correcta de acceder al valor asociado a la clave "b" en el diccionario `diccionario = {"a": {"x": 1, "y": 2}, "b": {"x": 3, "y": 4}}` en Python?
   - [ ] `diccionario["b"]["x"]`
   - [ ] `diccionario["b", "x"]`
   - [ ] `diccionario["b"].get("x")`
   - [x] `diccionario.get("b", "x")`

17. ¿Qué método se utiliza para iterar sobre los elementos de un diccionario?
   - [ ] `for key, value in diccionario:`
   - [x] `for key, value in diccionario.items():`
   - [ ] `for key, value in diccionario.keys():`
   - [ ] `for key, value in diccionario.values():`

18. ¿Cuál es la forma correcta de acceder al valor de la primera lista en el diccionario `diccionario = {"a": [1, 2, 3], "b": [4, 5, 6]}` en Python?
   - [ ] `diccionario[0]`
   - [x] `diccionario["a"]`
   - [x] `diccionario.get("a")`
   - [ ] `diccionario["a"][0]`

19. ¿Cal é a forma correcta de abrir un ficheiro de texto chamado "datos.txt" en modo lectura en Python?

   - [x] `archivo = open("datos.txt", "r")`
   - [ ] `archivo = open("datos.txt", "w")`
   - [ ] `archivo = open("datos.txt", "a")`
   - [ ] `archivo = open("datos.txt", "rb")`


20. ¿Qué método se utiliza para ler o contido completo dun ficheiro de texto en Python?
   
   - [x] `archivo.read()`
   - [ ] `archivo.readline()`
   - [ ] `archivo.readlines()`
   - [ ] `archivo.write()`


21. ¿Cal é a forma correcta de pechar un ficheiro despois de ler o seu contido en Python?
   
   - [ ] `close(archivo)`
   - [x] `archivo.close()`
   - [ ] `archivo.shutdown()`
   - [ ] `archivo.stop()`


22. ¿Qué método se utiliza para ler unha liña do ficheiro de texto en Python?
   
   - [ ] `archivo.read()`
   - [x] `archivo.readline()`
   - [ ] `archivo.readlines()`
   - [ ] `archivo.write()`

23. ¿Qué fai a seguinte liña de código en Python?

   ```python
   with open("datos.txt", "r") as archivo:
       contenido = archivo.read()
   ```
   - [x] Abre o ficheiro "datos.txt" en modo lectura e almacena o seu contido na variable `contenido`.
   - [ ] Abre o ficheiro "datos.txt" en modo escritura e almacena o seu contido na variable `contenido`.
   - [ ] Abre o ficheiro "datos.txt" en modo anexar e almacena o seu contido na variable `contenido`.
   - [ ] Pecha o ficheiro "datos.txt" despois de ler o seu contido.


24. Supón que temos un ficheiro CSV chamado "datos.csv" coas seguintes columnas: "nome", "idade" e "cidade". ¿Cal sería o código correcto para abrir e ler este ficheiro en Python utilizando o módulo `csv`?
    - [x] 
    
    ```python
       import csv

       with open("datos.csv", "r") as archivo:
           datos = csv.reader(archivo)
           for fila in datos:
               print(fila)
    ```
    - [ ] 
    
    ```python
       import csv

       with open("datos.csv", "r") as archivo:
           datos = csv.reader(archivo)
           print(datos)
    ```
    - [ ] 
    
    ```python
       import csv

       with open("datos.csv", "r") as archivo:
           datos = csv.read(archivo)
           for fila in datos:
               print(fila)
    ```
    - [ ] 
    
    ```python
       import csv

       with open("datos.csv", "r") as archivo:
           datos = archivo.read_csv()
           for fila in datos:
               print(fila)
    ```

25. ¿Cal das seguintes afirmacións é correcta sobre o manexo de delimitadores en ficheiros CSV en Python?
    - [x] Por defecto, o delimitador no módulo `csv` de Python é a coma (,).
    - [ ] O delimitador no módulo `csv` de Python sempre debe ser especificado polo usuario.
    - [ ] O delimitador no módulo `csv` de Python é sempre o tabulador (\t).
    - [ ] Non se poden utilizar delimitadores personalizados no módulo `csv` de Python.

26. ¿Cal é a forma correcta de ler un ficheiro CSV cun delimitador personalizado (por exemplo, un punto e coma ";") en Python utilizando o módulo `csv`?
    - [x] 
    ```python
       import csv

       with open("datos.csv", "r") as archivo:
           datos = csv.reader(archivo, delimiter=';')
           for fila in datos:
               print(fila)
    ```
    - [ ] 
    ```python
       import csv

       with open("datos.csv", "r") as archivo:
           datos = csv.reader(archivo, delim=';')
           for fila in datos:
               print(fila)
    ```
    - [ ] 
    ```python
       import csv

       with open("datos.csv", "r") as archivo:
           datos = csv.reader(archivo, delim=';')
           print(datos)
    ```
    - [x] 
    ```python
       import csv

       with open("datos.csv", "r") as archivo:
           datos = csv.read(archivo, delimiter=';')
           for fila in datos:
               print(fila)
    ```

27. ¿Qué método se utiliza para ler un ficheiro CSV nun dicionario en Python utilizando o módulo `csv`?
    - [ ] `csv.read()`
    - [ ] `csv.parse()`
    - [ ] `csv.dictreader()`
    - [x] `csv.reader()`

28. Supón que temos un ficheiro CSV chamado "datos.csv" coa primeira fila como encabezados de columna. ¿Cal sería o código correcto para ler este ficheiro en Python e obter os datos nun dicionario utilizando o módulo `csv`?
    - [ ] 
    ```python
       import csv

       with open("datos.csv", "r") as archivo:
           datos = csv.reader(archivo)
           diccionario_datos = {fila[0]: fila[1:] for fila in datos}
           print(diccionario_datos)
    ```
    - [ ] 
    ```python
       import csv

       with open("datos.csv", "r") as archivo:
           datos = csv.DictReader(archivo)
           diccionario_datos = {fila[0]: fila[1:] for fila in datos}
           print(diccionario_datos)
    ```
    - [x] 
    ```python
       import csv

       with open("datos.csv", "r") as archivo:
           datos = csv.DictReader(archivo)
           diccionario_datos = {fila['nombre']: fila['edad', 'ciudad'] for fila in datos}
           print(diccionario_datos)
    ```
    - [ ] 
    ```python
       import csv

       with open("datos.csv", "r") as archivo:
           datos = csv.DictReader(archivo)
           diccionario_datos = {fila[0]: fila[1:] for fila in datos}
           for fila in diccionario_datos:
               print(fila)
    ```


29. Supón que temos unha lista de listas chamada `datos` que contén datos que queremos escribir nun ficheiro CSV. ¿Cal sería o código correcto para escribir estes datos nun ficheiro chamado "output.csv" en Python utilizando o módulo `csv`?
    - [x] 
    ```python
       import csv

       with open("output.csv", "w") as archivo:
           escritor_csv = csv.writer(archivo)
           for fila in datos:
               escritor_csv.writerow(fila)
    ```
    - [ ] 
    ```python
       import csv

       with open("output.csv", "w") as archivo:
           escritor_csv = csv.writer(archivo)
           escritor_csv.write(datos)
    ```
    - [ ] 
    ```python
       import csv

       with open("output.csv", "w") as archivo:
           escritor_csv = csv.write(archivo)
           escritor_csv.write_rows(datos)
    ```
    - [ ] 
    ```python
       import csv

       with open("output.csv", "w") as archivo:
           escritor_csv = csv.writer(archivo)
           escritor_csv.write_rows(datos)
    ```

30. ¿Cal das seguintes afirmacións é correcta sobre a escritura de ficheiros CSV en Python?
    - [ ] Os ficheiros CSV sempre deben escribirse en modo binario.
    - [ ] O módulo `csv` de Python non admite a escritura de datos en ficheiros CSV.
    - [x] A función `writerow()` do módulo `csv` úsase para escribir múltiples filas nun ficheiro CSV.
    - [ ] Se o ficheiro CSV xa existe, escribir datos nel co módulo `csv` sobrescribirá o ficheiro existente.

31. Supón que queremos escribir un dicionario nun ficheiro CSV en Python. ¿Cal sería o enfoque máis axeitado utilizando o módulo `csv`?
    - [x] Converter o dicionario nunha lista de listas e logo escribir cada fila coa función `writerow()` do módulo `csv`.
    - [ ] Utilizar a función `write_dict()` do módulo `csv` para escribir o dicionario directamente no ficheiro CSV.
    - [ ] Converter o dicionario nunha lista de tuplas e logo escribir cada fila coa función `writerow()` do módulo `csv`.
    - [ ] Converter o dicionario nun obxecto `DictWriter` do módulo `csv` e logo escribilo no ficheiro CSV.

32. ¿Qué método se utiliza para escribir encabezados de columna nun ficheiro CSV utilizando o módulo `csv` en Python?
    - [ ] `write_headers()`
    - [x] `write_row()`
    - [ ] `writerow()`
    - [ ] `write_header_row()`

33. Supón que temos un dicionario onde as chaves son os encabezados de columna e os valores son listas de datos correspondentes. ¿Cal sería o código correcto para escribir este dicionario nun ficheiro CSV en Python utilizando o módulo `csv`?
    - [x] 
    ```python
       import csv

       with open("output.csv", "w") as archivo:
           campos = diccionario.keys()
           escritor_csv = csv.DictWriter(archivo, fieldnames=campos)
           escritor_csv.writeheader()
           escritor_csv.writerows(diccionario)
    ```
    - [ ] 
    ```python
       import csv

       with open("output.csv", "w") as archivo:
           escritor_csv = csv.writer(archivo)
           escritor_csv.writerow(diccionario.keys())
           escritor_csv.writerows(diccionario.values())
    ```
    - [ ] 
    ```python
       import csv

       with open("output.csv", "w") as archivo:
           escritor_csv = csv.DictWriter(archivo, fieldnames=diccionario.keys())
           escritor_csv.writeheader()
           escritor_csv.writerows(diccionario.values())
    ```
    - [ ] 
    ```python
       import csv

       with open("output.csv", "w") as archivo:
           escritor_csv = csv.DictWriter(archivo, fieldnames=diccionario.keys())
           escritor_csv.writerow(diccionario.keys())
           escritor_csv.writerows(diccionario.values())
    ```

34. ¿Cal é o módulo principal que se utiliza para traballar con arquivos JSON en Python?
    - [ ] `os`
    - [x] `json`
    - [ ] `csv`
    - [ ] `sys`

35. ¿Qué función se utiliza para cargar datos desde un arquivo JSON en Python?
    - [ ] `load_json()`
    - [ ] `parse_json()`
    - [x] `json.load()`
    - [ ] `read_json()`

36. ¿Cal é a forma correcta de abrir e cargar un arquivo JSON chamado "datos.json" en Python?
    - [x] 
    ```python
       with open("datos.json", "r") as arquivo:
           datos = json.load(arquivo)
    ```
    - [ ] 
    ```python
       datos = json.load("datos.json")
    ```
    - [x] 
    ```python
       arquivo = open("datos.json", "r")
       datos = json.load(arquivo)
    ```
    - [ ] 
    ```python
       datos = open("datos.json", "r").load()
    ```

37. ¿Cal é a forma correcta de manexar unha excepción cando se carga un arquivo JSON en Python?
    - [ ] 
    
    ```python
       try:
           with open("datos.json", "r") as arquivo:
               datos = json.load(arquivo)
       except JSONError:
           print("Erro ao cargar o arquivo JSON")
    ```

    - [ ] 
    ```python
       try:
           datos = json.load("datos.json")
       except IOError:
           print("Erro ao cargar o arquivo JSON")
    ```
    - [x] 
    ```python
       try:
           arquivo = open("datos.json", "r")
           datos = json.load(arquivo)
       except Exception as e:
           print("Erro:", e)
    ```
    - [ ] 
    ```python
       try:
           datos = open("datos.json", "r").load()
       except FileNotFoundError:
           print("Erro ao cargar o arquivo JSON")
    ```


38. ¿Qué función se utiliza para escribir datos nun ficheiro JSON en Python?
    - [ ] `write_json()`
    - [ ] `parse_json()`
    - [x] `json.dump()`
    - [ ] `json.write()`

39. ¿Cal é a forma correcta de abrir un ficheiro JSON en modo escritura en Python?
    - [x] `open("datos.json", "w")`
    - [ ] `open("datos.json", "r")`
    - [ ] `open("datos.json", "a")`
    - [ ] `open("datos.json", "x")`

40. ¿Qué función se utiliza para escribir un dicionario nun ficheiro JSON en Python?
    - [ ] `write_dict()`
    - [ ] `dump_dict()`
    - [ ] `json.write()`
    - [x] `json.dump()`

41. ¿Cal é a forma correcta de escribir un dicionario nun ficheiro JSON chamado "datos.json" en Python?
    - [ ] 
    ```python
       with open("datos.json", "w") as arquivo:
           json.write(archivo, diccionario)
    ```
    - [ ] 
    ```python
       with open("datos.json", "w") as arquivo:
           json.write(diccionario, arquivo)
    ```
    - [x] 
    ```python
       with open("datos.json", "w") as arquivo:
           json.dump(diccionario, arquivo)
    ```
    - [ ] 
    ```python
       with open("datos.json", "w") as arquivo:
           dump_dict(diccionario, arquivo)
    ```

42. ¿Cal é a forma correcta de manexar unha excepción ao escribir nun ficheiro JSON en Python?
    - [ ] 
    ```python
       try:
           with open("datos.json", "w") as arquivo:
               json.dump(diccionario, arquivo)
       except JSONError:
           print("Erro ao escribir no ficheiro JSON")
    ```
    - [x] 
    ```python
       try:
           arquivo = open("datos.json", "w")
           json.dump(diccionario, arquivo)
       except Exception as e:
           print("Erro:", e)
    ```
    - [ ] 
    ```python
       try:
           json.dump(diccionario, "datos.json")
       except IOError:
           print("Erro ao escribir no ficheiro JSON")
    ```
    - [ ] 
    ```python
       try:
           with open("datos.json", "w") as arquivo:
               arquivo.write(json.dump(diccionario))
       except FileNotFoundError:
           print("Erro ao escribir no ficheiro JSON")
    ```

43. ¿Qué é un decorador en Python?
    - [ ] Unha función que engade ornamentación a un obxecto.
    - [x] Unha función que modifica o comportamento doutra función.
    - [ ] Unha función que encapsula datos e comportamento.
    - [ ] Unha función que elimina a necesidade de usar parénteses ao chamar a outra función.

44. ¿Cal é a sintaxe básica para aplicar un decorador a unha función en Python?
    - [x] 
    ```python
       @decorador
       def funcion():
           pass
    ```
    - [ ] 
    ```python
       def funcion():
           pass

       decorador(funcion)
    ```
    - [ ] 
    ```python
       def funcion():
           pass

       @decorador()
       funcion()
    ```
    - [ ] 
    ```python
       def funcion():
           pass

       @decorador
       funcion()
    ```

45. ¿Cal é o propósito principal dun decorador en Python?
    - [ ] Engadir documentación a unha función.
    - [ ] Modificar o nome dunha función.
    - [ ] Cambiar o tipo de datos de retorno dunha función.
    - [x] Modificar o comportamento dunha función sen modificar a súa implementación.

46. ¿Que fai o seguinte decorador en Python?

    ```python
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            print("Antes de chamar á función")
            resultado = funcion(*args, **kwargs)
            print("Despois de chamar á función")
            return resultado
        return wrapper
    ```

    - [x] Imprime "Antes de chamar á función", chama á función orixinal, imprime "Despois de chamar á función" e devolve o resultado da función orixinal.
    - [ ] Imprime "Antes de chamar á función" e devolve o resultado da función orixinal sen chamarla.
    - [ ] Imprime "Despois de chamar á función" e devolve o resultado da función orixinal sen chamarla.
    - [ ] Imprime "Antes de chamar á función" e "Despois de chamar á función", pero non chama á función orixinal.

47. ¿Cal é a principal vantaxe de usar decoradores en Python?
    - [ ] Aumentar a complexidade do código.
    - [ ] Reducir a legibilidade do código.
    - [x] Proporcionar unha forma de reutilizar e extender o comportamento das funcións.
    - [ ] Permitir a chamada de funcións sen necesidade de parénteses.

48. ¿Qué fai o seguinte decorador en Python?

    ```python
    def cronometrar(funcion):
        def wrapper(*args, **kwargs):
            import time
            inicio = time.time()
            resultado = funcion(*args, **kwargs)
            fin = time.time()
            print(f"A función {funcion.__name__} tardou {fin - inicio} segundos en executarse.")
            return resultado
        return wrapper

    @cronometrar
    def suma(a, b):
        return a + b
    ```

    - [x] Calcula o tempo de execución da función `suma` e imprime o resultado.
    - [ ] Adiciona 5 segundos á execución da función `suma`.
    - [ ] Adiciona un retraso aleatorio á execución da función `suma`.
    - [ ] Subtrai o tempo de execución da función `suma` dun valor predefinido.

49. ¿Qué fai o seguinte decorador en Python?

    ```python
    def auditar(funcion):
        def wrapper(*args, **kwargs):
            resultado = funcion(*args, **kwargs)
            with open("log.txt", "a") as archivo:
                archivo.write(f"Chamada a {funcion.__name__} con argumentos {args} e {kwargs} devolveu {resultado}\n")
            return resultado
        return wrapper

    @auditar
    def multiplicar(a, b):
        return a * b
    ```

    - [ ] Multiplica os argumentos `a` e `b` e garda o resultado nun arquivo de rexistro.
    - [x] Escriba unha mensaxe de rexistro cando a función `multiplicar` sexa chamada.
    - [ ] Divide os argumentos `a` e `b` e garda o resultado nun arquivo de rexistro.
    - [ ] Engade os argumentos `a` e `b` e garda o resultado nun arquivo de rexistro.

50. ¿Qué fai o seguinte decorador en Python?

    ```python
    def memoizar(funcion):
        cache = {}
        def wrapper(*args):
            if args not in cache:
                cache[args] = funcion(*args)
            return cache[args]
        return wrapper

    @memoizar
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    ```

    - [x] Calcula o factorial dun número e garda o resultado nunha caché.
    - [ ] Escriba unha mensaxe de erro se o número pasado á función `factorial` xa se calculou anteriormente.
    - [ ] Calcula o factorial dun número sen gardar o resultado nunha caché.
    - [ ] Calcula o factorial dun número utilizando unha caché para almacenar resultados anteriores.


51. ¿Qué fai a función `re.match()` en Python?

    - [ ] Busca unha coincidencia ao principio dunha cadea de texto.
    - [x] Busca unha coincidencia en calquera parte dunha cadea de texto.
    - [ ] Substitúe un patrón por outro nunha cadea de texto.
    - [ ] Divide unha cadea de texto en base a un patrón dado.

52. ¿Cal é a sintaxe básica para usar a función `re.match()` en Python?

    - [x] `re.match(patrón, cadea)`
    - [ ] `match(patrón, cadea)`
    - [ ] `re.match(cadea, patrón)`
    - [ ] `match(cadea, patrón)`

53. ¿Que devolve a función `re.match()` se hai unha coincidencia ao principio da cadea de texto?

    - [ ] A cadea de texto orixinal sen ningún cambio.
    - [x] Un obxecto de coincidencia que contén información sobre a coincidencia atopada.
    - [ ] Un valor booleano True.
    - [ ] O patrón de busca utilizado.

54. ¿Qué devolve a función `re.match()` se non hai unha coincidencia ao principio da cadea de texto?

    - [ ] Un obxecto de coincidencia que contén información sobre a coincidencia atopada.
    - [ ] Un valor booleano True.
    - [ ] O patrón de busca utilizado.
    - [x] None

55. Considera o seguinte código:

    ```python
    import re
    resultado = re.match(r'ab', 'abcde')
    ```

    ¿Qué devolve `resultado`?

    - [x] `<re.Match object; span=(0, 2), match='ab'>`
    - [ ] `<re.Match object; span=(0, 4), match='abcde'>`
    - [ ] `None`
    - [ ] `True`
    

56. Considera o seguinte código:

    ```python
    import re
    resultado = re.match(r'cd', 'abcde')
    ```

    ¿Qué devolve `resultado`?

    - [x] `<re.Match object; span=(2, 4), match='cd'>`
    - [ ] `<re.Match object; span=(0, 2), match='ab'>`
    - [ ] `None`
    - [ ] `True`

57. ¿Para que se utiliza o método `group()` nun obxecto de coincidencia devolto por `re.match()`?

    - [x] Para devolver a cadea de texto na que se atopou a coincidencia.
    - [ ] Para devolver o patrón de busca utilizado.
    - [ ] Para devolver a posición inicial da coincidencia.
    - [ ] Para devolver información sobre a coincidencia atopada.


58. ¿Qué faz a función `re.findall()` en Python?

    - [ ] Busca a primeira coincidencia dun patrón nunha cadea de texto.
    - [x] Busca todas as ocurrencias dun patrón nunha cadea de texto e devolve unha lista coas coincidencias.
    - [ ] Busca unha coincidencia nunha cadea de texto e devolve o número total de ocurrencias.
    - [ ] Divide unha cadea de texto en base a un patrón dado.

59. ¿Cal é a sintaxe básica para usar a función `re.findall()` en Python?

    - [x] `re.findall(patrón, cadea)`
    - [ ] `findall(patrón, cadea)`
    - [ ] `re.findall(cadea, patrón)`
    - [ ] `findall(cadea, patrón)`

60. ¿Qué devolve a función `re.findall()` se hai coincidencias dun patrón na cadea de texto?

    - [ ] Unha cadea de texto que conteña todas as coincidencias atopadas.
    - [x] Un obxecto de coincidencia que conteña información sobre as coincidencias atopadas.
    - [ ] Unha lista con todas as ocurrencias do patrón na cadea de texto.
    - [ ] O patrón de busca utilizado.
    

61. ¿Qué devolve a función `re.findall()` se non hai coincidencias dun patrón na cadea de texto?

    - [ ] Un obxecto de coincidencia que conteña información sobre as coincidencias atopadas.
    - [ ] Un valor booleano False.
    - [x] Unha lista baleira.
    - [ ] Ningunha devolución, produce un erro.

62. Considera o seguinte código:

    ```python
    import re
    resultado = re.findall(r'\d+', 'Hoxe é o 1 de marzo e o 2 de abril')
    ```

    ¿Qué devolve `resultado`?

    - [x] `['1', '2']`
    - [ ] `['Hoxe', 'é', 'o', '1', 'de', 'marzo', 'e', 'o', '2', 'de', 'abril']`
    - [ ] `['marzo', 'abril']`
    - [ ] `[1, 2]`


63. ¿Qué fai a función `re.sub()` en Python?

    - [ ] Busca a primeira coincidencia dun patrón nunha cadea de texto.
    - [ ] Busca todas as ocurrencias dun patrón nunha cadea de texto e devolve unha lista coas coincidencias.
    - [x] Substitúe todas as ocurrencias dun patrón nunha cadea de texto por outro texto dado.
    - [ ] Divide unha cadea de texto en base a un patrón dado.

64. ¿Cal é a sintaxe básica para usar a función `re.sub()` en Python?

    - [x] `re.sub(patrón, novo_texto, cadea)`
    - [ ] `sub(patrón, novo_texto, cadea)`
    - [ ] `re.sub(cadea, novo_texto, patrón)`
    - [ ] `sub(cadea, novo_texto, patrón)`

65. ¿Qué devolve a función `re.sub()` despois de realizar a substitución dun patrón nunha cadea de texto?

    - [ ] A cadea de texto orixinal sen ningún cambio.
    - [ ] Un obxecto de coincidencia que conteña información sobre a substitución realizada.
    - [ ] Unha lista coas ocurrencias do patrón na cadea de texto.
    - [x] A cadea de texto despois da substitución.

66. ¿Qué devolve a función `re.sub()` se non hai coincidencias dun patrón na cadea de texto?

    - [x] A cadea de texto orixinal sen ningún cambio.
    - [ ] Un obxecto de coincidencia que conteña información sobre a substitución realizada.
    - [ ] Un valor booleano False.
    - [ ] Ningunha devolución, produce un erro.

67. Considera o seguinte código:

    ```python
    import re
    nova_cadea = re.sub(r'\d+', 'X', 'Hoxe é o 1 de marzo e o 2 de abril')
    ```

    ¿Que devolve `nova_cadea`?

    - [x] `'Hoxe é o X de marzo e o X de abril'`
    - [ ] `'Hoxe é o 1 de marzo e o 2 de abril'`
    - [ ] `'Hoxe é o de marzo e o de abril'`
    - [ ] `['Hoxe é o X de marzo e o X de abril']`


68. Considera o seguinte código:

    ```python
    import re
    texto = "O número de teléfono de João é 123-456-7890 e o de Maria é 987-654-3210."
    resultado = re.findall(r'\d{3}-\d{3}-\d{4}', texto)
    ```

    ¿Que devolve `resultado`?

    - [x] `['123-456-7890', '987-654-3210']`
    - [ ] `['123', '456', '7890', '987', '654', '3210']`
    - [ ] `['123', '987']`
    - [ ] `['456', '7890', '654', '3210']`

69. Considera o seguinte código:

    ```python
    import re
    texto = "O email de João é joao@example.com e o de Maria é maria@example.com."
    resultado = re.findall(r'(\w+)@(\w+.\w+)', texto)
    ```

    ¿Que devolve `resultado`?


    - [ ] `[('joao', 'example', 'com'), ('maria', 'example', 'com')]`
    - [ ] `[('joao', 'example.com'), ('maria', 'example.com')]`
    - [ ] `[('joao@example.com', 'maria@example.com')]`
    - [x] `['joao@example.com', 'maria@example.com']`


70. Considera o seguinte código:

    ```python
    import re
    texto = "O número de teléfono de João é 123-456-7890 e o de Maria é 987-654-3210."
    resultado = re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', texto)
    ```

    ¿Que devolve `resultado`?

    - [x] `"O número de teléfono de João é XXX-XXX-XXXX e o de Maria é XXX-XXX-XXXX."`
    - [ ] `"O número de teléfono de João é 123-456-7890 e o de Maria é 987-654-3210."`
    - [ ] `"O número de teléfono de João é 123-456-7890 e o de Maria é 123-456-7890."`
    - [ ] `"O número de teléfono de João é 987-654-3210 e o de Maria é 987-654-3210."`

71. ¿Que devolve o seguinte código Python?

   ```python
   from datetime import datetime

   fecha = datetime.strptime('2024-04-10', '%Y-%m-%d')
   print(fecha.month)
   ```

   - [x] 4
   - [ ] '2024-04-10'
   - [ ] 10
   - [ ] 24

72. ¿Qué fai o seguinte código Python?

   ```python
   from datetime import datetime, timedelta

   fecha_actual = datetime.now()
   fecha_manana = fecha_actual + timedelta(days=1)
   ```

   - [ ] Calcula a diferenza de tempo entre a data actual e mañá.
   - [x] Engade un día á data actual.
   - [ ] Resta un día á data actual.
   - [ ] Xera un erro debido a unha mala sintaxe.

73. Considera o seguinte código Python:

   ```python
   from datetime import datetime

   fecha = datetime.strptime('2024-04-10', '%Y-%m-%d')
   ```

   Que tipo de obxecto é `fecha`?

   - [ ] str
   - [ ] int
   - [ ] list
   - [x] datetime.datetime

74. ¿Qué fai o seguinte código Python?

   ```python
   from datetime import datetime

   fecha = datetime.now()
   print(fecha.strftime('%Y-%m-%d'))
   ```

   - [x] Imprime a data actual no formato "ano-mes-día".
   - [ ] Converte a data actual nun obxecto `datetime`.
   - [ ] Parsea unha cadea de texto co formato "ano-mes-día" nun obxecto `datetime`.
   - [ ] Xera un erro debido a unha mala sintaxe.

75. ¿Cal é o resultado do seguinte código Python?

   ```python
   from datetime import datetime

   fecha = datetime(2024, 4, 10)
   print(fecha.year)
   ```

   - [x] 2024
   - [ ] 4
   - [ ] '2024-04-10'
   - [ ] '2024'


76. ¿Que devolverá o seguinte código Python?

   ```python
   from datetime import date

   fecha = date(2024, 4, 10)
   print(fecha.day)
   ```

   - [x] 10
   - [ ] 4
   - [ ] '2024-04-10'
   - [ ] '2024'

77. ¿Qué fai o seguinte código Python?

   ```python
   from datetime import time

   hora = time(15, 30)
   ```

   - [x] Define unha hora para as 15:30.
   - [ ] Soma 15 horas e 30 minutos á hora actual.
   - [ ] Resta 15 horas e 30 minutos á hora actual.
   - [ ] Xera un erro debido a unha mala sintaxe.

78. Considera o seguinte código Python:

   ```python
   from datetime import date

   fecha = date.today()
   ```

   Que tipo de obxecto é `fecha`?

   - [ ] str
   - [ ] int
   - [ ] list
   - [x] datetime.date

79. ¿Que devolverá o seguinte código Python?

   ```python
   from datetime import date

   fecha = date(2024, 4, 10)
   print(fecha.month)
   ```

   - [x] 4
   - [ ] 10
   - [ ] '2024-04-10'
   - [ ] '2024'

80. ¿Que devolverá o seguinte código Python?

   ```python
   from datetime import time

   hora = time(15, 30, 45)
   print(hora.second)
   ```

   - [x] 45
   - [ ] 30
   - [ ] 15
   - [ ] '15:30:45'

81. ¿Qué fai o seguinte código Python?

   ```python
   from datetime import time

   hora = time(15, 30)
   print(hora.strftime('%H:%M'))
   ```

   - [x] Imprime a hora actual en formato "hora:minuto".
   - [ ] Converte a hora actual nun obxecto `time`.
   - [ ] Parsea unha cadea de texto con formato "hora:minuto" nun obxecto `time`.
   - [ ] Xera un erro debido a unha mala sintaxe.

82. Considera o seguinte código Python:

   ```python
   from datetime import time

   hora = time(15, 30, 45)
   ```

   Que tipo de obxecto é `hora`?

   - [ ] str
   - [ ] int
   - [ ] list
   - [x] datetime.time

83. ¿Que devolverá o seguinte código Python?

   ```python
   from datetime import date

   fecha = date.today()
   print(fecha.year)
   ```

   - [x] O ano actual.
   - [ ] O día actual.
   - [ ] O mes actual.
   - [ ] '2024'

84. ¿Qué devolverá o seguinte código Python?

   ```python
   from datetime import datetime, timedelta

   fecha_actual = datetime.now()
   fecha_futura = fecha_actual + timedelta(days=7)
   print(fecha_futura.strftime('%Y-%m-%d'))
   ```

   - [ ] A data actual en formato "ano-mes-día".
   - [x] A data actual máis 7 días en formato "ano-mes-día".
   - [ ] A data actual en formato "día-mes-ano".
   - [ ] Un erro debido a unha mala sintaxe.

85. Considera o seguinte código Python:

   ```python
   from datetime import datetime, timedelta

   fecha_actual = datetime.now()
   fecha_pasada = fecha_actual - timedelta(hours=2)
   ```

   ¿Que fai este código?

   - [ ] Calcula a diferenza de tempo entre a data actual e hai 2 horas.
   - [x] Resta 2 horas á data actual.
   - [ ] Soma 2 horas á data actual.
   - [ ] Xera un erro debido a unha mala sintaxe.

86. ¿Que devolverá o seguinte código Python?

   ```python
   from datetime import datetime, timedelta

   fecha = datetime.strptime('2024-04-10', '%Y-%m-%d')
   diferenza = datetime.now() - fecha
   print(diferenza.days)
   ```

   - [x] A diferenza de días entre a data actual e o 10 de abril de 2024.
   - [ ] A diferenza de segundos entre a data actual e o 10 de abril de 2024.
   - [ ] A data actual en formato "ano-mes-día".
   - [ ] Un erro debido a unha mala sintaxe.

87. ¿Que devolverá o seguinte código Python?

   ```python
   from datetime import datetime, timedelta

   fecha_actual = datetime.now()
   nova_fecha = fecha_actual.replace(year=2025, month=1, day=1)
   print(nova_fecha.strftime('%Y-%m-%d'))
   ```

   - [ ] A data actual en formato "ano-mes-día".
   - [x] A data actual substituíndo o ano, mes e día por 2025-01-01.
   - [ ] A data actual en formato "día-mes-ano".
   - [ ] Un erro debido a unha mala sintaxe.

88. ¿Que devolverá o seguinte código Python?

   ```python
   from datetime import date, timedelta

   data_inicio = date(2024, 4, 1)
   data_fin = date(2024, 4, 15)
   duracion = data_fin - data_inicio
   print(duracion.days)
   ```

   - [x] A diferenza de días entre o 1 de abril de 2024 e o 15 de abril de 2024.
   - [ ] A diferenza de segundos entre o 1 de abril de 2024 e o 15 de abril de 2024.
   - [ ] A data actual en formato "ano-mes-día".
   - [ ] Un erro debido a unha mala sintaxe.

89. Considera o seguinte código Python:

   ```python
   from datetime import time, timedelta

   hora = time(10, 30)
   duracion = timedelta(hours=2, minutes=15)
   hora_final = hora + duracion
   ```

   ¿Qué representa `hora_final`?

   - [x] A hora 12:45.
   - [ ] A hora 10:45.
   - [ ] Un erro debido a unha mala sintaxe.
   - [ ] Un erro debido á operación non permitida entre `time` e `timedelta`.
   