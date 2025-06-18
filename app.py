from flask import Flask, request, send_file, render_template
from descargador import Descargador
import os
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.rout("/descargar", methods=["post"])
def descargar():
    link = request.form["link"]
    tipo = request.form["tipo"]
    descargador = Descargador(link, tipo)
    ruta_archivo = descargador.descargar()
    return send_file(ruta_archivo, as_attachment=True)
if __name__ == "__main__":
    app.run(debug = True)