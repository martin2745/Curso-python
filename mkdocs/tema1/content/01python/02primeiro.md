---
title: "1.2. Crear un programa en Python"
weight: 2
---

Podemos definir **programa** como unha secuencia de declaracións ou sentenzas que foron deseñadas para facer algo. Vamos a crear o noso primeiro programa en Python. Para iso abrimos un editor de texto e escribimos a mesma liña que fixemos no apartado anterior co intérprete.

```python
print("Ola mundo!")
```

Gardamos o arquivo co nome `ola.py`. A extensión ".py" indica que é un programa escrito en Python. Agora nun terminal escribimos o seguinte comando:

```bash
$ python3 ola.py
```

Deste xeito o intérprete de Python abre o noso arquivo e comeza a executar todas as liñas do arquivo de xeito secuencial. Como só contén unha liña executará unicamente unha instrución.

![captura1_2_1.png](captura1_2_1.png)

{{% notice style="note" title="Executable de Python en Windows" %}}

O comando para executar *scripts* de Python en Windows non é `python3` senón `py`. Polo tanto neste sistema operativo deberiamos escribir o seguinte comando:

```powershell
$ py ola.py
```

{{% /notice %}}

## 1.2.1. Cabeceiras Python

Un *script* en Python como o visto anteriormente é totalmente funcional.

Pero por convención xeralmente utilízanse unhas determinadas cabeceiras. Por exemplo as seguintes:

- A primeira liña debe de ser a seguinte: `#!/usr/bin/env python`. Nela indicamos que se trata dun *script* escrito en Python.

- A continuación pódese indicar a codificación. Por exemplo para utilizar UTF-8 podemos engadir a liña `# -*- coding: utf-8 -*-`. En Python 3 xa por defecto senón se indica nada se utiliza esta codificación.

- O seguinte debe ser unha descrición do *script* como comentario.

{{% notice style="blue" title="Comentarios" %}}

Os comentarios son fragmentos de texto que non se executan como código e sirven para proporcionar explicacións, notas ou documentación do código fonte.

A súa sintaxe é a seguinte:

- Os comentarios de unha liña en Python comenzan co símbolo `#`.

	```python
	# Este e un comentario
	```

- Os comentarios de varias liñas pódense crear mediante triple comillas (`'''` ou `"""`).
	
	```python
	'''
	Este e un comentario multiliña
	'''
	```

{{% /notice %}}


- A continuación impórtanse as librerías.

- E por último, antes de comezar o programa, inclúese a información de autoría. Non ten porque incluírse toda a información. Un exemplo desa información é a seguinte:

```python
__author__ = "Rob Knight, Gavin Huttley, and Peter Maxwell"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Rob Knight", "Peter Maxwell", "Gavin Huttley",
                    "Matthew Wakefield"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Rob Knight"
__email__ = "rob@spot.colorado.edu"
__status__ = "Production"
```

Polo tanto o programa anterior debería quedar do seguinte xeito:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Programa que imprime por pantalla a texto "Ola mundo!"

__author__ = "Manuel Ramón Varela López"

print("Ola mundo!")
```

## 1.2.2. Exemplo de programa: contar palabras dun texto

O programa escrito no apartado anterior é sinxelo, quizais o máis sinxelo que se pode escribir. Vamos complicalo un pouco. Necesitamos encontrar cal é a palabra que máis se usa dun texto. Podemos facelo a man, o que é moi laborioso ou escribir este programa:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Programa que conta o número de palabras dun ficheiro.

__author__ = "Manuel Ramón Varela López"


name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None

for word, count in list(counts.items()):
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print(bigword, bigcount)
```

Este pequeno programa contén moitas instrucións que de momento non podemos entender. Pero iso non significa que non o poidamos utilizar. Se gardamos as liñas anteriores nun arquivo denominado `words.py` poderemos executalo nunha terminal do seguinte xeito:

```bash
$ python3 words.py
```

O programa preguntaranos pola ruta do arquivo co texto que queremos analizar e posteriormente analizarao e proporcionaranos a palabra máis común e o seu número de aparicións.

Aquí un exemplo de texto que gardamos no arquivo `historia_python.txt` que será o que analicemos.

```vim
Python fue creado a finales de los ochenta4 por Guido van Rossum en el Centro para las Matemáticas y la Informática (CWI, Centrum Wiskunde & Informatica), en los Países Bajos, como un sucesor del lenguaje de programación ABC, capaz de manejar excepciones e interactuar con el sistema operativo Amoeba.
El nombre del lenguaje proviene de la afición de su creador por los humoristas británicos Monty Python.
Van Rossum es el principal autor de Python, y su continuo rol central en decidir la dirección de Python es reconocido, refiriéndose a él como Benevolente Dictador Vitalicio (en inglés: Benevolent Dictator for Life, BDFL); sin embargo el 12 de julio de 2018 declinó de dicha situación de honor sin dejar un sucesor o sucesora y con una declaración altisonante:
Entonces, ¿qué van a hacer todos ustedes? ¿Crear una democracia? ¿Anarquía? ¿Una dictadura? ¿Una federación?
En 1991, van Rossum publicó el código de la versión 0.9.0 en alt.sources. En esta etapa del desarrollo ya estaban presentes clases con herencia, manejo de excepciones, funciones y los tipos modulares, como: str, list, dict, entre otros. Además en este lanzamiento inicial aparecía un sistema de módulos adoptado de Modula-3; van Rossum describe el módulo como «una de las mayores unidades de programación de Python». El modelo de excepciones en Python es parecido al de Modula-3, con la adición de una cláusula else. En el año 1994 se formó comp.lang.python, el foro de discusión principal de Python, marcando un hito en el crecimiento del grupo de usuarios de este lenguaje.
Python alcanzó la versión 1.0 en enero de 1994. Una característica de este lanzamiento fueron las herramientas de la programación funcional: lambda, reduce, filter y map. Van Rossum explicó que «hace 12 años, Python adquirió lambda, reduce(), filter() y map(), cortesía de Amrit Perm, un hacker informático de Lisp que las implementó porque las extrañaba».
La última versión liberada proveniente de CWI fue Python 1.2. En 1995, van Rossum continuó su trabajo en Python en la Corporation for National Research Initiatives (CNRI) en Reston, Virginia, donde lanzó varias versiones del software.
Durante su estancia en CNRI, van Rossum lanzó la iniciativa Computer Programming for Everybody (CP4E), con el fin de hacer la programación más accesible a más gente, con un nivel de 'alfabetización' básico en lenguajes de programación, similar a la alfabetización básica en inglés y habilidades matemáticas necesarias por muchos trabajadores. Python tuvo un papel crucial en este proceso: debido a su orientación hacia una sintaxis limpia, ya era idóneo, y las metas de CP4E presentaban similitudes con su predecesor, ABC. El proyecto fue patrocinado por DARPA. En el año 2007, el proyecto CP4E está inactivo, y mientras Python intenta ser fácil de aprender y no muy arcano en su sintaxis y semántica, alcanzando a los no-programadores, no es una preocupación activa.
En el año 2000, el equipo principal de desarrolladores de Python se cambió a BeOpen.com para formar el equipo BeOpen PythonLabs. CNRI pidió que la versión 1.6 fuera pública, continuando su desarrollo hasta que el equipo de desarrollo abandonó CNRI; su programa de lanzamiento y el de la versión 2.0 tenían una significativa cantidad de traslapo. Python 2.0 fue el primer y único lanzamiento de BeOpen.com. Después que Python 2.0 fuera publicado por BeOpen.com, Guido van Rossum y los otros desarrolladores de PythonLabs se unieron en Digital Creations.
Python 2.0 tomó una característica mayor del lenguaje de programación funcional Haskell: listas por comprensión. La sintaxis de Python para esta construcción es muy similar a la de Haskell, salvo por la preferencia de los caracteres de puntuación en Haskell, y la preferencia de Python por palabras claves alfabéticas. Python 2.0 introdujo además un sistema de recolección de basura capaz de recolectar referencias cíclicas.
Posterior a este doble lanzamiento, y después que van Rossum dejara CNRI para trabajar con desarrolladores de software comercial, quedó claro que la opción de usar Python con software disponible bajo GNU GPL era muy deseable. La licencia usada entonces, la Python License, incluía una cláusula estipulando que la licencia estaba gobernada por el estado de Virginia, por lo que, bajo la óptica de los abogados de Free Software Foundation (FSF), se hacía incompatible con GPL. Para las versiones 1.61 y 2.1, CNRI y FSF hicieron compatibles la licencia de Python con GPL, renombrandola Python Software Foundation License. En el año 2001, van Rossum fue premiado con FSF Award for the Advancement of Free Software.
Python 2.1 fue un trabajo derivado de las versiones 1.6.1 y 2.0. Es a partir de este momento que Python Software Foundation (PSF) pasa a ser dueño del proyecto, organizada como una organización sin ánimo de lucro fundada en el año 2001, tomando como modelo la Apache Software Foundation. Incluido en este lanzamiento fue una implementación del scoping más parecida a las reglas de static scoping (del cual Scheme es el originador).
Una innovación mayor en Python 2.2 fue la unificación de los tipos en Python (tipos escritos en C), y clases (tipos escritos en Python) dentro de una jerarquía. Esa unificación logró un modelo de objetos de Python puro y consistente. También fueron agregados los generadores que fueron inspirados por el lenguaje Icon.
Las adiciones a la biblioteca estándar de Python y las decisiones sintácticas fueron influenciadas fuertemente por Java en algunos casos: el package logging, introducido en la versión 2.3, está basado en log4j; el parser SAX, introducido en 2.0; el package threading, cuya clase Thread expone un subconjunto de la interfaz de la clase homónima en Java.
Python 2, es decir Python 2.7.x, fue oficialmente descontinuado el 1 de enero de 2020 (primero planeado para 2015) después de lo cual no se publicarán parches de seguridad y otras mejoras para él. Con el final del ciclo de vida de Python 2, solo tienen soporte la rama Python 3.5.x y posteriores.
En la actualidad, Python se aplica en los campos de inteligencia artificial y machine learning.
```

Vemos un exemplo da execución:

![captura1_2_2.png](captura1_2_2.png)

Este é un bo exemplo de como Python e a linguaxe Python actúan como intermediario entre o usuario final e o programador. Python é un medio para que intercambiemos secuencias de instrucións útiles (programas) nunha linguaxe común que pode ser usado por calquera. Polo tanto usamos Python para comunicarnos entre nos os programadores e os usuarios dos programas.