#from voice.speech_to_text import escuchar_comando
from voice.text_to_speech import hablar 
from voz import hablar, escuchar_comando
from modules import agenda

def main():
    print("Hola Jefe, soy Alisc tu asistente virtual. ¿En qué puedo ayudarte hoy?")
    
    while True:
        comando = escuchar_comando()

        if not comando:
            continue

        if "salir" in comando or "adiós" in comando:
            print("Hasta luego. Que tengas un gran día.")
            break

        elif "hora" in comando:
            from datetime import datetime
            hora_actual = datetime.now().strftime("%H:%M")
            print(f"Son las {hora_actual}")

        elif "cómo estás" in comando:
            print("Estoy lista para ayudarte. ¿Qué necesitas?")

        elif "nombre" in comando:
            print("Me puedes llamar AsistAI. Pero puedes cambiar mi nombre si lo deseas.")

        else:
            print("Aún no puedo hacer eso, pero estoy en entrenamiento. Intenta otra cosa.")
            
        # Aquí puedes agregar más comandos y funcionalidades según sea necesario
def mostrar_menu():
    print("\n--- Asistente de Agenda ---")
    print("¿buen dia jefe que desea que haga por usted el dia de hoy?:")
    print("1. Agregar tarea")
    print("2. consultas en la wed")
    print("3. tomar control de computador y abrir programas")
    print("4. Ver tareas")
    print("3. Salir")

def main():
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
            print("¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
print("Hola jefe Buenos dias, ¿en qué puedo ayudarte?")

# Este es el punto de entrada principal para el asistente virtual.
# Aquí se inicializa el asistente, se escucha el comando del usuario y se responde.
# Se utiliza un bucle infinito para mantener el asistente activo y esperando comandos.