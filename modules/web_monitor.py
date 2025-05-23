# modules/web_monitor.py
from bs4 import BeautifulSoup
import wikipedia
from googlesearch import search
import requests

def buscar_google(consulta, num_resultados=3):
    resultados = []
    for resultado in search(consulta, num=num_resultados, stop=num_resultados):
        resultados.append(resultado)
    return resultados

def buscar_wikipedia(consulta):
    try:
        resumen = wikipedia.summary(consulta, sentences=2, auto_suggest=False)
        return resumen
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Consulta ambigua. Intenta ser más específico. Opciones: {e.options[:5]}"
    except Exception as e:
        return f"No se encontró información: {str(e)}"

def monitorear_url(url, palabra_clave):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        contenido = soup.get_text()
        if palabra_clave.lower() in contenido.lower():
            return f"La palabra clave '{palabra_clave}' fue encontrada en el sitio."
        else:
            return f"La palabra clave '{palabra_clave}' NO se encontró en el sitio."
    except Exception as e:
        return f"No se pudo acceder al sitio: {str(e)}"
    
# modules/inversiones.py

def buscar_noticias(palabra_clave="inversion rentable"):
    url = f"https://www.google.com/search?q={palabra_clave.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        titulos = []
        for item in soup.find_all('h3'):
            texto = item.get_text()
            if texto and any(keyword in texto.lower() for keyword in ['mejor', 'rentable', '2025', 'ganancia']):
                titulos.append(texto)

        if titulos:
            return f"📈 Oportunidades de inversión encontradas:\n" + "\n".join(titulos[:5])
        else:
            return "No se encontraron oportunidades destacadas."

    except Exception as e:
        return f"❌ Error buscando oportunidades: {str(e)}"

def buscar_ofertas_pasivos():
    # Busca formas de ganar dinero pasivamente
    return buscar_noticias("cómo ganar dinero con ingresos pasivos 2025")

def oportunidades_con_alta_probabilidad():
    # Busca inversiones con poca pérdida y buena probabilidad
    return buscar_noticias("inversiones seguras con alta rentabilidad 2025")


