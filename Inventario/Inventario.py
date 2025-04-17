import os
import platform
import socket
import psutil
import sqlite3
import time

def coletar_dados():
    """Coleta informações do sistema."""
    dados = {
        "hostname": socket.gethostname(),
        "sistema_operacional": platform.system() + " " + platform.release(),
        "processador": platform.processor(),
        "memoria_ram": round(psutil.virtual_memory().total / (1024**3), 2),  # Em GB
        "espaco_disco": round(psutil.disk_usage('/').total / (1024**3), 2),  # Em GB
        "endereco_ip": socket.gethostbyname(socket.gethostname())
    }
    return dados

def salvar_dados(dados):
    """Salva os dados em um banco SQLite."""
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS maquinas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        hostname TEXT,
                        sistema_operacional TEXT,
                        processador TEXT,
                        memoria_ram REAL,
                        espaco_disco REAL,
                        endereco_ip TEXT,
                        data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    cursor.execute('''INSERT INTO maquinas (hostname, sistema_operacional, processador, memoria_ram, espaco_disco, endereco_ip)
                      VALUES (?, ?, ?, ?, ?, ?)''',
                   (dados["hostname"], dados["sistema_operacional"], dados["processador"],
                    dados["memoria_ram"], dados["espaco_disco"], dados["endereco_ip"]))
    conn.commit()
    conn.close()

def main():
    while True:
        dados = coletar_dados()
        salvar_dados(dados)
        print("[INFO] Dados coletados e salvos com sucesso!")
        time.sleep(3600)  # Executa a coleta a cada 1 hora

if __name__ == "__main__":
    main()
