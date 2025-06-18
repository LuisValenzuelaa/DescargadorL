from yt_dlp import YoutubeDL
import os
from uuid import uuid4
class Descarador:
    def __init__(self, link, tipo):
        self.link = link
        self.tipo = tipo
        self.output_dir = "downloads"
        os.makedirs(self.output_dir, exist_ok = True)
        
    def descargar(self):
        nombre_archivo = str(uuid4())
        formato = "bestaudio" if self.tipo == "audio" else "best"
        extension = "mp3" if self.tipo == "audio" else "mp4"
        ruta_salida = f"{self.output_dir}/{nombre_archivo}.%(ext)s"
        opciones = {
            "format": formato,
            "outtmpl": ruta_salida
        }
        if self.tipo == "audio":
            opciones["postprocessors"] = [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192"
            }]
        with YoutubeDL(opciones) as ydl:
            ydl.download([self.link])
        ruta_real = f"{self.output_dir}/{nombre_archivo}.{extension}"
        return ruta_real    
            
            