---
title: "13.2. Grupo de captura"
weight: 2
---

Un grupo de captura en expresións regulares é unha parte da expresión regular que está entre parénteses. Estes grupos utilízanse para capturar subcadeas específicas que coinciden con este patrón dentro do texto de entrada.

Cando unha expresión regular encontra unha coincidencia, os grupos de captura permiten extraer e manipular partes especificar desa coincidencia.

Consideremos a seguinte expresión regular:

```
(\d{3})-(\d{3})-(\d{4})
```

En esta expresión regular, hay tres grupos de captura:

1. `(\d{3})`: Este grupo de captura captura tres díxitos.

2. `(\d{3})`: Outro grupo de captura tamén captura tres díxitos.

3. `(\d{4})`: Este grupo de captura captura catro díxitos.

Entón se aplicamos esta expresión regular ao texto `"123-456-7890"`, xerarase unha coincidencia e cada grupo de captura conterá a parte correspondente da cadea. É dicir, o primeiro grupo de captura contería `123`, o segundo `456` e o terceiro `7890`.