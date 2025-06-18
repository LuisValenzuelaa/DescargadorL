from yt_dlp import DownloadError, YoutubeDL #librería para descargar de youtube
import os 
import logging
from uuid import uuid4 #crear ids únicos, evita que archivos se sobrescriban
class Descargador:
    def __init__(self, link, tipo):
        self.link = link
        self.tipo = tipo
        self.output_dir = "downloads"
        os.makedirs(self.output_dir, exist_ok = True) #para crear directorios, toma en cuenta si ya está creada o no
        
    def descargar(self):
        nombre_archivo = str(uuid4()) #función de uuid, crea un id aleatorio, se pasa a string para usarlo como nombre
        formato = "140" if self.tipo == "audio" else "18"
        extension = "m4a" if self.tipo == "audio" else "mp4"
        ruta_salida = f"{self.output_dir}/{nombre_archivo}.%(ext)s"#%(ext)s es laextensión del archivo
        opciones = {
            "format": formato,
            "outtmpl": ruta_salida, #output template
            "merge_output_format": extension #unir audio y video
        }
        try:    
            with YoutubeDL(opciones) as ydl: #de YoutubeDL, crea un objeto
                info = ydl.extract_info(self.link, download = True)
                ruta_real = ydl.prepare_filename(info)
                if not os.path.exists(ruta_real):
                    logging.error(f"EL archivo no se generó: {ruta_real}")
                    return None
                return ruta_real
        except DownloadError as e:
            logging.error(f"Error al descargar: {e}")
            return None
        except Exception as e:
            logging.error(f"Error inesperado: {e}")
            return None  
            
            