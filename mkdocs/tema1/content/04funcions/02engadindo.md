---
title: "4.2. Definición e uso de novas funcións"
weight: 2
---

## 4.2.1. Definición

Ata agora, só usamos funcións que veñen incorporadas en Python, pero é posible engadir tamén funcións novas. Unha **definición de función** especifica o nome dunha función nova e a secuencia de sentenzas que se executan cando esa función é chamada. Unha vez definida unha función, pódese reutilizar unha vez e outra ao longo de todo o programa.

Aquí un exemplo:

```python
def mostrar_estribillo():
	print('Son un leñador, qué alegría.')
	print('Durmo toda a noite e traballo todo o día.')
```

**def** é unha palabra reservada que indica que se trata da definición dunha función. O nome da función é `mostrar_estribillo`. As regras para os nomes das funcións son os mesmos que para as variables. Pódense usar letras, números e algúns signos de puntuación, pero o primeiro carácter non pode ser un número. Non se pode usar unha palabra clave como nome dunha función, e deberíase evitar tamén unha variable e unha función co mesmo nome.

As parénteses baleiras despois do nome indican que esta función non toma ningún argumento. Máis tarde construiremos funcións que reciban argumentos de entrada.

A primeira liña de definición dunha función é chamada **cabeceira**. O resto chámase **corpo**. A cabeceira debe rematar con dous puntos (:), e o corpo debe ir tabulado. O corpo pode conter calquera número de sentenzas.

Ao definir unha función créase unha variable co mesmo nome.

```python
print(mostrar_estribillo) # <function mostrar_estribillo at 0xb7e99e9c>
print(type(mostrar_estribillo)) # <type 'function'>
```

O valor de **mostrar_estribillo** é *function object*, que ten como tipo **function**.

## 4.2.2. Uso de novas funcións

A sintaxe para chamar a nosa nova función é a mesma que usamos para as funcións internas:

```python
mostrar_estribillo()
'''
Son un leñador, qué alegría.
Durmo toda a noite e traballo todo o día.
'''
```

Unha vez que se definiu unha función, pode usarse dentro de outra. Por exemplo, para repetir o estribillo anterior. Poderíamos escribir unha función chamada `repite_estribillo`.

```python
def repite_estribillo():
	mostrar_estribillo()
	mostrar_estribillo()
```

E despois chamar a esa función:

```python
repite_estribillo()
'''
Son un leñador, qué alegría.
Durmo toda a noite e traballo todo o día.
Son un leñador, qué alegría.
Durmo toda a noite e traballo todo o día.
'''
```

## 4.2.3. Exemplo de definicións e uso de funcións nun script

Reunindo os fragmentos de código das seccións anteriores, o programa completo sería algo como isto:

```python
def mostrar_estribillo():
	print('Son un leñador, qué alegría.')
	print('Durmo toda a noite e traballo todo o día.')

def repite_estribillo():
    muestra_estribillo()
    muestra_estribillo()

repite_estribillo()
```

Este programa contén dúas definicións de funcións: `mostrar_estribillo` e `repite_estrebillo`. As definicións son executadas exactamente igual que calquera outra sentenza, pero o seu resultado consiste en crear obxectos do tipo función. As sentenzas dentro de cada función son executadas soamente cando se chama a esa función, e a definición dunha función non xera ningunha saída.

Como xa te imaxinarás, **é necesario crear unha función antes de que se poida executar**. Noutras palabras, a definición da función debe ser executada antes que se chame por primeira vez.

