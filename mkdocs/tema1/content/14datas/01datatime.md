---
title: "14.1. Clase datetime"
weight: 1
---

A clase `datetime` representa unha data e horas específicas incluíndo información sobre o ano, mes, día, hora, minuto, segundo e microsegundo.

É a clase máis completa de `datetime`.

O construtor é o seguinte:

```python
datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0)
```

### 14.1.1. Métodos


- `now()`: Retorna un obxecto `datetime` coa data e hora actuais.

- `strftime(format)`: Formatea o obxecto `datetime` como una cadea utilizando o formato especificado no parámetro `format`.

- `strptime(date_string, format)`: Converte una cadea de texto nun obxecto `datetime` segundo o formato especificado.

- `fromtimestamp(timestamp)`: converte un *timestamp* nun obxecto `datetime`. 