import os
import socket
import hashlib
import time
import psutil

# --- Escaneo de puertos locales abiertos ---
def escanear_puertos_locales():
    print("Escaneando puertos abiertos en localhost...")
    puertos_abiertos = []
    for puerto in range(1, 1025):  # Escanea puertos del 1 al 1024
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        resultado = sock.connect_ex(('127.0.0.1', puerto))
        if resultado == 0:
            puertos_abiertos.append(puerto)
        sock.close()
    print("Puertos abiertos:", puertos_abiertos)
    return puertos_abiertos

# --- Verificar cambios en un archivo ---
def obtener_hash_archivo(ruta):
    with open(ruta, 'rb') as archivo:
        contenido = archivo.read()
        return hashlib.sha256(contenido).hexdigest()

def monitorear_cambios_archivo(ruta_archivo, intervalo=10):
    if not os.path.exists(ruta_archivo):
        print("Archivo no encontrado:", ruta_archivo)
        return
    hash_anterior = obtener_hash_archivo(ruta_archivo)
    print(f"Monitoreando cambios en: {ruta_archivo} (cada {intervalo}s)")
    while True:
        time.sleep(intervalo)
        hash_actual = obtener_hash_archivo(ruta_archivo)
        if hash_actual != hash_anterior:
            print("⚠️  Se detectó un cambio en el archivo:", ruta_archivo)
            break

# --- Mostrar conexiones de red activas ---
def mostrar_conexiones_activas():
    conexiones = psutil.net_connections()
    for c in conexiones:
        if c.status == "ESTABLISHED":
            print(f"Conexión establecida: {c.laddr} -> {c.raddr}")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    escanear_puertos_locales()
    mostrar_conexiones_activas()
    # monitorear_cambios_archivo("ruta/a/archivo.txt")
