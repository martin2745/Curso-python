---
title: "3.7. Depuración de expresións lóxicas"
weight: 7
---

Os ***traceback*** que Python mostra cando se produce un erro contén un montón de información, pero poden resultar abafadores. As partes máis útiles xeralmente son:

- Que tipo de erro se produciu
- Onde ocorreu

Os erros de sintaxe xeralmente son doados de localizar, pero a veces teñen trampa. Os erros debido a espazos en branco poden ser complicados, xa que os espazos e tabulacións son invisibles. E podemos ignoralos.

```python
>>> x = 5
>>>  y = 6
	File "<stdin>", line 1
     y = 6
     ^
IndentationError: unexpected indent
```

Neste exemplo, o problema é que a segunda liña está mal indentada por un espazo. Pero o mensaxe apunta a y, o cal pode resultar enganoso. En xeral, os mensaxes de erro indican onde se descubriu o problema, pero o erro real podería estar no código previo, e nalgúns casos nalgunha liña anterior.