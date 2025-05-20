# voz.py
from gtts import gTTS
import pyglet
import os
import time
import speech_recognition as sr

def hablar(texto):
    tts = gTTS(text=texto, lang='es')
    archivo = "voz.mp3"
    tts.save(archivo)

    music = pyglet.media.load(archivo, streaming=False)
    music.play()

    while music.playing:
        time.sleep(0.1)

    os.remove(archivo)

def escuchar_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
        try:
            comando = r.recognize_google(audio, language="es-ES")
            print("Comando reconocido:", comando)
            return comando
        except sr.UnknownValueError:
            print("No se entendió el audio.")
            return ""
        except sr.RequestError:
            print("Error al conectar con el servicio de reconocimiento.")
            return ""

# Este módulo se encarga de la interacción de voz del asistente virtual.
# Utiliza la biblioteca speech_recognition para convertir voz a texto
# y pyttsx3 para convertir texto a voz.
# La función `hablar` convierte texto a voz y lo reproduce.