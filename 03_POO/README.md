# POO - Programación Orientada a Objetos

## Conceptos
La Programación Orientada a Objetos (POO) es un paradigma de programación que utiliza "objetos" para organizar el código. Python es un lenguaje de programación multiparadigma, que permite el enfoque de POO. En la POO tenemos que destacar dos conceptos en un primer momento:
    
- **Clase:** Una clase es una plantilla o un plano para crear objetos. En términos más sencillos, puedes pensar en una clase como un conjunto de instrucciones que describe cómo crear un objeto. Define las propiedades y comportamientos comunes a todos los objetos de ese tipo. Aunque enPython empleamos snake_case, en la declaración de clases emleamos PascalCase.
- **Objeto:** Un objeto es una instancia única de una clase. Se crea utilizando la plantilla proporcionada por la clase. Cada objeto tiene sus propias características, pero comparte comportamientos comunes con otros objetos de la misma clase.

### Importancia de usar POO

La elección entre programación orientada a objetos (POO) en lugar de otros paradigmas como la programación estructurada que hemos visto en los capitolos anteriores depende del contexto del problema a resolver y de las preferencias del programador. Ambos paradigmas tienen sus propias ventajas y desventajas. Aquí hay algunas razones para considerar el uso de la programación orientada a objetos en lugar de la programación estructurada:

- **Reutilización de código:** La POO fomenta la reutilización de código mediante el uso de conceptos como la herencia. Puedes crear clases base con funcionalidades comunes y luego heredar esas funcionalidades en clases derivadas, evitando así la duplicación de código.

- **Abstracción:** La POO permite la abstracción, lo que significa que puedes modelar objetos del mundo real y sus interacciones de manera más natural. Esto hace que el código sea más comprensible y más cercano a la forma en que pensamos sobre los problemas.

- **Encapsulamiento:** La encapsulación en POO ayuda a ocultar la implementación interna de los objetos y exponer solo lo que es necesario. Esto facilita el mantenimiento del código y mejora la modularidad al reducir las dependencias. Tenemos diferentestipos de atributos     

  - Atributo Público:
        Acceso: Se puede acceder y modificar desde cualquier parte del programa, ya sea dentro de la misma clase, en clases derivadas (herencia) o desde cualquier otra parte del código.

  -  Atributo Protegido:
        Acceso: Se puede acceder y modificar dentro de la misma clase y también desde clases derivadas (herencia). No se puede acceder desde fuera de la clase o la jerarquía de herencia.

  -  Atributo Privado:
        Acceso: Solo se puede acceder y modificar dentro de la misma clase. No se puede acceder desde clases derivadas ni desde fuera de la clase.

- **Jerarquía y herencia:** La herencia permite organizar las clases en una jerarquía, lo que facilita la comprensión de la estructura del código. Además, la herencia permite extender y especializar comportamientos sin modificar la clase base.

- **Polimorfismo:** En programación orientada a objetos (POO), el polimorfismo es un principio que permite a un objeto ser tratado como un objeto de su clase base. En Python, el polimorfismo se logra mediante la capacidad de un objeto para tomar muchas formas o clases diferentes.

- **Manejo de complejidad:** En POO este termino se refiere a la capacidad de un objeto se comporte de diferentes maneras según el contexto en el que se utilice. En términos más sencillos, el polimorfismo permite que objetos de distintas clases sean tratados de manera uniforme si comparten una interfaz común o heredan de una misma clase base.

- **Modelado más cercano a la realidad:** La POO se basa en el modelado de entidades del mundo real, lo que puede hacer que el código sea más intuitivo y fácil de entender, especialmente para problemas que se pueden representar naturalmente como objetos.

### Herencia

La herencia es uno de los conceptos fundamentales de la programación orientada a objetos (POO) en Python y en muchos otros lenguajes de programación. En Python, la herencia permite a una clase heredar atributos y métodos de otra clase, lo que facilita la reutilización de código y la creación de jerarquías de clases.

En términos simples, una clase hija puede heredar características (atributos y métodos) de una clase padre. La clase padre se conoce como la clase base o superclase, mientras que la clase hija se llama subclase. La subclase puede agregar nuevos métodos o modificar los existentes, y también puede tener sus propios atributos.

A diferencia de otros lenguajes como Java, Python permite herencia múltiple, lo que significa que una clase puede heredar atributos y métodos de más de una clase base. Esta característica permite la creación de jerarquías de clases más complejas y la reutilización de código de varias fuentes.

Cuando una clase hereda de múltiples clases, se coloca una lista de las clases base en la declaración de la clase. A continuación, se muestra un jemplo simple:

```python
    class ClaseA:
        def metodo_A(self):
            print("Método A de ClaseA")

    class ClaseB:
        def metodo_B(self):
            print("Método B de ClaseB")

    class ClaseC(ClaseA, ClaseB):
        def metodo_C(self):
            print("Método C de ClaseC")

    # Crear una instancia de la clase que hereda de ambas ClaseA y ClaseB
    objeto_c = ClaseC()

    # Utilizar métodos de ambas clases base
    objeto_c.metodo_A()  # Salida: Método A de ClaseA
    objeto_c.metodo_B()  # Salida: Método B de ClaseB
    objeto_c.metodo_C()  # Salida: Método C de ClaseC
```

### MRO

MRO (Method Resolution Order) en Python determina el orden en el que se buscan los métodos en las clases cuando hay herencia múltiple. Aquí tienes un ejemplo sencillo con cuatro clases A, B, C y D:

```python
class A:
    def saludar(self):
        print("Hola desde A")

class B(A):
    def saludar(self):
        print("Hola desde B")
        super().saludar()

class C(A):
    def saludar(self):
        print("Hola desde C")
        super().saludar()

class D(B, C):
    def saludar(self):
        print("Hola desde D")
        super().saludar()

# Crear una instancia de la clase D
instancia_d = D()

# Llamar al método saludar de la clase D
instancia_d.saludar()
```

En este ejemplo, la clase D hereda de las clases B y C, que a su vez heredan de la clase A. La MRO en este caso seguiría el orden de herencia de izquierda a derecha, es decir, primero buscará en la clase B, luego en la clase C, y finalmente en la clase A. La salida esperada sería:
- Hola desde D
- Hola desde B
- Hola desde C
- Hola desde A

Ten en cuenta que la función super() se utiliza para llamar al método de la clase base en la jerarquía de herencia. En este caso, super().saludar() se encarga de llamar al método saludar de la clase inmediatamente superior en la MRO.

### Decoradores y propiedades

En Python, un decorador es una función especial que se utiliza para modificar el comportamiento de otra función o método. Los decoradores permiten extender o modificar la funcionalidad de funciones existentes sin cambiar su código interno. Se aplican usando la sintaxis @decorador justo encima de la definición de la función o método que se va a decorar.

El decorador @property es comúnmente utilizado para crear propiedades en clases. En lugar de utilizar métodos tradicionales para acceder y modificar atributos, se pueden utilizar propiedades para proporcionar una interfaz más clara y legible, similar a la sintaxis de acceso a atributos públicos.

En particular, @property se utiliza para convertir un método en una propiedad de solo lectura. Cuando se usa este decorador, el método se puede acceder como si fuera un atributo, sin necesidad de llamarlo como una función. Además, se puede utilizar @property.setter para definir un método que se llamará cuando se intente asignar un valor a la propiedad.

Aquí hay un resumen de cómo funciona @property:

**@property:** Se aplica al método que actuará como getter. Permite acceder al método como si fuera un atributo, sin necesidad de llamarlo como una función.

**@property.setter:** Se aplica al método que actuará como setter. Permite asignar un valor a la propiedad utilizando la sintaxis de asignación (objeto.propiedad = valor).