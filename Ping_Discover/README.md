# Arquitectura
Para poder identificar el estado de los equipos, debemos importar algunas librerías para la obtención de datos, guardándolos en un formato JSON así mismo indicar la hora en la que el servidor deja de responder.
	
	from pygame import mixer
	import datetime
	import time
	import json
	import os
___
Creamos una clase con el nombre Ping, de esta manera crearemos el constructor para poder instanciar las variables en cualquier método correspondiente.
	
	class Ping():
		def __init__(self, ip_1):
			self.ip_1 = ip_1
___

Cuando creamos la clase y mandamos las direcciones IP establecidas por el cliente, estas mismas variables desde el constructor las guardara de forma temporal mientras se utiliza el software parametrizando los métodos que se crearan a continuación.

	
	
    def IP_1(self):
        self.response_1 = os.popen('ping ' + self.ip_1).read()
___
Creamos nuestro primer método, donde vamos a identificar los equipos mediante el comando ping, como se puede observar, guardando los datos recibidos en una variable.

	
	 if 'Received = 4' in self.response_1:
            self.alive_1 = 'Up'
___

## Funcionamiento
Este programa monitorea servidores Forescout y Splunk, dando como resultado final la respuesta de conexion si un equipo se encuentra vivo o muerto.

![](https://github.com/Mr-r00t11/Monitoring/blob/main/Ping_Discover/ping.png)

*Por metodos de seguridad, el codigo se encuentra oculto, son proyectos desarrollados para el monitoreo de servidores. o equipos de Forescout.*
