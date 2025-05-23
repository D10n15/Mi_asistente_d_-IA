# modules/inversiones.py

import random
from datetime import datetime

# modules/inversion.py

def buscar_inversiones():
    return (
        "Algunas opciones populares de inversión incluyen:\n"
        "- Criptomonedas (Bitcoin, Ethereum)\n"
        "- Acciones (Tesla, Apple, Amazon)\n"
        "- Bienes raíces\n"
        "- ETFs o fondos indexados\n"
        "- Negocios en línea o activos digitales\n"
        "¿Te interesa alguno en particular?"
    )

def activos_pasivos():
    return (
        "Un activo es algo que pone dinero en tu bolsillo, como una propiedad en alquiler o una acción que paga dividendos.\n"
        "Un pasivo es algo que saca dinero de tu bolsillo, como un préstamo o un coche.\n"
        "El objetivo es adquirir más activos que generen ingresos pasivos."
    )

def consejos_financieros():
    return (
        "Consejos básicos para invertir:\n"
        "- Nunca inviertas en algo que no entiendas.\n"
        "- Diversifica tus inversiones.\n"
        "- Invierte a largo plazo.\n"
        "- Mantén un fondo de emergencia antes de arriesgar dinero.\n"
        "- Invierte en tu educación financiera."
    )
def tendencias_inversion():
    return (
        "Tendencias actuales en inversiones:\n"
        "- Inversiones sostenibles y responsables.\n"
        "- Tecnología blockchain y criptomonedas.\n"
        "- Inteligencia artificial y automatización.\n"
        "- Energías renovables y sostenibilidad.\n"
        "- Salud y biotecnología."
    )

# Recomendaciones de inversión basadas en tendencias actuales
def sugerencia_inversion():
    inversiones = [
        "Invertir en acciones de empresas tecnológicas enfocadas en inteligencia artificial.",
        "Explorar fondos indexados que sigan el rendimiento de mercados emergentes.",
        "Considerar inversiones en energías renovables, como la solar y eólica.",
        "Evaluar oportunidades en el sector de la salud y biotecnología.",
        "Analizar inversiones en criptomonedas establecidas, como Bitcoin y Ethereum."
    ]
    return random.choice(inversiones)

# Ideas para generar ingresos pasivos
def ideas_ingresos_pasivos():
    ideas = [
        "Crear y vender un curso en línea sobre una habilidad que domines.",
        "Escribir un libro electrónico y publicarlo en plataformas digitales.",
        "Invertir en bienes raíces para alquilar propiedades.",
        "Participar en programas de marketing de afiliación.",
        "Desarrollar una aplicación móvil con funcionalidades útiles."
    ]
    return random.choice(ideas)

# Simulación de búsqueda de inversiones en la red
def buscar_inversiones_en_red():
    # Esta función simula una búsqueda en la red. Puedes expandirla para realizar scraping o consultar APIs.
    tendencias = [
        "La inteligencia artificial está revolucionando múltiples industrias.",
        "Las energías renovables continúan siendo una inversión sólida a largo plazo.",
        "El sector de la salud y biotecnología muestra un crecimiento constante.",
        "Las criptomonedas siguen siendo volátiles pero con potencial de alta rentabilidad.",
        "La inversión en bienes raíces sigue siendo una opción segura en muchas regiones."
    ]
    return random.choice(tendencias)

# Análisis de inversión basado en el texto proporcionado
def analizar_inversion(texto):
    texto = texto.lower()
    if "acciones" in texto:
        return "Considera diversificar tu cartera con acciones de diferentes sectores para mitigar riesgos."
    elif "fondos indexados" in texto or "etf" in texto:
        return "Los fondos indexados ofrecen una forma eficiente de invertir en una amplia gama de activos."
    elif "criptomonedas" in texto:
        return "Investiga y comprende los riesgos antes de invertir en criptomonedas debido a su alta volatilidad."
    elif "ingresos pasivos" in texto:
        return ideas_ingresos_pasivos()
    else:
        return sugerencia_inversion()
# Función principal para interactuar con el usuario
def main():
    print("Bienvenido al asistente de inversiones.")
    while True:
        print("\nOpciones:")
        print("1. Sugerencia de inversión")
        print("2. Ideas para generar ingresos pasivos")
        print("3. Buscar tendencias de inversión en la red")
        print("4. Analizar texto sobre inversiones")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            print(sugerencia_inversion())
        elif opcion == "2":
            print(ideas_ingresos_pasivos())
        elif opcion == "3":
            print(buscar_inversiones_en_red())
        elif opcion == "4":
            texto = input("Introduce el texto a analizar: ")
            print(analizar_inversion(texto))
        elif opcion == "5":
            print("Saliendo del asistente de inversiones.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
            
