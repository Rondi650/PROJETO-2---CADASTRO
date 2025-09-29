import os

CAMINHO = os.path.abspath(os.path.dirname(__file__))
PASTA = os.path.join(CAMINHO,'uploads')

ARQUIVO_CSV = os.path.join(PASTA, 'dados.csv')
ARQUIVO_TXT = os.path.join(PASTA, 'dados.txt')
ARQUIVO_JSON = os.path.join(PASTA, 'dados.json')
