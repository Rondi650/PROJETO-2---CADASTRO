import os
from config import PASTA, ARQUIVO_TXT

os.makedirs(PASTA, exist_ok=True)

def salvar_dados_txt(dicionario):
    with open(ARQUIVO_TXT, 'a') as f:
        for x in dicionario:
            f.write(str(f'{x['nome']},{x['email']},{x['idade']}\n'))
        
def ler_dados_txt():
    with open(ARQUIVO_TXT, 'r') as f:
        conteudo = f.read()
        print(f'{'-'*50} \nDADOS TXT\n{conteudo}\n {'-'*50}')
