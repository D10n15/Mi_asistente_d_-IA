#import pyttsx3
#from gtts import gTTS
#import pyglet

# Inicializa el motor una sola vez
#engine = pyttsx3.init()

# Función principal para hablar
#def hablar(texto):
 #   print(f"[IA dice]: {texto}")  # Modo texto visible
 #   engine.say(texto)
 #  engine.runAndWait()

# Alternativa usando gTTS y pyglet

#def hablar(texto):
#    tts = gTTS(text=texto, lang='es')
#   tts.save("voz.mp3")
#   music = pyglet.media.load("voz.mp3", streaming=False)
#    music.play()
#   pyglet.app.run()

#if __name__ == "__main__":
#    hablar("Hola Jefe, esto es una prueba de texto a voz usando pyttsx3.")
#    hablar("Hola Jefe, esto es una prueba de texto a voz usando gTTS.")
#    # Puedes probar ambas funciones comentando una de ellas
    
    
# voice/text_to_speech.py
from gtts import gTTS
import pyglet
import os

def hablar(texto):
    tts = gTTS(text=texto, lang='es')
    archivo = "voz.mp3"
    tts.save(archivo)
    
    music = pyglet.media.load(archivo, streaming=False)
    music.play()

    # Esperar a que termine de reproducirse
    while music.playing:
        pyglet.app.platform_event_loop.dispatch_posted_events()
    
    # Eliminar el archivo de audio luego
    os.remove(archivo)
