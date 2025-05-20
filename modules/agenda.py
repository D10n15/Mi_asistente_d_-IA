# -*- coding: utf-8 -*- 
import json
from datetime import datetime
from pathlib import Path
import os



DATA_FILE = 'data/agenda.json'

# Asegura que el archivo exista
def cargar_agenda():
    if not os.path.exists(DATA_FILE):
        guardar_agenda([])
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def guardar_agenda(agenda):
    with open(DATA_FILE, 'w') as file:
        json.dump(agenda, file, indent=2)

def agregar_evento(titulo, fecha):
    agenda = cargar_agenda()
    evento = {
        "titulo": titulo,
        "fecha": fecha,
        "creado": datetime.now().isoformat()
    }
    agenda.append(evento)
    guardar_agenda(agenda)
    return f"Evento '{titulo}' agregado para el {fecha}."

def ver_agenda():
    agenda = cargar_agenda()
    if not agenda:
        return "No tienes eventos en tu agenda."
    eventos = [f"- {ev['titulo']} el {ev['fecha']}" for ev in agenda]
    return "Tus eventos:\n" + "\n".join(eventos)

def borrar_agenda():
    guardar_agenda([])
    return "Todos los eventos han sido eliminados."

# -*- coding: utf-8 -*-
# agenda.py
# Ruta al archivo JSON donde se guardan las tareas
DATA_PATH = Path("data/agenda.json")

# Asegura que el archivo y carpeta existan
DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
if not DATA_PATH.exists():
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump([], f)

def cargar_tareas():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_tareas(tareas):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)

def agregar_tarea(descripcion, fecha_str):
    tareas = cargar_tareas()
    tareas.append({
        "descripcion": descripcion,
        "fecha": fecha_str,
        "creado": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    guardar_tareas(tareas)

def ver_tareas():
    tareas = cargar_tareas()
    if not tareas:
        return "No tienes tareas pendientes."

    resultado = "Estas son tus tareas:\n"
    for i, tarea in enumerate(tareas, 1):
        resultado += f"{i}. {tarea['descripcion']} - para el {tarea['fecha']}\n"
    return resultado

def borrar_tarea(indice):
    tareas = cargar_tareas()
    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        guardar_tareas(tareas)
        return f"Tarea '{tarea_eliminada['descripcion']}' eliminada."
    else:
        return "Índice de tarea no válido."