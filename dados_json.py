import json, os
from config import ARQUIVO_JSON, PASTA

os.makedirs(PASTA, exist_ok=True)
arquivo = ARQUIVO_JSON

def salvar_dados_json(dados_lista):
    lista_substituta = []
    if os.path.exists(ARQUIVO_JSON): # <-- verifica se o arquivo ja existe
        try:
            with open(arquivo, 'r') as f:
                lista_substituta = json.load(f) # <-- lista vazia recebe os dados 
        except ValueError as e:
            print(e)
            
    lista_substituta.extend(dados_lista) # <-- extend adiciona uma lista na outra
    
    with open(ARQUIVO_JSON, 'w') as f:
        json.dump(lista_substituta, f, indent=4)  # <-- dump para escrever
              
def ler_dados_json():
    with open(ARQUIVO_JSON, 'r') as f:
        ler_dados = json.load(f) # <-- load para ler
        print(f'{'-'*50} \nDADOS JSON\n{ler_dados}\n {'-'*50}')
        

