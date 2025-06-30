from flask import Flask, request, send_file, render_template
from descargador import Descargador
import os
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
    return send_file(archivo, as_attachment = True, download_name = os.path.basename(archivo))  
if __name__ == "__main__":
    app.run(debug = True) 