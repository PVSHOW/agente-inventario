import sqlite3
import csv

def exportar_para_csv():
    # Conectar ao banco de dados
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    # Buscar os dados
    cursor.execute("SELECT * FROM maquinas")
    dados = cursor.fetchall()

    # Buscar os nomes das colunas
    colunas = [descricao[0] for descricao in cursor.description]

    # Escrever o CSV
    with open("inventario_exportado.csv", "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(colunas)  # cabeçalhos
        writer.writerows(dados)   # dados

    # Finalizar
    conn.close()
    print("[INFO] Exportação para CSV concluída com sucesso!")

if __name__ == "__main__":
    exportar_para_csv()
