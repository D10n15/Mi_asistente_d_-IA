import webbrowser
import wikipedia

wikipedia.set_lang("es")  # Español

def buscar_en_google(consulta):
    url = f"https://www.google.com/search?q={consulta}"
    webbrowser.open(url)
    return f"🔍 Buscando '{consulta}' en Google..."

def buscar_en_wikipedia(consulta):
    try:
        resumen = wikipedia.summary(consulta, sentences=2)
        return f"📚 Wikipedia dice: {resumen}"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"❗ Hay múltiples resultados para '{consulta}': {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return f"❌ No encontré resultados para '{consulta}' en Wikipedia."
    except Exception as e:
        return f"❌ Ocurrió un error al buscar en Wikipedia: {str(e)}"