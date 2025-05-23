
# -*- coding: utf-8 -*- core/control.py
# Asistente Virtual
"""
Asistente Virtual - Controlador Principal
Este módulo actúa como el controlador principal del asistente virtual.
Se encarga de interpretar los comandos del usuario y dirigirlos a las funciones correspondientes.
"""

import re
import dateparser

from AsistenteVirtual.modules import inversion, web_monitor
from core.analisis_etico import realizar_analisis_etico
from core.nlp import interpretar_comando as nlp_interpretar_comando

from modules import agenda, code_helper, tarea
from modules.ciberseguridad import defensiva, ofensiva
from voice.text_to_speech import hablar
from modules.ciberseguridad import escanear_puertos, detectar_dispositivos_red, fuerza_bruta_simulada

def iniciar_asistente():
    """
    Inicia el asistente virtual y espera comandos del usuario.
    """
    print("Asistente Virtual iniciado. ¿En qué puedo ayudarte hoy?")
    while True:
        texto = input("Tú: ")
        if texto.lower() == "salir":
            print("Asistente Virtual cerrado.")
            break
        respuesta = ejecutar_comando(texto)
        print(f"Asistente: {respuesta}")
def ejecutar_comando(texto):
    """
    Recibe texto, interpreta el comando y ejecuta la función correspondiente.
    """
    comando = nlp_interpretar_comando(texto)

    if comando == "agenda":
        return agenda.mostrar_agenda()

    elif comando == "programacion":
        return code_helper.ayuda_con_codigo()

    elif comando == "inversion":
        return inversion.sugerencia_inversion()

    elif comando == "infiltrar":
        return defensiva.realizar_analisis_etico()
    
    elif comando == "escanear puertos":
        return ofensiva.escanear_puertos()
        
    elif comando == "musica":
        return "Funcionalidad de música en construcción."

    elif comando == "analisis_web":
        return "Funcionalidad de análisis web en construcción."

    elif comando == "salir":
        return "Saliendo del asistente. ¡Hasta pronto!"

    else:
        return "Lo siento, no entendí el comando."


def procesar_comando(comando):
    """
    Procesa comandos específicos relacionados con la agenda.
    """
    comando = comando.lower()

    if "agrega" in comando and "evento" in comando:
        # Ejemplo: "agrega evento reunión mañana a las 10"
        partes = comando.split("evento")
        if len(partes) > 1:
            detalles = partes[1].strip()
            fecha = "sin fecha"
            if "para" in detalles:
                titulo, fecha = detalles.split("para", 1)
                titulo = titulo.strip()
                fecha = fecha.strip()
            else:
                titulo = detalles
            return agenda.agregar_evento(titulo, fecha)
        else:
            return "No entendí los detalles del evento."

    elif "muéstrame" in comando and "agenda" in comando:
        return agenda.ver_agenda()

    elif "borra" in comando and "agenda" in comando:
        return agenda.borrar_agenda()

    else:
        return "No entendí ese comando."


def interpretar_comando(texto):
    """
    Interpreta comandos de texto y llama a las funciones correspondientes.
    """
    texto = texto.lower()

    # Agenda
    if "agregar tarea" in texto or "añadir tarea" in texto:
        tarea = texto.split("tarea")[-1].strip()

        # Buscar una fecha natural como "mañana", "el viernes", etc.
        fecha = dateparser.parse(texto, languages=['es'])

        if fecha:
            agenda.agregar_tarea(tarea, fecha.strftime("%Y-%m-%d"))
            return f"Tarea '{tarea}' añadida para el {fecha.strftime('%A, %d de %B de %Y')}."
        else:
            return "¿Para qué fecha deseas agendar la tarea?"

    elif "ver tareas" in texto:
        return agenda.ver_tareas()

    # Ayuda con código
    elif "cómo programar" in texto or "ayuda con código" in texto:
        return code_helper.ayuda_codigo(texto)

    # Inversiones
    elif "invertir" in texto or "acción" in texto or "dividendo" in texto:
        return inversion.analizar_inversion(texto)

    # Ciberseguridad ofensiva
    elif "escanear puertos" in texto:
        host = "127.0.0.1"  # Por defecto, o puedes hacerlo dinámico
        resultados = escanear_puertos(host)
        for puerto, estado in resultados:
            hablar(f"Puerto {puerto} está {estado}")
        return "Escaneo de puertos finalizado."

    elif "dispositivos en red" in texto or "escanear red local" in texto:
        resultado = detectar_dispositivos_red()
        hablar("Resultado del escaneo de red:")
        print(resultado)
        return "Escaneo de red finalizado."

    elif "fuerza bruta" in texto:
        usuario = "admin"
        intentos = ["1234", "admin", "password"]
        resultado = fuerza_bruta_simulada(usuario, intentos)
        hablar(resultado)
        return "Simulación de fuerza bruta finalizada."

    # Despedida
    elif "salir" in texto or "adiós" in texto:
        return "Hasta luego. ¡Que tengas un gran día!"

    else:
        return "Lo siento, no entendí ese comando."

