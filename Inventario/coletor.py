import platform
import socket
import psutil

def coletar_dados():
    return {
        "hostname": socket.gethostname(),
        "sistema_operacional": platform.system() + " " + platform.release(),
        "processador": platform.processor(),
        "memoria_ram": round(psutil.virtual_memory().total / (1024**3), 2),
        "espaco_disco": round(psutil.disk_usage('/').total / (1024**3), 2),
        "endereco_ip": socket.gethostbyname(socket.gethostname())
    }
