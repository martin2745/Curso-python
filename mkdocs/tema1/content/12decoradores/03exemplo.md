---
title: "12.3. Exemplo"
weight: 3
---

Aquí temos un exemplo dun decorador que imprime por pantalla o tempo de execución dunha función:

```python
import time

# Definimos un decorador para medir o tiempo de execución dunha función
def medir_tiempo(funcion):
    def wrapper(*args, **kwargs):
        
        ## Antes de executar a función
        inicio = time.time()  # Collemos o tempo de inicio
        
        # Chamamos a función a decorar e obtemos o resultado cos seus argumentos orixinais
        resultado = funcion(*args, **kwargs)

        ## Depois de executar a función
        fin = time.time()  # Capturamos o tempo de fin
        tempo_transcurrido = fin - inicio  # Calculamos o tiempo transcurrido
        print(f"A función {funcion.__name__} tardou {tiempo_transcurrido} segundos en executarse.")

        # Devolvemos o resultado orixinal da función a decorar
        return resultado
    return wrapper

# Definimos unha función e aplicamos o decorador
@medir_tiempo
def calcular_cadrado(numero):
    return numero ** 2

# Definimos unha función e aplicamos o decorador
@medir_tiempo
def calcular_cubo(numero):
    return numero ** 3
```

Neste exemplo cada vez que se invoquen e executen as funcións `calcular_cadrado(numero)` e `calcular_cubo(numero)` imprimirase o tempo transcorrido na súa execución. Este decorador pódese utilizar en calquera función.