---
title: "4.6. Funcións produtivas e esteriles"
weight: 6
---

Algunhas funcións que estamos usando producen resultados, como as matemáticas, estas ímolas coñecer como **funcións produtivas**. Outras funcións, como `mostra_duas_veces`, realizan unha acción pero non devolven ningún valor. A estas chamarémolas **funcións estériles**.

Cando chamas a unha función produtiva, case sempre quererás facer logo algo co resultado; por exemplo, pode que queiras asignalo a unha variable ou usalo como parte dunha expresión.

```python
x = math.cos(radians)
aurea = (math.sqrt(5) + 1) / 2
```

As funcións estériles poden mostrar algo por pantalla, ou ter calquera outro efecto, pero non devolven un valor. Se intentas asignar o resultado a unha variable, obterás un valor especial chamado **None**.

```python
resultado = mostra_duas_veces('Bing')
'''
Bing
Bing
'''
print(resultado) # Imprime: None
```

Para devolver un resultado dende unha función, usamos a sentenza `return` dentro dela. Por exemplo, podemos crear unha función muy simple chamada `sumador`, que suma dous números e devolve o resultado.

```python
def sumador(a, b):
	suma = a + b
	return suma
x = sumador(3, 5)
print(x) # Imrpime: 8
```

## 4.6.1. Devolver múltiples valores

Python permite devolver múltiples valores dende unha función utilizando tuplas. Exemplo:


```python
def funcion_multiples_valores():
    resultado1 = "Ola"
    resultado2 = 42
    resultado3 = [1, 2, 3]
	# Devolve unha tupla con varios valores
    return resultado1, resultado2, resultado3
```

Para recoller os múltiples valores tras a execución da función, podemos realizalo do seguinte xeito:

```python
valor1, valor2, valor3 = funcion_multiples_valores()

print(valor1) # Imprime: Hola
print(valor2) # Imprime: 42
print(valor3) # Imprime: [1, 2, 3]
```
