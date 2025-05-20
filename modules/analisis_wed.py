import requests
from bs4 import BeautifulSoup

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
