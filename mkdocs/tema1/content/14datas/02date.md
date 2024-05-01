---
title: "14.2. Clase date"
weight: 2
---

A clase `date` representa só unha data, sen información sobre a hora. É útil cando só se necesita traballar con datas e non importa a hora do día.

O construtor:

```python
date(year, month, day)
```

### 14.2.1. Métodos

- `today()`: Devolve un obxecto `date` coa data actual.

- `strftime(format)`: Formatea o obxecto `date` como unha cadea utilizando o formato especificado.

- `strptime(date_string, format)`: Converte unha cadea de texto nun obxecto `date` segundo o formato especificado.
