import sqlite3

def salvar_dados(dados):
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS maquinas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hostname TEXT,
            sistema_operacional TEXT,
            processador TEXT,
            memoria_ram REAL,
            espaco_disco REAL,
            endereco_ip TEXT,
            data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    ''')
    cursor.execute('''
        INSERT INTO maquinas (hostname, sistema_operacional, processador, memoria_ram, espaco_disco, endereco_ip)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        dados["hostname"], dados["sistema_operacional"], dados["processador"],
        dados["memoria_ram"], dados["espaco_disco"], dados["endereco_ip"]
    ))
    conn.commit()
    conn.close()
