import requests

# Inserta tu API key de OpenWeatherMap
API_KEY_WEATHER = "TU_API_KEY"
CIUDAD_DEFAULT = "Bogotá"

# Inserta tu API key de NewsAPI
API_KEY_NEWS = "TU_API_KEY"

def obtener_clima(ciudad=CIUDAD_DEFAULT):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY_WEATHER}&lang=es&units=metric"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()
        temp = data["main"]["temp"]
        descripcion = data["weather"][0]["description"]
        return f"En {ciudad} hay {descripcion} con una temperatura de {temp}°C."
    else:
        return "No se pudo obtener el clima. Verifica la ciudad o la API Key."

def obtener_noticias():
    url = f"https://newsapi.org/v2/top-headlines?country=mx&apiKey={API_KEY_NEWS}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        noticias = respuesta.json()["articles"][:5]
        resumen = "\n".join(f"- {n['title']}" for n in noticias)
        return f"📰 Noticias destacadas:\n{resumen}"
    else:
        return "No se pudieron obtener las noticias. Verifica la API Key."
def buscar_noticias_inversion():
    url = f"https://newsapi.org/v2/everything?q=inversion rentable&apiKey={API_KEY_NEWS}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        noticias = respuesta.json()["articles"][:5]
        resumen = "\n".join(f"- {n['title']}" for n in noticias)
        return f"📈 Oportunidades de inversión encontradas:\n{resumen}"
    else:
        return "No se pudieron obtener las oportunidades de inversión. Verifica la API Key."

def obtener_clima(ciudad="Bogotá"):
    return (f"🌤️ Clima actual en {ciudad}:\n"
            "Temperatura: 22°C\n"
            "Humedad: 60%\n"
            "Condición: Parcialmente nublado\n"
            "(Esto es un ejemplo. Se activará en tiempo real cuando tengas tu API).")

def obtener_noticias():
    noticias_demo = [
        "🔹 Científicos descubren una nueva especie en el Amazonas.",
        "🔹 La inteligencia artificial revoluciona la medicina.",
        "🔹 Elon Musk anuncia avances en su nuevo proyecto espacial.",
        "🔹 Economistas predicen cambios en el mercado global.",
        "🔹 Nuevo récord mundial en maratón olímpico."
    ]
    return "📰 Noticias destacadas:\n" + "\n".join(noticias_demo)
