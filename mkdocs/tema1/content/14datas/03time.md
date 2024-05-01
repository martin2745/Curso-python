---
title: "14.3. Clase time"
weight: 3
---

A clase `time` representa só unha hora do día, sen información sobre a data.

O construtor:

```python
time(hour=0, minute=0, second=0, microsecond=0)
```

### 14.3.1. Métodos

- `now()`: Retorna un obxecto `time` coa hora actual.

- `strftime(format)`: Formatea o obxecto `time` como unha cadea utilizando o formato especificado.

- `strptime(time_string, format)`: Converte unha cadea de texto nun obxecto `time` segundo o formato especificado.
