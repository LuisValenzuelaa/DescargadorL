from yt_dlp import DownloadError, YoutubeDL 
import os 
from uuid import uuid4 #crear ids únicos, evita que archivos se sobrescriban
class Descargador:
    def __init__(self, url, tipo):
        self.url = url
        self.tipo = tipo
        
    def descargar(self):
        nombre_archivo = str(uuid4()) #función de uuid, crea un id aleatorio, se pasa a string para usarlo como nombre
        formato = "140" if self.tipo == "audio" else "18"
        extension = "m4a" if self.tipo == "audio" else "mp4"
        opciones = {"format": formato, "outtmpl": f"{nombre_archivo}.%(ext)s", "merge_output_format": extension}
        try:    
            with YoutubeDL(opciones) as ydl:
                info = ydl.extract_info(self.url, download = True)
                ruta_salida = ydl.prepare_filename(info)
                if not os.path.exists(ruta_salida):
                    return None
                return ruta_salida
        except DownloadError as e:
            return None
        except Exception as e:
            return None