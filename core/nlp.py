import re

def interpretar_comando(texto):
    texto = texto.lower()

    if "tarea" in texto or "evento" in texto:
        return "agenda"
    elif "programa" in texto or "código" in texto or "ayuda con python" in texto:
        return "programacion"
    elif "invertir" in texto or "acciones" in texto:
        return "inversion"
    elif "buscar" in texto or "investiga" in texto:
        return "analisis_web"
    elif "infiltrar" in texto or "hackear" in texto:
        return "infiltrar"
    elif "reproducir" in texto or "música" in texto:
        return "musica"
    elif "abrir" in texto or "ejecutar" in texto:
        return "abrir" 
    elif "salir" in texto or "terminar" in texto:
        return "salir"
    else:
        return "desconocido"


from datetime import datetime, timedelta
import re

def interpretar_fecha(texto):
    texto = texto.lower()
    hoy = datetime.today()

    if "hoy" in texto:
        return hoy.strftime("%Y-%m-%d")
    elif "mañana" in texto:
        return (hoy + timedelta(days=1)).strftime("%Y-%m-%d")
    elif "pasado mañana" in texto:
        return (hoy + timedelta(days=2)).strftime("%Y-%m-%d")
    elif "lunes" in texto:
        return _proximo_dia_semana(0).strftime("%Y-%m-%d")
    elif "martes" in texto:
        return _proximo_dia_semana(1).strftime("%Y-%m-%d")
    elif "miércoles" in texto or "miercoles" in texto:
        return _proximo_dia_semana(2).strftime("%Y-%m-%d")
    elif "jueves" in texto:
        return _proximo_dia_semana(3).strftime("%Y-%m-%d")
    elif "viernes" in texto:
        return _proximo_dia_semana(4).strftime("%Y-%m-%d")
    elif "sábado" in texto or "sabado" in texto:
        return _proximo_dia_semana(5).strftime("%Y-%m-%d")
    elif "domingo" in texto:
        return _proximo_dia_semana(6).strftime("%Y-%m-%d")
    
    # Extrae fechas escritas en formato dd/mm/yyyy
    match = re.search(r"\b(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})\b", texto)
    if match:
        dia, mes, anio = match.groups()
        return f"{int(anio):04d}-{int(mes):02d}-{int(dia):02d}"
    
    return None

def _proximo_dia_semana(dia_semana):
    hoy = datetime.today()
    dias_diferencia = (dia_semana - hoy.weekday() + 7) % 7
    if dias_diferencia == 0:
        dias_diferencia = 7
    return hoy + timedelta(days=dias_diferencia)
def interpretar_hora(texto):
    texto = texto.lower()
    match = re.search(r"(\d{1,2}):(\d{2})", texto)
    if match:
        hora, minuto = match.groups()
        return f"{int(hora):02d}:{int(minuto):02d}"
    
    match = re.search(r"(\d{1,2})(?:h|:)(\d{2})", texto)
    if match:
        hora, minuto = match.groups()
        return f"{int(hora):02d}:{int(minuto):02d}"
    
    return None
def interpretar_fecha_hora(texto):
    fecha = interpretar_fecha(texto)
    hora = interpretar_hora(texto)

    if fecha and hora:
        return f"{fecha} {hora}"
    elif fecha:
        return fecha
    elif hora:
        return f"Hoy {hora}"
    
    return None
