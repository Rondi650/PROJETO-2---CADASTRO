# Sistema de Cadastro de Usuários

Sistema simples de cadastro de usuários em Python que salva dados em CSV, TXT e JSON.

## Funcionalidades

- Cadastro de usuários (nome, email, idade)
- Validação de dados com Pydantic
- Salvamento em 3 formatos: CSV, TXT e JSON
- Menu interativo

## Como usar

1. Instale as dependências:
   ```
   pip install pydantic email-validator
   ```

2. Execute o programa:
   ```
   python main.py
   ```

3. Siga o menu para cadastrar usuários e visualizar dados

## Estrutura

```
├── main.py          # Programa principal
├── base_model.py    # Modelo de dados
├── config.py        # Configurações
├── dados_csv.py     # Funções CSV
├── dados_json.py    # Funções JSON
├── dados_txt.py     # Funções TXT
└── uploads/         # Arquivos salvos
    ├── dados.csv
    ├── dados.json
    └── dados.txt
```

---

Projeto desenvolvido para aprendizado em Python.
