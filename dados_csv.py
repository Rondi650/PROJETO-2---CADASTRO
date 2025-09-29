import csv, os
from config import PASTA, ARQUIVO_CSV

os.makedirs(PASTA,exist_ok=True)

def salvar_dados_csv(dados):
    arquivo_existe = os.path.exists(ARQUIVO_CSV)
    with open(ARQUIVO_CSV, 'a', newline='') as f:
        escritor = csv.DictWriter(f, fieldnames=['nome','email','idade'])
        if not arquivo_existe:
            escritor.writeheader()
        escritor.writerows(dados)
        
def ler_dados_csv():
    with open(ARQUIVO_CSV, 'r', newline='') as f:
        leitor = csv.DictReader(f)
        print(f'{'-'*50} \nDADOS CSV')
        for dado in leitor:
            print(f'{dado['nome']} - {dado['email']} - {dado['idade']}')
        print(f'{'-'*50}')