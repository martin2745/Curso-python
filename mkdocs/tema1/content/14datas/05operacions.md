---
title: "14.5. Operacións"
weight: 5
---

A clase `datetime.timedelta` representa un período de tempo, expresado como unha diferenza entre dous obxectos de `datetime`, `date` o `time`. É útil para realizar operacións aritméticas con datas e horas, como sumar ou restar intervalos de tempo a unha data ou hora.

### 14.5.1. Creación de obxectos

Para crear un obxecto `timedelta`debemos especificar o tempo que se desexa representar.

```python
from datetime import timedelta

# Crea un timedelta de 5 días
delta = timedelta(days=5)

# Crear un timedelta de 3 horas, 30 minutos e 10 segundos
delta_otro = timedelta(hours=3, minutes=30, seconds=10)
```

Tamén se pode crear un `timedelta` calculando a diferenza entre dous obxectos `datetime`, `date` ou  `time`:


```python
from datetime import datetime, timedelta

inicio = datetime(2024, 4, 1)
fin = datetime(2024, 4, 10)

# Calcula a diferenza entre as dúas datas
delta = fin - inicio
```

Esta clase tamén ten os atributos como `datetime`, `date` ou  `time` para acceder aos anos, meses, etc.

### 14.5.2. Operacións

Pódense realizar operacións aritméticas con obxectos `timedelta`, como sumar ou restar a un obxecto`datetime`, `date` o `time`:


```python
from datetime import datetime, timedelta

inicio = datetime(2024, 4, 1)
delta = timedelta(days=5)

# Suma o timedelta a unha data
nueva_fecha = inicio + delta

# Resta o timedelta a unha data
fecha_anterior = inicio - delta
```

O método `replace()` utilízase para crear unha nova data (ou dia ou hora) con valores substituídos. Devolve un novo obxecto con valores novos, non modifica o orixinal.

Exemplo:

```python
from datetime import datetime

fecha_hora = datetime(2022, 4, 8, 12, 30, 15)

nueva_fecha_hora = fecha_hora.replace(year=2023, hour=10)

print("Fecha e hora orixinal:", fecha_hora)
print("Nova fecha e hora:", nova_fecha_hora)
```