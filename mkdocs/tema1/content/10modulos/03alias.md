---
title: "10.3. Alias"
weight: 3
---

Os **alias** ao importar en Python son utilizados para proporcionar un nome alternativo a un módulo, función ou variable importada. Isto pode ser útil para:

- **Evitar conflitos de nomes**. Por exemplo se os nomes do módulo importado entran en conflito con nomes do teu código actual.

- **Facilitar a escritura de código**. Se os nomes de módulos son longos, podemos utilizar alias máis curtos para facilitar a escritura de código.

Exemplos:

```python
import numpy as np
import pandas as pd

np.array([1, 2, 3])
```