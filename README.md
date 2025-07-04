**DescargadorL:**
Este proyecto tiene como objetivo la práctica del programador en el desarrollo web utilizando HTML, CSS y el framework de python para web, Flask.
Esta aplicación web permite descargar videos de Youtube utilizando la librería "yt_dlp" de python, permitiendo agregar el enlace del video y seleccionar si se desea descargar 
el audio o video con audio de este.

**Instalación:**
Para utilizar el proyecto se deben instalar las dependencias  de python del archivo "requeriments.txt" usando el comando pip install y ejecutar el archivo "app.py", para interactuar, se debe 
acceder en el navegador al localhost para python, suele ser "http://127.0.0.1:5000".
Recomendación, estar pendiente de utilizar la versiones más reciente de las dependencias, se puede verificar con el comando pip install --updrade.

**Desarollo:**
El directorio raíz cuenta con:
-  app.py: Archivo main, contiene el código que llama a la renderización de la plantilla html y lleva al directorio "/descargar" cuando se envía el formulario html, dentro de dicho directorio se
   crea una instancia de la clase "Descargador", donde se maneja la lógica de la descarga y también la limpieza de recursos, pensando en la optimización para el despligue web.

- descargador.py: Aquí se define la clase Descargador con los atributos "tipo" y "url","tipo" es referente al formato que se desea descargar, "url" es la url del video del que se desea descargar.
  La clase cuenta con un método "descargar", donde se genera un id único aleatorio para nombrar el archivo descargado y con la clase "YoutubeDL" de yt_dlp se maneja la descarga.

/templates
      - index.html: plantilla html simple.

/static
      - estilo.css: aquí se encuentra todo el código css, está vinculada al index.html, se utiliza media query para el diseño responsive.
      - logo.jpg: logo a utilizar en la aplicación.

**Funcionamiento para el usuario:** 
El usuario pega el url de un video de Youtube en el input con el placeholder "Ingresa la url del video", luego en el menú desplegable selecciona si desea descargar el video con
audio o solo el audio, luego envía la solicitud presionando el botón con la etiqueta "Descargar". El tiempo de espera durante la descarga varía según la velocidad del internet y el tamaño del archivo.
El archivo se guardará en la carpeta asignada por defecto para las descargas, al terminar se abrirá el cuadro de descarga del navegador.

**Funcionamiento del backend:**
Al ejecutar el archivo "app.py" nos encontramos en el directorio raíz, por lo que se renderiza la plantilla html, luego, cuando el usuario envía el formulario, nos envía al directorio "/descargar", al 
estar situados allí, se ejecuta la función "descargar()" del mismo "app.py", este obtiene los datos del formulario y los pasa como parámetros para crear una instancia de la clase "Descargador" y se llama
a su método "descargar" que crea un nombre aleatorio para el archivo y asigna especificaciones como el formato a descargar, estos datos los pasa a la clase "YoutubeDL" de la librería "yt_dlp". 
Tomemos en cuenta que esta aplicación se hizo pensando en el despliegue web, por lo que el backend está pasando del lado del sistema del host web, "YoutubeDL" hace la descarga en disco, pero con la librería
"io" hacemos que se lea el archivo completamente en la memoria RAM, esto permite eliminar el archivo del disco y optimizar el espacio, luego desde la memoria RAM se envía el archivo al navegador del usuario
y la memoria RAM de la máquina se libera automáticamente.

**Notas adicionales:**
La etiqueta nombrada como "version-1" es totalmente funcional en el localhost, pero se enfrentaron desafíos para el despliegue web, encontrando bloqueos por parte de Youtube marcando la solicitud como bot por
falta de autenticación, las razones sugeridas son que los host web utilizados, "Render" y "Railway", proporcionan IPs compartidas para su plan gratuito, además la documentación de 
yt_dlp tiene un apartado referente a este problema, mencionando el uso de cookies para superar este obstáculo, no se utilizaron cookies puesto que implicarían un riesgo. Se probó utilizar proxies
gratuitos de "https://free-proxy-list.net" pero el resultado fue el mismo. Es posible que con un plan pago del host web haya diferentes resultados.

**Despligue web:**
Si aún se considerara el despliegue web, se recomienda el uso de **"apt-get update && apt-get install -y ffmpeg && pip install -r requirements.txt"** para el Build Command y **"gunicorn -w 4 app:app"** 
para el Start Command.

**Autor:**
Luis Valenzuela, junio de 2025
