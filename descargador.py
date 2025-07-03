from yt_dlp import DownloadError, YoutubeDL #descargar de Youtube 
import os #manejar directorios
from uuid import uuid4 #crear ids únicos, evita que archivos se sobrescriban
class Descargador:
    def __init__(self, url, tipo):
        self.url = url 
        self.tipo = tipo
        
    def descargar(self):
        nombre_archivo = str(uuid4()) #función de uuid, crea un id aleatorio, se pasa a string para usarlo como nombre
        formato = "140" if self.tipo == "audio" else "18" #140 es 128 kbps para m4a, 18 es 360p con audio para mp4
        extension = "m4a" if self.tipo == "audio" else "mp4"
        ruta_para_guardar = os.path.join(os.path.expanduser("~"), "Downloads", f"{nombre_archivo}.%(ext)s") #enviar el archivo a la carpeta de descargas por defecto, "%(ext)s" es un placeholder
        opciones = {"format": formato, "outtmpl": ruta_para_guardar, "merge_output_format": extension}
        try:    
            with YoutubeDL(opciones) as ydl: #se le pasa el diccionario de opciones para instanciar YoutubeDL
                info = ydl.extract_info(self.url, download = True) 
                ruta_salida = ydl.prepare_filename(info)
                if not os.path.exists(ruta_salida):
                    return None
                return ruta_salida #envía la ruta completa para el archivo
        except DownloadError as e:
            return None
        except Exception as e:
            return None