---
title: "4.3. Fluxo de execución"
weight: 3
---

Para asegurarnos de que unha función está definida antes de usala por primeira vez, é necesario saber a orde na que as sentenzas son executadas, que é o que chamamos **fluxo de execución**.

A execución sempre comeza na primeira sentenza do programa. As sentencias son executadas unha por unha, de arriba a abaixo.

As **definicións** de funcións non alteran o fluxo de execución do programa, pero recorda que **as sentenzas dentro dunha función non son executadas ata que se chame a esa función**.

Unha chamada a unha función é como un desvío no fluxo de execución. En vez de pasar a seguinte sentenza, o fluxo salta ao corpo da función, executa todas as sentenzas que hai alí, e despois volve ao punto onde o deixou.

Todo isto parece bastante sinxelo, ata que un recorda que unha función pode chamar a outra. Cando está en metade dunha función o programa pode ter que executar sentenzas doutra función.

Python é capaz de levar o seguimento de onde se encontra en cada momento, de xeito que cada vez que completa unha execución dunha función, o programa volve o punto onde deixou a función que chamou a esa.

Polo tanto, cando leas un programa non terás que ler de arriba a abaixo. O que máis sentido ten é seguir o fluxo do programa.


