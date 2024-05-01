---
title: "14.6. De texto a datas e viceversa"
weight: 6
---

### 14.6.1. De data a texto

Exemplos de converter unha data en formato texto:

```python
# Formatear data como cadea
fecha_formateada = fecha.strftime("%Y-%m-%d")
print(fecha_formateada)

# Formatear hora como cadea
hora_formateada = hora.strftime("%H:%M:%S")
print(hora_formateada)
```
### 14.6.2. De texto a data

Para crear un obxecto de data ou hora a partir de texto, pódese utilizar o método `strptime()`.

Exemplo

```python
from datetime import datetime

# Cadea de texto que representa unha data
fecha_texto = "2023-04-01"

# Crea un objeto de data a partir do texto
fecha = datetime.strptime(fecha_texto, "%Y-%m-%d")

print(fecha)
```

Se a cadea non se axusta o formato especificado, producirase un erro `ValueError`.


### 14.6.3. Comodíns

Tano en `strftime()` como `strptime()` é necesario o uso de certos comodíns para especificar o formato.

Algún dos comodíns son os seguintes:


- `%Y`: Ano como un número decimal de catro díxitos.

- `%m`: Mes como un número decimal de dous díxitos (01 a 12).

- `%d`: Día do mes como un número decimal de dous díxitos (01 a 31).

- `%H`: Hora (reloxo de 24 horas) como un número decimal de dous díxitos (00 a 23).

- `%M`: Minuto como un número decimal de dous díxitos (00 a 59).

- `%S`: Segundo como un número decimal de dous díxitos (00 a 59).

- `%a`: Nome abreviado do día da semana.

- `%A`: Nome completo do día da semana.

- `%b`: Nome abreviado do mes.

- `%B`: Nome completo do mes.

- `%p`: AM ou PM para reloxo de 12 horas.

