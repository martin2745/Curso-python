---
title: "6.4. Comparación de cadeas e operador in"
weight: 4
---

## 6.4.1. Comparación de cadeas

Os operadores de comparación funcionan en cadeas. Para ver se dúas cadeas son iguais:

```python
if palabra == 'banana':
	print('Moi ben, bananas.')
```

Outras operacións de comparación son útiles para poñer palabras en orde alfabético:

```python
if palabra < 'banana':
	print('A tua palabra, ' + palabra + ', está antes de banana.')
elif palabra > 'banana':
	print('A tu palabra, ' + palabra + ', está despois de banana.')
else:
	print('Moi ben, bananas.')
```

Python non manexa letras maiúsculas e minúsculas da mesma forma que a xente fai. Todas as letras maiúsculas van antes que todas as letras minúsculas.

Unha forma común de manexar este problema é converter cadeas a un formato estándar, como todas as minúsculas, antes de levar a cabo a comparación.

## 6.4.2. Operador in

A palabra `in` é un operador booleano que toma dúas cadeas e regresa **True** se a primeira cadea aparece como unha subcadea da segunda:

```python
'a' in 'banana' # True
'semilla' in 'banana' # False
```