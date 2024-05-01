---
title: "2.4. Orde de operacións"
weight: 4
---

Cando nunha instrución aparece máis dun operador, a orde de avaliación depende das **regras de precedencia**. Para os operadores matemáticos, Python segue as convencións matemáticas.

- Os parénteses teñen un nivel superior de precedencia, e poden usarse para forzar a que unha expresión sexa avaliada na orde que se queira. Dado que as expresións entre parénteses son avaliadas primeiro, `2 * (3-1)` é 4 e `(1+1)**(5-2)` é 8. Pódense utilizar parénteses para facer unha expresión máis sinxela de ler, incluso se o resultado da mesma non varía, como por exemplo `(minuto * 100) / 60`.

- A potenciación ten o seguinte nivel máis alto de precedencia. Deste xeito `2**1+1` é 3, non 4; e `3*1**3` é 3, non 27.

- A multiplicación e a división teñen a mesma precedencia, que é superior a da suma e a da resta, as cales teñen tamén o mesmo nivel de precedencia. Así que `2*3-1` é 5, non 4; e `6+4/2` é 8, non 5.

- Os operadores con igual precedencia son avaliados de esquerda a dereita. Así a expresión `5-3-1` é 1, non 3, porque `5-3` avalíase antes.

En caso de dúbida, engade sempre parénteses as túas expresións para asegurarte de que as operacións realízanse na orde que queres.