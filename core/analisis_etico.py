# -*- coding: utf-8 -*-
# core/analisis_etico.py

import speech_recognition as sr

def obtener_texto_por_voz():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Por favor, hable ahora...")
        audio = recognizer.listen(source)
    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        print(f"Texto reconocido: {texto}")
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
        return ""
    except sr.RequestError:
        print("Error al conectarse al servicio de reconocimiento de voz.")
        return ""

class AnalisisEtico:
    def __init__(self, texto):
        self.texto = texto

    def evaluar(self):
        """
        Realiza un análisis ético básico del texto.
        Retorna un dict con el resultado.
        """
        resultado = {
            "contiene_palabras_inapropiadas": self._contiene_palabras_inapropiadas(),
            "longitud_texto": len(self.texto),
        }
        return resultado

    def _contiene_palabras_inapropiadas(self):
        palabras_inapropiadas = {"odio", "violencia", "discriminación"}
        texto_minuscula = self.texto.lower()
        return any(palabra in texto_minuscula for palabra in palabras_inapropiadas)

def realizar_analisis_etico():
    texto = obtener_texto_por_voz()
    if not texto:
        return "No se pudo obtener texto por voz."

    analisis = AnalisisEtico(texto)
    resultado = analisis.evaluar()

    if resultado["contiene_palabras_inapropiadas"]:
        return f"Advertencia: El texto contiene lenguaje inapropiado. Longitud: {resultado['longitud_texto']} caracteres."
    else:
        return f"Análisis ético completo. El texto es apropiado. Longitud: {resultado['longitud_texto']} caracteres."
