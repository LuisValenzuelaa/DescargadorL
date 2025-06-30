from flask import Flask, request, send_file, render_template, after_this_request
from descargador import Descargador
import os
from io import BytesIO
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/descargar", methods=["POST"])
def descargar():
    url = request.form.get("url")
    tipo = request.form.get("tipo")
    descargador = Descargador(url, tipo)
    archivo = descargador.descargar()
    if not archivo or not os.path.exists(archivo): # puede ser None
        return "Error: No se pudo generar el archivo", 500
    with open(archivo, "rb") as f:
        contenido = BytesIO(f.read())
    @after_this_request
    def limpiar(respuesta):
        if os.path.exists(archivo):
            os.remove(archivo)
        return respuesta
    return send_file(contenido, as_attachment = True, download_name = os.path.basename(archivo),mimetype = "application/octet-stream")  
if __name__ == "__main__":
    app.run(debug = True) 