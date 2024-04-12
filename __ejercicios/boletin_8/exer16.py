#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fai unha función en Python que instale un paquete utilizando `apt-get` sen utilizar a opción `-y`. Antes da instalación executa `apt-get update` O nome do paquete debe de pasárselle como argumento a función.

__author__ = "Martín Gil Blanco"

import subprocess

def comando_iterativo(comando, lista_respostas=[]):

    # Creamos o comando en forma de lista
    comando_lista = comando.split(" ")

    # Crea un obxecto Popen para executar o comando
    proceso = subprocess.Popen(comando_lista, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Recorremos todalas respostas proporcionadas
    for resposta in lista_respostas:
        # Enscribimos a respostas
        proceso.stdin.write(resposta + '\n')
        # Aseguramos de que a entrada se envía correctamente
        proceso.stdin.flush()

    # Obtense a saida e erros do proceso
    saida, erros = proceso.communicate()

    # Cerra a entrada estándar do proceso
    proceso.stdin.close()

    # Imprimir a salida y errores
    print("Saida do comando:")
    print(saida)

    print("\nErros do comando:")
    print(erros)

def instalar_paquete(paquete):
    comando_update = "apt-get update"
    comando_instalar = "apt-get install " + paquete
    lista_respostas =  ["S"]
    comando_iterativo(comando_update)
    comando_iterativo(comando_instalar, lista_respostas)

instalar_paquete("apache2")

