---
title: "4.2. Funcións"
weight: 2
---
A libraría `pwd` en Python proporciona funcións para traballar con información de usuarios do sistema operativo nun entorno Unix.

A función **`getpwuid(uid)`** devolve un obxecto `pwd.struct_passwd` que contén información dun usuario dado o seu identificador de usuario (`uid`). A través deste obxecto, podes acceder a detalles como o nome do usuario, o seu directorio de inicio, a shell predeterminada, entre outros.

A función **`getpwnam(name)`** devolve un obxecto `pwd.struct_passwd` que contén información dun usuario dado o seu nome de usuario (`name`). Utiliza o nome de usuario para atopar a información asociada a ese usuario.

```python
import pwd

def obter_info_usuario(uid):
    info_usuario = pwd.getpwuid(uid)
    
    # Imprime a información do usuario
    print("Nome do usuario:", info_usuario.pw_name)
    print("Directorio de inicio:", info_usuario.pw_dir)
    print("Shell predeterminada:", info_usuario.pw_shell)

# Chama á función e pasa o UID do usuario para obter a súa información
obter_info_usuario(1000)
```
