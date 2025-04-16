import time
from Inventario.coletor import coletar_dados
from Inventario.banco import salvar_dados

def main():
    while True:
        dados = coletar_dados()
        salvar_dados(dados)
        print("[INFO] Dados coletados e salvos com sucesso!")
        time.sleep(3600)

if __name__ == "__main__":
    main()
