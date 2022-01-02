# Arquitectura
Para la validación de los equipos que tengan los servicios web corriendo, se deben realizar algunas peticiones, para ello se deben realizar peticiones con métodos get para la entrega de datos hacia servicios http o https, como primera función importamos la librería para que se pueda ejecutar la conexión.

    import requests
___
Cuando se importa la librería, ya se realiza la instancia de las funciones de Requests.

    print(requests.get('https://google.com/'))
___
Como se puede ver en el ejemplo anterior se realizó una petición con el método GET, lo cual significa que está mandando un paquete hacia el servidor, de igual forma, el servidor debe responder con un OK en estados de HTTP el numero 200 es el valor del servidor el cual indica que está vivo y respondiendo dicha petición.

    <Response [200]>
___
Se puede observar que por defecto detecta el método HTTPS, siendo un servicio cifrado dando una conexión segura, en algunos de los casos existen certificados “No validos” creados por los mismos clientes, los cuales son hechos con OpenSSL una librería que permite la creación de certificados para las comunicaciones cifradas mediante HTTP, pero al no ser creado por alguna institución certificada, no lo detectara como valido, por lo cual para la verificación de certificados no válidos, creados por los mismos clientes, se debe ignorar esas validaciones.

    print(requests.get('https://google.com/', verify=False))

___

Para realizar la validación y tratar de identificar si el servidor estáfuncionando correctamente, se deben declarar parámetros en los cuales se deben validar ciertos valores de HTTP; haciendo condiciones en cuanto a la respuesta del servidor.

    r = requests.get('https://google.com/')
	try:
		if r.status_code == 200:
			print("[+] Conexion Establecida")
		else:
			print("[-] Conexion Rechazada")

___

Cuando realizamos las condicionales se debe agregar un “try” y “except”, esto sirve para que forcemos al programa su funcionamiento, el cual debe ejecutar las peticiones GET mediante HTTP o HTTPS si las respuestas del servidor son 404, 403, etc, no rompe el programa, por lo contrario captura ese error y lo muestra al usuario mediante un mensaje de “Conexión Rechazada”, haciendo más precioso el resultado de las respuestas inmediatas del programa.

    [+] Conexion Establecida

___

Una vez finalizado el desarrollo de las peticiones GET a los servidores, debemos realizar la alerta sonora de la aplicación, usaremos una librería llamada “PyGame”, la cual nos permite la reproducción de audios en formato “.WAV”, para iniciarlo usaremos la instancia de “pygame”.


    from pygame import mixer

___

Una vez declarada la librería, vamos a declarar una variable para la reproducción del audio.


    mixer.init()
	mixer.music.load("alarma.wav")
	mixer.music.play()

___
Dando como resultado final una alerta sonora y alerta visual cuando esta vivo.

![](https://github.com/Mr-r00t11/Monitoring/blob/main/PyMonitor/pymonitor.png)
___
Cuando esta el servidor se encuentra no disponible, se cambiara a color rojo.

![](https://github.com/Mr-r00t11/Monitoring/blob/main/PyMonitor/pymonitor%20down.png)
___
