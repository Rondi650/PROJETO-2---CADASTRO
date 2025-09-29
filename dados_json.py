import json, os
from config import ARQUIVO_JSON, PASTA

os.makedirs(PASTA, exist_ok=True)
arquivo = ARQUIVO_JSON

def salvar_dados_json(novos_dados):
    dados_existentes = []
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r') as f:
            try:
                dados_existentes = json.load(f)
            except ValueError as e:
                print(f'Erro: {e}')

    dados_existentes.extend(novos_dados) # <-- .extend = [1, 2, 3] ao inves de .append = [1, [2, 3]] 

    with open(ARQUIVO_JSON, 'w') as f:
        json.dump(dados_existentes, f, indent=4)
          
def ler_dados_json():
    with open(ARQUIVO_JSON, 'r') as f:
        ler_dados = json.load(f)
        print(ler_dados)
