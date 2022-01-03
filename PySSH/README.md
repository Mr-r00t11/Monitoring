# Arquitectura
Para la validación de los equipos debemos de igual forma se deben llamar a las librerías para tener de una forma más estructurada la programación.

    from Crypto.Cipher import PKCS1_OAEP
	from Crypto.PublicKey import RSA
	from pygame import mixer
	import paramiko
	import binascii
	import datetime
	import getpass
	import json
	import time
	import os
___

Creamos una clase con el nombre SSH y de igual forma realizamos el constructor.
	
	class SSH():
    	pass
    def __init__(self, user_1, password_1):
		self.user_1 = user_1

___

Como se observa, se crea el constructor para poder llamar a las variables desde otros métodos para poder guardar la información y poder manipularla.
	
	 self.keyPair = RSA.generate(1024)
     self.pubKey = self.keyPair.publickey()
     self.pubKeyPEM = self.pubKey.exportKey()
     self.privKeyPEM = self.keyPair.exportKey()
___
Ahora establecemos un valor de 1024 bits para generar la llave privada, después se crea una llave publica con el mismo valor para posteriormente exportar dicha llave publica y crear una sesión segura en las comunicaciones.

	
	def Encrypt_1(self):
     self.encryptor_1 = PKCS1_OAEP.new(self.pubKey)
     self.encrypted_1 = self.encryptor_1.encrypt(self.password_1)
     return "Encrypted:", binascii.hexlify(self.encrypted_1)
___
# Funcionamiento
###  Up
Cuando detecta que el puerto 22 SSH esta abierto, accede al servidor con credenciales permitidas y toma el uptime del equipo de tal manera que muestra el tiempo de encendido del servidor linux.

![](https://github.com/Mr-r00t11/Monitoring/blob/main/PySSH/up.png)


### Down
Cuando detecta que el puerto 22 SSH esat cerrado, manda una alerta sonora y pinta de color rojo una etiqueta indicando que el servidor no se encuetra activo.

![](https://github.com/Mr-r00t11/Monitoring/blob/main/PySSH/down.png)
___
*Por metodos de seguridad, el codigo se encuentra oculto, son proyectos desarrollados para el monitoreo de servidores. o equipos de Forescout*
