# modules/code_helper.py

def ayuda_con_codigo():
    """
    Función base para responder a consultas generales sobre programación.
    """
    return "¿En qué lenguaje o tema de programación necesitas ayuda?"

def ayuda_codigo(texto):
    """
    Función que recibe un texto (consulta) y devuelve una respuesta básica.
    Aquí podrías integrar algún modelo de IA o base de conocimiento.
    """
    texto = texto.lower()

    if "python" in texto:
        return ("Python es un lenguaje de programación muy popular, "
                "ideal para desarrollo web, análisis de datos y automatización. "
                "¿Quieres un ejemplo básico?")
    elif "javascript" in texto:
        return ("JavaScript es el lenguaje principal para desarrollo web frontend. "
                "Permite crear páginas web interactivas.")
    elif "qué es una función" in texto:
        return ("Una función es un bloque de código reutilizable que realiza una tarea específica.")
    elif "ejemplo" in texto:
        return ("Aquí tienes un ejemplo básico de función en Python:\n"
                "def saludar(nombre):\n"
                "    return f'Hola, {nombre}!'")
    else:
        return "Lo siento, no tengo información para esa consulta. ¿Quieres ayuda con algo más?"

# Puedes agregar funciones más avanzadas para analizar código, generar snippets, etc.

def analizar_codigo(texto):
    """
    Función que analiza el código proporcionado y devuelve un resumen o error.
    Aquí podrías integrar un analizador de código o un modelo de IA.
    Además, se agregan funciones avanzadas para mejorar el análisis.
    """

    # Eliminar espacios innecesarios
    texto = texto.strip()

    # Verificar si el texto está vacío
    if not texto:
        return "No se proporcionó ningún código para analizar."

    # Verificar si el código contiene palabras clave comunes de Python
    keywords = ["def", "class", "import", "for", "while", "if", "else", "elif", "return"]
    encontrados = [kw for kw in keywords if kw in texto]
    if encontrados:
        return f"El código contiene las siguientes palabras clave de Python: {', '.join(encontrados)}."

    # Verificar si el código parece tener indentación incorrecta
    lines = texto.split('\n')
    for i, line in enumerate(lines):
        if line.startswith(' ') and (len(line) - len(line.lstrip(' '))) % 4 != 0:
            return f"Posible problema de indentación en la línea {i+1}."

    # Simulación de análisis de código
    if "error" in texto:
        return "Se ha detectado un error en el código. Revisa la sintaxis."
    elif "bueno" in texto:
        return "El código parece estar bien estructurado."

    # Si no se detecta nada relevante
    return "El análisis avanzado no detectó problemas evidentes en el código."
def generar_snippet(texto):
    """
    Función que genera un snippet de código basado en la consulta.
    Aquí podrías integrar un generador de código o un modelo de IA.
    """
    # Simulación de generación de código
    if "hola mundo" in texto:
        return "print('Hola, mundo!')"
    elif "suma" in texto:
        return "def suma(a, b):\n    return a + b"
    else:
        return "No se pudo generar el snippet. Proporciona más detalles."