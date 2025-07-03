from flask import Flask, request, send_file, render_template, after_this_request #web
from descargador import Descargador #clase importada
import os #manejar directorios
from io import BytesIO
app = Flask(__name__) #se instancia una app de flask
@app.route("/") #al ir al directorio raíz ejecutar index()
def index():
    return render_template("index.html")
@app.route("/descargar", methods=["POST"]) #al ir al directorio "/descargar" ejecutar descargar()
def descargar():
    url = request.form.get("url") #obtener la url
    tipo = request.form.get("tipo") # obtener si es audio o video
    descargador = Descargador(url, tipo) #instanciar la clase pasándole los atributos
    archivo = descargador.descargar() #usar el método descargar
    if not archivo or not os.path.exists(archivo): # puede ser None
        return "Error: No se pudo generar el archivo", 500
    with open(archivo, "rb") as f: # rb = read binary, lectura binaria
        contenido = BytesIO(f.read())
    @after_this_request #eliminar el archivo después de send_file
    def limpiar(respuesta):
        if os.path.exists(archivo):
            os.remove(archivo)
        return respuesta
    return send_file(contenido, as_attachment = True, download_name = os.path.basename(archivo),mimetype = "application/octet-stream") #envía el archivo al navegador del usuario y lo descarga  
if __name__ == "__main__":
    app.run(debug = True) 