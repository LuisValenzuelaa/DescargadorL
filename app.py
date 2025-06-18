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
    tipo = request.form.get("tipo", "video")
    if not url:
        return "URL no proporcionada", 400
    descargador = Descargador(url, tipo)
    ruta_archivo = descargador.descargar()
    if not ruta_archivo or not os.path.exists(ruta_archivo):
        return "Error: No se pudo generar el archivo", 500
    @after_this_request
    def cleanup(response):
        try:
            if os.path.exists(ruta_archivo):
                os.remove(ruta_archivo)
                logging.info(f"Archivo eliminado: {ruta_archivo}")
        except Exception as e:
            logging.error(f"Error al eliminar archivo: {e}")
        return response
    try:
        return send_file(ruta_archivo, as_attachment = True, download_name = os.path.basename(ruta_archivo))
    except Exception as e:
        logging.error(f"Error al enviar archivo: {e}")
        return f"Error al enviar el archivo: {str(e)}", 500    
if __name__ == "__main__":
    app.run(debug = True) 