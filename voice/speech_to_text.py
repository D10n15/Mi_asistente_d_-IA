import speech_recognition as sr

def escuchar_microfono():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language="es-ES")
            print(f"Has dicho: {texto}")
            return texto
        except sr.UnknownValueError:
            print("No entendí lo que dijiste.")
            return ""
        except sr.RequestError as e:
            print(f"Error con el servicio de reconocimiento: {e}")
            return ""
    except OSError as e:
        print(f"No se detectó un micrófono: {e}")
        return ""
# Este módulo se encarga de la conversión de voz a texto.
# Utiliza la biblioteca speech_recognition para escuchar el micrófono