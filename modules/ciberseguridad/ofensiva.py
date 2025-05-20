# modules/ciberseguridad/ofensiva.py

import socket
import subprocess
import platform

def escanear_puertos(host, puertos=[21, 22, 80, 443, 8080]):
    print(f"Escaneando puertos de {host}...")
    resultados = []
    for puerto in puertos:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((host, puerto))
        if resultado == 0:
            resultados.append((puerto, 'Abierto'))
        else:
            resultados.append((puerto, 'Cerrado'))
        sock.close()
    return resultados

def detectar_dispositivos_red():
    print("Escaneando red local (simulado)...")
    sistema = platform.system()
    comando = "arp -a" if sistema == "Windows" else "arp -a"
    try:
        resultado = subprocess.check_output(comando, shell=True).decode()
        return resultado
    except Exception as e:
        return f"Error al escanear red: {e}"

def fuerza_bruta_simulada(usuario, intentos):
    print(f"Simulando ataque de fuerza bruta a {usuario}...")
    for i, intento in enumerate(intentos, 1):
        print(f"Intento {i}: {intento}")
    return "Simulación finalizada"

if __name__ == "__main__":
    print(escanear_puertos("127.0.0.1"))
    print(detectar_dispositivos_red())
    print(fuerza_bruta_simulada("admin", ["1234", "admin", "password"]))
