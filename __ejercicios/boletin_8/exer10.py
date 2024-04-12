#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A partir do ficheiro CSV anterior, crea os directorios "home" de cada usuario antes de engadilos usuarios. Asígnalle dito directorio na súa creación e por último cambia o usuario propietario de dito directorio.


# Executarse con sudo para poder crear os directorios home
# sudo python3 exer10.py ... 


__author__ = "Martín Gil Blanco"

import os
import sys
import csv
import subprocess
import pwd

# Comprobamos que haxa dous parametros
if len(sys.argv) != 2:
    print("Engade os parametros necesarios")
    exit()

# Collemos o primeiro parametro que e a ruta do ficheiro CSV
ruta = sys.argv[1]

# Lista cos usuarios
usuarios = []

# Abrimos o ficheiro CSV
with open(ruta, "r") as ficheiro:
    # Lemolo como unha lista de dicionarios
    lector_csv = csv.DictReader(ficheiro)

    # Recorremos cada fila do ficheiro CSV
    for fila in lector_csv:
        # Collemos o nome e apelido en minusculas
        nome = fila["nome"].lower()
        apelido = fila["apelido"].lower()

        # Construimos o nome de usuario
        nome_usuario = nome[0] + apelido

        # Comprobamos se o nome ainda non esta na lista de usuaris
        if nome_usuario not in usuarios:
            # Engadimos a lista de usuarios o novo nome de usuarios
            usuarios.append(nome_usuario)
        else:
            # Debemos arranxar o problema de repeticion de nome de usuarios
            i = 1
            # Facemos un while True, para comprobar usuarios ata atopar un non utilizado
            while True:
                # Creamos o novo nome de usuario
                nome_composto = nome_usuario + str(i)
                # Comprobamos se esta o nome na lista de usuarios
                if nome_composto not in usuarios:
                    # Se non esta gardamolo e salimos do bucle While con break
                    usuarios.append(nome_composto)
                    break
                # Probamos co seguinte numero
                i += 1


# Recorremos a lista de usuarios
for nome_usuario in usuarios:
    # Creamos os directorios
    ruta_home_usuario = os.path.join("/home",nome_usuario)
    print(ruta_home_usuario)
    os.mkdir(ruta_home_usuario)

    # Engadimos o usuario executando o comando
    resultado = subprocess.run(["useradd", 
                                "-m", 
                                "-d", 
                                ruta_home_usuario, 
                                "-s", 
                                "/bin/bash",
                                nome_usuario], capture_output=True, text=True)
    
    # Obtemos o uid do usuario
    uid = pwd.getpwnam(nome_usuario).pw_uid
    gid = pwd.getpwnam(nome_usuario).pw_gid

    # Cambiamos o propietario do directorio
    os.chown(ruta, uid, gid)
