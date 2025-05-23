import os
import subprocess
import webbrowser


def abrir_programa(nombre):
    nombre = nombre.lower()

    if "navegador" in nombre:
        webbrowser.open("https://www.google.com")
    elif "calculadora" in nombre:
        subprocess.Popen("calc")
    elif "bloc de notas" in nombre or "notas" in nombre:
        subprocess.Popen("notepad")
    elif "vscode" in nombre or "visual studio code" in nombre:
        os.system("code")  # Asegúrate de tener `code` en variables de entorno
    else:
        return f"No reconozco el programa '{nombre}'"
    
    return f"Abrí {nombre} correctamente"
def cerrar_programa(nombre):
    nombre = nombre.lower()

    if "navegador" in nombre:
        os.system("taskkill /im chrome.exe /f")  # Cambia 'chrome.exe' por el navegador que uses
    elif "calculadora" in nombre:
        os.system("taskkill /im calc.exe /f")
    elif "bloc de notas" in nombre or "notas" in nombre:
        os.system("taskkill /im notepad.exe /f")
    elif "vscode" in nombre or "visual studio code" in nombre:
        os.system("taskkill /im Code.exe /f")  # Cambia 'Code.exe' por el ejecutable correcto
    else:
        return f"No reconozco el programa '{nombre}'"
    
    return f"Cerré {nombre} correctamente"