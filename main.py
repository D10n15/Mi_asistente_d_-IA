# from voice.speech_to_text import escuchar_comando
from voz import hablar, escuchar_comando
from core.ia_dialogo import responder_mensaje
from modules.control_pc import abrir_programa
from modules.code_helper import explicar_codigo
from modules import noticias_clima
from modules import web_monitor
from modules import web_consultas
from modules import cyber_security
from modules import productividad
from modules import inversion
from modules import agenda
import subprocess


from datetime import datetime


def mostrar_menu():
    print("✅ El asistente se está ejecutando correctamente.")
    print("\n--- Asistente de Agenda ---")
    print("¿Buen día jefe, qué desea que haga por usted hoy?:")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Tomar control de computador y abrir programas")
    print("4. Consultas en la web")
    print("5. Hablar con Jarvis (por texto)")
    print("6. Salir")
    print("7. Hablar con Jarvis (por voz)")
    print("8. Ayuda con código")
    print("9. Optimizar código") 
    print("10. Inversiones y finanzas")
    print("11. Monitorear URL")
    print("12. Seguridad (escaneo, contraseñas, HTTPS)")
    print("13. Productividad (notas, frases motivacionales, Pomodoro)")
    print("14. Noticias y clima")


def actualizar_desde_git():
    try:
        resultado = subprocess.run(["git", "pull"], capture_output=True, text=True)
        if "Already up to date" in resultado.stdout:
            print("✅ El asistente ya está actualizado.")
        else:
            print("🔄 Se descargaron actualizaciones del asistente.")
    except Exception as e:
        print(f"❌ Error al actualizar desde Git: {e}")
 


def main():
    print("🔧 Iniciando asistente virtual...")
    actualizar_desde_git()
    print("Hola Jefe, soy Alisc tu asistente virtual. ¿En qué puedo ayudarte hoy?")
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")

            fecha = input("¿Para qué fecha es la tarea? (formato YYYY-MM-DD): ")
            
            agenda.agregar_tarea(descripcion, fecha)
            print("✅ Tarea agregada exitosamente.")

        elif opcion == "2":
            print(agenda.ver_tareas())

        elif opcion == "3":
            programa = input("¿Qué programa deseas abrir? (ej. navegador, calculadora, bloc de notas): ")
           

            resultado = abrir_programa(programa)
            print(resultado)

        elif opcion == "4":
            print("Consultas en la web activadas.")
            consulta = input("¿Qué deseas buscar?: ")
            
            fuente = input("¿Dónde buscar? (google / wikipedia): ").lower()
            if fuente == "google":
                resultado = web_consultas.buscar_en_google(consulta)
                print(resultado)
            elif fuente == "wikipedia":
                resultado = web_consultas.buscar_en_wikipedia(consulta)
                print(resultado)
            else:
                print("❌ Fuente no válida. Elige 'google' o 'wikipedia'.")

        elif opcion == "5":
            print("Jarvis activado. Escribe 'salir' para terminar la conversación.")
            while True:
                entrada = input("Tú: ")
                
                if entrada.lower() in ["salir", "exit", "adiós"]:
                    print("Jarvis: Hasta luego.")
                    break
                respuesta = responder_mensaje(entrada)
                print("Jarvis:", respuesta)

        elif opcion == "6":
            print("Hasta luego jefe.")
            break

        elif opcion == "7":
            print("Jarvis por voz activado. Di 'salir' para terminar la conversación.")
            while True:
                entrada = escuchar_comando()
                if not entrada:
                    continue
                if entrada.lower() in ["salir", "exit", "adiós"]:
                    hablar("Hasta luego jefe.")
                    break
                respuesta = responder_mensaje(entrada)
                print("Jarvis:", respuesta)
                hablar(respuesta)
                
        elif opcion == "8":
            codigo = input("Escribe o pega el código que necesitas que analice:\n") 
            
            respuesta = explicar_codigo(codigo)
            print("Asistente:", respuesta)
        
        elif opcion == "9":
            print("Función de optimización de código en desarrollo.")
            # Aquí podrías integrar un optimizador de código o un modelo de IA.
            # Por ahora, solo se muestra un mensaje.
            print("🔧 Función de optimización de código en desarrollo.")
            
        elif opcion == "10":
            print("1. Buscar oportunidades de inversión")
            print("2. Diferencias entre activos y pasivos")
            print("3. Consejos financieros")
            subopcion = input("Selecciona una opción: ")
            
            if subopcion == "1":
                print(inversion.buscar_inversiones())
            elif subopcion == "2":
                print(inversion.activos_pasivos())
            elif subopcion == "3":
                print(inversion.consejos_financieros())
                
        elif opcion == "11":
            print("1. Buscar en Google")
            print("2. Buscar en Wikipedia")
            print("3. Monitorear una página web")
            subopcion = input("Selecciona una opción: ")
            
            if subopcion == "1":
                consulta = input("¿Qué deseas buscar en Google?: ")
                resultados = web_monitor.buscar_google(consulta)
                print("Resultados encontrados:")
                for r in resultados:
                    print("🔎", r)

            elif subopcion == "2":
                consulta = input("¿Qué tema deseas consultar en Wikipedia?: ")
                resumen = web_monitor.buscar_wikipedia(consulta)
                print("📚", resumen)

            elif subopcion == "3":
                url = input("Ingresa la URL de la página: ")
                palabra = input("¿Qué palabra clave deseas monitorear?: ")
                resultado = web_monitor.monitorear_url(url, palabra)
                print("🕵️", resultado)
            
            elif subopcion == "4":
                print("Función de monitoreo de páginas web en desarrollo.")
                # Aquí podrías integrar un monitor de páginas web.
                # Por ahora, solo se muestra un mensaje.
                print("🔍 Función de monitoreo de páginas web en desarrollo.")
                
        elif opcion == "12":
            print("1. Verificar contraseña")
            print("2. Revisar HTTPS en un sitio")
            print("3. Analizar cabeceras HTTP")
            print("4. Escanear puertos")
            print("5. Buscar subdominios (simulado)")

            subop = input("Selecciona una opción: ")

            if subop == "1":
                pwd = input("Introduce la contraseña a evaluar: ")
                print(cyber_security.verificar_contraseña(pwd))

            elif subop == "2":
                sitio = input("Introduce el sitio web (ej. google.com): ")
                print(cyber_security.verificar_https(sitio))

            elif subop == "3":
                sitio = input("Introduce la URL (ej. http://ejemplo.com): ")
                print(cyber_security.analizar_cabeceras(sitio))

            elif subop == "4":
                host = input("Introduce el dominio o IP a escanear: ")
                print(cyber_security.escanear_puertos(host))

            elif subop == "5":
                dominio = input("Introduce el dominio base (ej. ejemplo.com): ")
                print(cyber_security.buscar_subdominios_simulado(dominio))
            else:
                print("❌ Opción no válida. Intenta de nuevo.")

        elif opcion == "13":
            while True:
                print("\n--- Productividad ---")
                print("1. Agregar nota")
                print("2. Ver notas")
                print("3. Frase motivacional")
                print("4. Iniciar Pomodoro")
                print("5. Volver al menú principal")
                subop = input("Elige una opción: ")

                if subop == "1":
                    nota = input("Escribe tu nota: ")
                    print(productividad.agregar_nota(nota))

                elif subop == "2":
                    print(productividad.ver_notas())

                elif subop == "3":
                    print(productividad.frase_motivacional())

                elif subop == "4":
                    print(productividad.iniciar_pomodoro())

                elif subop == "5":
                    break

                else:
                    print("Opción inválida.")
                    # Fin del menú de productividad
        elif opcion == "14":
            while True:
                print("\n--- Noticias y Clima ---")
                print("1. Ver clima actual")
                print("2. Ver noticias destacadas")
                print("3. Volver al menú principal")
                subop = input("Elige una opción: ")

                if subop == "1":
                    ciudad = input("¿De qué ciudad deseas el clima? (Deja vacío para Bogotá): ")
                    print(noticias_clima.obtener_clima(ciudad or "Bogotá"))

                elif subop == "2":
                    print(noticias_clima.obtener_noticias())

                elif subop == "3":
                    break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("❌ Ocurrió un error:", e)

# Este código es un asistente virtual que permite al usuario interactuar con él a través de texto o voz.
# El asistente puede agregar tareas a una agenda, ver las tareas existentes y mantener una conversación.
# El asistente utiliza un modelo de IA para responder a las preguntas del usuario.
# Además, se han añadido módulos en desarrollo para el control del computador y consultas en la web.
# El asistente también puede hablar y escuchar comandos de voz.
# Se han añadido opciones para interactuar con el asistente a través de texto o voz.
# El asistente tiene un menú que permite al usuario seleccionar la acción que desea realizar.
