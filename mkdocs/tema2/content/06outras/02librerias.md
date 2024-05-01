---
title: "6.2. Librerías interesantes"
weight: 2
---

### 6.2.1. [Paramiko](https://pypi.org/project/paramiko/---)

Librería que permite a comunicación con servidores remotos a través de SSH.

```python
import paramiko

# Datos de conexión SSH
host = 'hostname_o_direccon_IP'
puerto = 22
usuario = 'nome_de_usuario'
contrasinal = 'contraseña_do_usuario'

# Crea unha instancia do cliente SSH
cliente_ssh = paramiko.SSHClient()

# Configura o cliente SSH para que acepte automáticamente as claves de host descoñecidas
cliente_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Conéctate ao servidor SSH
    cliente_ssh.connect(hostname=host, port=puerto, username=usuario, password=contrasinal)
    
    # Executa un comando no servidor SSH
    comando = 'ls -l'
    stdin, stdout, stderr = cliente_ssh.exec_command(comando)
    
    # Le a saida do comando executado
    salida = stdout.read().decode()
    
    # Imprime a saida do comando
    print("Salida del comando:")
    print(salida)

except paramiko.AuthenticationException:
    print("Erro de autenticación.")
except paramiko.SSHException as e:
    print("Erro ao conectarse ao servidor SSH:", str(e))
finally:
    # Cierra la conexión SSH
    cliente_ssh.close()
```


### 6.2.2. [PSutil](https://pypi.org/project/psutil/)

Proporciona unha interface para acceder a información sobre procesos e sistemas en execución como CPU, memoria, discos, redes, etc.

```python
import psutil

# Obter información sobre o uso de CPU
uso_cpu = psutil.cpu_percent(interval=1)  # Porcentaje de uso de CPU no último segundo
print("Uso de CPU:", uso_cpu, "%")

# Obter información sobre o uso de memoria
memoria = psutil.virtual_memory()
print("Memoria total:", memoria.total, "bytes")
print("Memoria disponible:", memoria.available, "bytes")

# Obter información sobre o uso de disco
particions = psutil.disk_partitions()
for particion in particions:
    print("Partición:", particion.device)
    uso_disco = psutil.disk_usage(particion.mountpoint)
    print("   Uso total:", uso_disco.total, "bytes")
    print("   Uso utilizado:", uso_disco.used, "bytes")
    print("   Uso libre:", uso_disco.free, "bytes")
    print("   Porcentaxe de uso:", uso_disco.percent, "%")

# Obter información sobre a redw
estadisticas_redw = psutil.net_if_stats()
for interfaz, estadisticas in estadisticas_redw.items():
    print("Interfaz:", interfaz)
    print("   Velocidad de transmisión:", estadisticas.speed, "bytes/s")
    print("   Duplex:", estadisticas.duplex)

# Obtener información sobre os procesos en execución
procesos = psutil.process_iter()
print("Procesos en execución:")
for proceso in procesos:
    print("PID:", proceso.pid, "| Nome:", proceso.name(), "| Uso de CPU:", proceso.cpu_percent(interval=0.1), "%")
```


### 6.2.3. [PyYaml](https://pypi.org/project/PyYAML/)

É unha biblioteca para traballar con ficheiros YAML, que un formato utilizado para ficheiros de configuración.

- `datos.yaml`:

```yaml
nomes:
  - Juan
  - María
  - Pedro

idades:
  Juan: 30
  María: 25
  Pedro: 35
```

```python
import yaml

# Le o arquivo YAML
with open('datos.yaml', 'r') as arquivo:
    datos = yaml.safe_load(arquivo)

# Imprime os datos lídos
print("Datos leídos del archivo:")
print(datos)
print()

# Modificar los datos
datos['nomes'].append('Luis')
datos['idades']['Luis'] = 40
```


### 6.2.4. [PyWin32](https://pypi.org/project/pywin32/)

Proporciona acceso a moitas función da API de Windows, que permite interactuar co sistema operativo manipulando arquivos, traballar co rexistro, administrar servizos, etc.

```python
import win32com.client

# Abre o bloc de notas
shell.Run("notepad.exe")

# Espera a que se abra completamente
shell.AppActivate("Bloc de notas")

# Escribe no bloc de notas
mensaxe = "¡Hola desde Python con pywin32!"
shell.SendKeys(mensaxe)

# Esperamos antes de cerralo
import time
time.sleep(1)

# Cerramolo
shell.SendKeys("%{F4}")  # Alt + F4 para cerrar a venta activa
```

### 6.2.5.[ipaddress]((https://docs.python.org/3/library/ipaddress.html))

**É unha biblioteca estándar de Python dende a versión 3.3.**. Esta proporciona unha serie de clases e funcións para manipular de xeito sinxelo direccións IP.

```python
import ipaddress

# Crea unha instancia dunha dirección IPv4
ip = ipaddress.IPv4Address('192.168.1.1')

# Crea una instancia de unha rede IPv4
rede = ipaddress.IPv4Network('192.168.1.0/24')

# Verificaa se unha dirección IP está dentro dunha rede
if ip in rede:
    print(f'{ip} está dentro da rede {red}')

# Iterar sobre todalas direccions IP dunha rede
for direccion_ip in rede:
    print(direccion_ip)
```


### 6.2.6. [pyad](https://zakird.github.io/pyad/)

É unha librería que proporciona unha interface para interactuar con *Active Directory* utilizando o servizo de directorio de Windows.


```python
from pyad import *

# Establece o controlador de dominio
pyad.set_defaults(ldap_server="servidor_ad")

# Busca usuarios por nome
usuarios = pyad.adsearch.ADSearch().search_users(display_name="NomeDeUsuario")

# Imprimie os usuarios encontrados
for usuario in usuarios:
    print("Nome de usuario:", usuario.get_attribute("sAMAccountName"))
    print("Nome completo:", usuario.get_attribute("displayName"))
    print("Correo electrónico:", usuario.get_attribute("mail"))
    print("Departamento:", usuario.get_attribute("department"))
    print()
```


### 6.2.7. [python-ldap](https://www.python-ldap.org/en/python-ldap-3.4.3/)

É unha biblioteca para acceder e administrar servidores LDAP.


```python
import ldap

# parametros de conexion
ldap_server = 'ldap://servidor_ad'
base_dn = 'dc=example,dc=com'
user = 'usuario_ad'
password = 'contraseña_ad'

# Conectar ao servidor
con = ldap.initialize(ldap_server)
con.simple_bind_s(user, password)

# Realiza busca de usuarios
filtro = '(objectClass=user)'
atributos = ['sAMAccountName', 'displayName', 'mail', 'department']
resultados = con.search_s(base_dn, ldap.SCOPE_SUBTREE, filtro, atributos)

# Imprimir os resultados
for usuario, datos in resultados:
    print("Nome de usuario:", datos['sAMAccountName'][0].decode())
    print("Nome completo:", datos['displayName'][0].decode())
    print("Correo electrónico:", datos['mail'][0].decode())
    print("Departamento:", datos['department'][0].decode())
    print()
```

### 6.2.8. [ansible_runner](https://ansible.readthedocs.io/projects/runner/en/latest/)

Esta librería permite interactuar con **Ansible** para executar e controlar tarefas directamente dende Python. 

```python
from ansible_runner import run

# Define a tarefa
task = {
    'hosts': 'localhost',
    'gather_facts': 'no',
    'tasks': [
        {
            'name': 'Imprime a información do sistema',
            'command': 'ansible -m setup localhost'
        }
    ]
}

# Executa a tarefa de Ansible
resultados = run(**task)

# Imprime ls resultados
for evento in resultados.events:
    print(evento['stdout'])
```

### 6.2.9. [pysmb](https://pypi.org/project/pysmb/)

Esta librería proporciona unha interface para interactuar con servidores Samba.

```python
from smb.SMBConnection import SMBConnection

# Datos de conexión ao servidor Samba
servidor = 'nome_do_servidor'
usuario = 'nome_de_usuario'
contrasena = 'contraseña_do_usuario'
dominio = 'DOMINIO'  # Si e necesario, do contrario, deixa este valor como ''

# Crea unha conexión ao servidor Samba
conexion = SMBConnection(usuario, contrasena, 'cliente', servidor, dominio=dominio)

# Conéctate ao servidor
conexion.connect(servidor)

# Lista os recursos compartidos dispoñibles
recursos_compartidos = conexion.listShares()

# Imprime os recursos compartidos dispoñibles
for recurso in recursos_compartidos:
    print(f"Recurso compartido: {recurso.name}")

# Cerra a conexión
conexion.close()
```
