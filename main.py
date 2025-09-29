from base_model import Usuario
from pydantic import ValidationError
import os, sys
from dados_csv import salvar_dados_csv, ler_dados_csv
from config import ARQUIVO_CSV, ARQUIVO_JSON, ARQUIVO_TXT
from dados_json import salvar_dados_json, ler_dados_json
from dados_txt import salvar_dados_txt, ler_dados_txt

os.system('cls')
      
def sair_do_programa():
    os.system('cls')
    print('SAINDO DO PROGRAMA...\n')
    
def menu_principal():
    while True:
        entrada = input('Escolha sua opcao:\n'
                            'Digite 1 para Cadastrar Usuarios;\n'
                            'Digite 2 para ver a listagem TXT;\n'
                            'Digite 3 para ver a listagem CSV;\n'
                            'Digite 4 para ver a listagem JSON;\n'
                            'Digite 5 para Sair;\n'
                            'Digite: ').strip()
        
        if entrada == '1':
            os.system('cls')
            cadastro_usuario()
        elif entrada == '2':
            os.system('cls')
            ler_dados_txt()
        elif entrada == '3':
            os.system('cls')
            ler_dados_csv()
        elif entrada == '4':
            os.system('cls')
            ler_dados_json()
        elif entrada == '5':
            sair_do_programa()
            sys.exit()
        else:
            os.system('cls')
            print('Entrada invalida!\n')
    
lista = []
def cadastro_usuario():
    while True:
        
        try:
            nome = input('Digite o nome do usuario: ').strip()
            email = input('Digite o email do usuario: ').strip()
            idade = int(input('Digite a idade: '))
            dados = Usuario(nome=nome, email=email, idade=idade)
            dicionario = {'nome':dados.nome, 'email': dados.email, 'idade':dados.idade}
            lista.append(dicionario)
            
            novo_cadastro = input('Deseja cadastrar novo usuario? (S/N): ')
            if novo_cadastro.lower() == 's':
                continue
            else:
                sub_menu()
                break
        
        except (ValueError, Exception, ValidationError) as e:
            os.system('cls')
            print(f'Erro, dados incorretos: {e}.\n')
            continuar = input('Deseja cadastrar outro usuario: digite "S" para continuar ou qualquer outra tecla para voltar ao menu principal: ')
            if continuar.lower() != 's':
                os.system('cls')
                menu_principal()
                break

def sub_menu():
    while True:
        entrada = input('\nEm que tipo de arquivo deseja salvar os dados?\n'
                        'Digite 1 para CSV;\n'
                        'Digite 2 para TXT;\n'
                        'Digite 3 para JSON;\n'
                        'Digite 4 para voltar ao menu principal;\n'
                        'Digite 5 para Sair;\n'
                        'Digite: ').strip()
        
        if entrada == '1':
            os.system('cls')
            print(f'Dados Salvos em CSV na pasta: {ARQUIVO_CSV}')
            salvar_dados_csv(lista)
            ler_dados_csv()
            lista.clear()
            break
        elif entrada == '2':
            os.system('cls')
            print(f'Dados Salvos em TXT na pasta: {ARQUIVO_TXT}')
            salvar_dados_txt(lista)
            ler_dados_txt()
            lista.clear()
            break
        elif entrada == '3':
            os.system('cls')
            print(f'Dados Salvos em JSON na pasta: {ARQUIVO_JSON}')
            salvar_dados_json(lista)
            ler_dados_json()
            lista.clear()
            break
        elif entrada == '4':
            menu_principal()
            break
        elif entrada == '5':
            sair_do_programa()
            sys.exit()
        else:
            print('\nEntrada invalida!')
         
def main():   
   menu_principal()

if __name__ == '__main__':
    main()