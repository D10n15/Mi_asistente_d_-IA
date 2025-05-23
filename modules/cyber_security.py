import socket
import requests

def verificar_https(url):
    if not url.startswith("http"):
        url = "https://" + url
    try:
        response = requests.get(url)
        if response.url.startswith("https://"):
            return "✅ La conexión es segura (HTTPS activo)."
        else:
            return "⚠️ La conexión no es segura (HTTPS ausente)."
    except Exception as e:
        return f"❌ Error al acceder al sitio: {e}"

def analizar_cabeceras(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url
        response = requests.get(url)
        cabeceras = response.headers
        return "\n".join([f"{k}: {v}" for k, v in cabeceras.items()])
    except Exception as e:
        return f"❌ Error al analizar cabeceras: {e}"

def verificar_contraseña(password):
    largo = len(password)
    tiene_mayus = any(c.isupper() for c in password)
    tiene_num = any(c.isdigit() for c in password)
    tiene_especial = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

    score = sum([largo >= 8, tiene_mayus, tiene_num, tiene_especial])

    if score == 4:
        return "✅ Contraseña fuerte."
    elif score == 3:
        return "🟡 Contraseña moderada."
    else:
        return "🔴 Contraseña débil. Usa mayúsculas, números y símbolos."

def escanear_puertos(host, puertos=[21, 22, 80, 443, 3306]):
    resultados = []
    for puerto in puertos:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            sock.connect((host, puerto))
            resultados.append(f"✅ Puerto {puerto} está ABIERTO")
        except:
            resultados.append(f"❌ Puerto {puerto} está cerrado o filtrado")
        sock.close()
    return "\n".join(resultados)

def buscar_subdominios_simulado(dominio):
    subdominios = ["www", "mail", "ftp", "test", "admin"]
    encontrados = []
    for sub in subdominios:
        url = f"http://{sub}.{dominio}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code < 400:
                encontrados.append(f"🌐 Subdominio activo: {url}")
        except:
            continue
    if encontrados:
        return "\n".join(encontrados)
    return "❌ No se detectaron subdominios activos simulados."

def verificar_ssl(dominio):
    try:
        response = requests.get(f"https://{dominio}", timeout=5)
        if response.status_code == 200:
            return "✅ El dominio tiene un certificado SSL válido."
        else:
            return "⚠️ El dominio tiene un certificado SSL, pero no es válido."
    except requests.exceptions.SSLError:
        return "❌ El dominio no tiene un certificado SSL."
    except requests.exceptions.RequestException as e:
        return f"❌ Error al verificar el SSL: {e}"