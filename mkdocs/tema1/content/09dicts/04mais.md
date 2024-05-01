---
title: "9.4. Dicionarios como argumento de funcións"
weight: 4
---

Debemos recordar que se modificamos un dicionario dentro dunha función, este modificase en todo o programa. 

Neste exemplo podemos observar o comportamento dos dicionarios e as funcións:

```python
def modificar_dicionario(dicionario):
	dicionario['clave'] = 'cambio_de_valor'

def engadir_clave(dicionario):
	dicionario['clave_nova'] = 'novo_valor'

def eliminar_clave(dicionario):
	del dicionario['clave']

dic = {'clave':'valor_inicial'}
print(dic)
modificar_dicionario(dic)
print(dic)
engadir_clave(dic)
print(dic)
eliminar_clave(dic)
print(dic)
```

A saída deste pequeno programa é a seguinte.

```bash
{'clave': 'valor_inicial'}
{'clave': 'cambio_de_valor'}
{'clave': 'cambio_de_valor', 'clave_nova': 'novo_valor'}
{'clave_nova': 'novo_valor'}
```



