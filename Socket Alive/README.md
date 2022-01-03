#Arquitctura
Se importarán librerías específicas para la recolección de datos y extracción de información, la librería mas importante que usaremos es la de socket, ya que con esa librería podemos mandar una petición hacia un puerto especifico.
	
	from pygame import mixer
	import datetime
	import socket
	import time
	import json
___
Se crea una clase principal la cual es llamada Socket_Alive, cuya finalidad es establecer una variable global para que pueda ser alcanzable por todos los métodos que se desarrollaran en un futuro.
	
	class Sockets_Alive():
    pass
    def __init__(self):
        self.ip_1 = '192.168.100.22'
___
Se inicializa creando el primer método en este caso podemos ver que creamos la instancia del socket, pasando parámetros específicos que son únicos para las direcciones IPv4, usando el protocolo de TCP.
	
	def Connect_Port(self):
        self.s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
___
En esta parte hacemos uso de las excepciones, el socket intentará establecer la conexión con el puerto 22 si establece la conexión entonces tendrá un valor “True”, que a su vez se transforma en un valor string “Up”.
	
	 try:
            self.alive_1 = 'Up'
            self.s1.connect((self.ip_1, self.port_1))
            self.s1.close()
___
El puerto se establece desde el constructor el cual se podrá instanciar desde cualquier método.
	 
	 self.port_1 = 22
___
Se crea un JSON, el cual servirá para poder manipular los datos en forma de diccionario y así mismo poder declarar los valores de estado de los NAC.
	
	def Create_Json(self):
        self.data = {
            'Status_1': self
		}
___
## Funcionamiento
Una vez que se abre la aplicación en este caso la interfaz, mostrara ya en pantalla de una manera más fácil de leer si el equipo cuenta con el puerto abierto o no.

*Nota: puede declararse cualquier puerto tcp.*

![](https://github.com/Mr-r00t11/Monitoring/blob/main/Socket%20Alive/up.png)

Si el equipo estuviera fuera de línea pintara las etiquetas verdes a rojas y lanzara una alerta sonora.

![](https://github.com/Mr-r00t11/Monitoring/blob/main/Socket%20Alive/down.png)
___
*Por metodos de seguridad, el codigo se encuentra oculto, son proyectos desarrollados para el monitoreo de servidores. o equipos de Forescout.*
