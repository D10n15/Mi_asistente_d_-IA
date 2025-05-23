import time
import random

notas = []

def agregar_nota(nota):
    notas.append(nota)
    return "Nota agregada."

def ver_notas():
    if notas:
        return "\n".join(f"{i+1}. {n}" for i, n in enumerate(notas))
    else:
        return "No hay notas guardadas."

def frase_motivacional():
    frases = [
        "¡Tú puedes con todo, jefe!",
        "Cada día es una nueva oportunidad.",
        "No te detengas ahora, vas por buen camino.",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día."
    ]
    return random.choice(frases)

def iniciar_pomodoro():
    print("🕒 Temporizador Pomodoro iniciado: 25 minutos de trabajo.")
    time.sleep(5)  # Simula 25 minutos con 5 segundos para prueba
    print("⏲️ ¡Tiempo de descanso! 5 minutos.")
    time.sleep(2)  # Simula 5 minutos con 2 segundos
    print("✅ Fin del ciclo Pomodoro.")
    return "Ciclo Pomodoro completado."

def iniciar_pomodoro_largo():
    print("🕒 Temporizador Pomodoro largo iniciado: 50 minutos de trabajo.")
    time.sleep(5)  # Simula 50 minutos con 5 segundos para prueba
    print("⏲️ ¡Tiempo de descanso! 10 minutos.")
    time.sleep(2)  # Simula 10 minutos con 2 segundos
    print("✅ Fin del ciclo Pomodoro largo.")
    return "Ciclo Pomodoro largo completado."