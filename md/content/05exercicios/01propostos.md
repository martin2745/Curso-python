---
title: "5.1. Enunciados"
weight: 1
---

1. Escribe unha función que conte a cantidade de ficheiros dun directorio dado por argumento. Deberá devolver a cantidade.

2. Escribe unha función que busque os arquivos con unha extensión específica nun directorio. Recibirá como parámetro obrigatorio a extensión e como opcional a ruta dun directorio. Se non se pasa este dato utilizarase o directorio actual. Devolve unha lista de nomes de ficheiros.

3. Modifica o exercicio anterior para que ademais se realice unha busca nos subdirectorios do directorio.

4. Escribe unha función que elimine os arquivos dun directorio se teñen máis dunha cantidade de días. Recibirá como parámetro obrigatorio a cantidade de días como un enteiro e como opcional a ruta dun directorio. Se non se pasa este dato utilizarase o directorio actual. 

5. Escribe unha función no que a tódolos ficheiros se lles engada a extensión "backup" dun directorio dado por parámetros.

6. Escribe unha función que devolva o ficheiro máis grande dentro do directorio actual e os seus subdirectorios. Débese de utilizar recursividade para simplificar dito algoritmo. A función devolverá a ruta absoluta do ficheiro.

7. Escribe unha función que reciba a ruta dun directorio e unha cadea de texto. Esta debe buscar en que ficheiros ".txt" se encontra dito texto como contido. Debe devolver unha lista con tódolos nomes deses ficheiros.

8. Escribe unha función que substitúa unha palabra dun ficheiro de texto por outra. A función recibirá a ruta do ficheiro, a palabra a substituír e o texto co se realizará o cambio.

9. Crea un *script* que a partir dun ficheiro CSV cree usuarios nun sistema Linux. O nome de usuario será a primeira letra do seu nome seguido do apelido, todo en minúscula. Se dous usuarios tiveran o mesmo nome de usuario, engádelle ao final o número 1. Se volverá haber máis coincidencias, en lugar do 1 ponlle o número 2, e así sucesivamente. O ficheiro CSV ten o seguinte formato:

```csv
nome,apelido
Juan,Perez
Maria,Gonzalez
Carlos,Rodriguez
Jose,Perez
```

10. A partir do ficheiro CSV anterior, crea os directorios "home" de cada usuario antes de engadilos usuarios. Asígnalle dito directorio na súa creación e por último cambia o usuario propietario de dito directorio.

11. Fai o exercicio anterior, pero en lugar de obtela información dun ficheiro CSV faino a partir deste ficheiro JSON.

```json
[
    {"nome": "Juan", "apelido": "Perez"},
    {"nome": "Maria", "apelido": "Gonzalez"},
    {"nome": "Carlos", "apelido": "Rodriguez"},
    {"nome": "Jose", "apelido": "Perez"}
]
```

12. Crea un *script* que copie tódolos ficheiros do sistema coa extensión "py" no directorio "python". Debes comprobar se existe este directorio, e se existe borrar todo o seu contido. Fai que o *script* se poida executar en Windows e en Linux. Podes axudarte desta función para obter tódalas unidades en Windows.

```python
def obtener_unidades_windows():
    unidades = []
    # Recorremos as letras de unidades da A a Z
    for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        unidade = f"{letra}:\\"
        # Verificamos se a unidade existe como directorio
        if os.path.isdir(unidade):
            unidades.append(unidade)
    return unidades
```

13. Crea unha función en Python para realizar unha copia de seguridade dun directorio. Débese gardar cada copia de seguridade nun arquivo comprimido que terá como nome o día, mes e ano do momento no que se execute. A función recibirá a carpeta da que se fará a copia de seguridade e o directorio donde se almacenará dita copia.

14. A partir do ficheiro `/etc/fstab` e utilizando expresións regulares, crea unha función en Python no que se obteñan tódolos dispositivos montados e o seu punto de montaxe a través deste ficheiro. Devolve esta información nunha lista de dicionarios.

15. Fai un *script* con dúas funcións que permitirá eliminar arquivos duplicados nun directorio:

- `obter_hash(directorio)`: a partir dun directorio que recibe como argumento, devolve un dicionario onde cada clave e o *hash* do contido dos ficheiros do directorio e o seu valor é unha lista coa ruta absoluta de cada un dos ficheiros que contén con ese *hash*. No seguinte exemplo explícase como obter o *hash* dun ficheiro.

```python
import hashlib

# rb permite ler un ficheiro en binario
with open(ruta_absoluta, 'rb') as archivo:
    contenido = archivo.read()
    # isto devolve o hash do ficheiro
    hash_archivo = hashlib.sha256(contenido).hexdigest()
```

- `eliminar_duplicados(directorio)`: a partir da información do dicionario anterior elimina os arquivos duplicados. Almacena nun ficheiro `eliminados.log` tódolos arquivos eliminados. 

16. Fai unha función en Python que instale un paquete utilizando `apt-get` sen utilizar a opción `-y`. Antes da instalación executa `apt-get update` O nome do paquete debe de pasárselle como argumento a función.