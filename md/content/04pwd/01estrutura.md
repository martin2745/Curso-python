---
title: "4.1. Estrutura de pwd"
weight: 1
---

A estrutura `struct_passwd` é un obxecto que contén información sobre un usuario do sistema operativo nun sistema Unix. 

Esta estrutura é devolta polas funcións da libraría `pwd`, como `getpwuid()` ou `getpwnam()`, e contén os seguintes campos:

- `pw_name`: O nome do usuario.
- `pw_passwd`: O contrasinal do usuario (encriptado).
- `pw_uid`: O identificador de usuario (UID).
- `pw_gid`: O identificador de grupo (GID) primario do usuario.
- `pw_gecos`: Información adicional do usuario (por exemplo, o nome completo).
- `pw_dir`: O directorio de inicio do usuario.
- `pw_shell`: A shell predeterminada do usuario.

