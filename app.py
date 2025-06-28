from flask import Flask, after_this_request, request, send_file, render_template
from descargador import Descargador
import logging
import os
app = Flask(__name__)#name equivale a main si el archivo se ejecuta directamente
logging.basicConfig(level=logging.INFO)
@app.route("/")#cuando se vaya al directorio raiz se ejecuta la función index
def index():
    return render_template("index.html")#busca en la carpeta templates y carga el archivo
@app.route("/descargar", methods=["POST"])
def descargar():
    url = request.form.get("url") # se obtiene del name del html
    tipo = request.form.get("tipo")
    if not url:
        return "URL no proporcionada", 400 # 400 es solicitud incorrrecta, bad error
    descargador = Descargador(url, tipo)
    ruta_archivo = descargador.descargar()
    if not ruta_archivo or not os.path.exists(ruta_archivo): # puede ser None
        return "Error: No se pudo generar el archivo", 500 # 500 es internal several error
    return send_file(ruta_archivo, as_attachment = True, download_name = os.path.basename(ruta_archivo))  
if __name__ == "__main__":
    app.run(debug = True) 