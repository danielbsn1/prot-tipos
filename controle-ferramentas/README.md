# Controle de Ferramentas

Este projeto é um protótipo para o controle de ferramentas utilizadas pela empresa. A aplicação permite que os usuários insiram informações sobre as ferramentas e as armazenem em um banco de dados SQLite. Além disso, a aplicação inclui uma funcionalidade para ler QR codes, facilitando a entrada de dados.

## Estrutura do Projeto

```
controle-ferramentas
├── src
│   ├── app.py          # Ponto de entrada da aplicação com interface gráfica
│   ├── db.py           # Funções para criar e gerenciar o banco de dados
│   ├── qr_reader.py     # Funcionalidade para leitura de QR codes
│   └── types
│       └── __init__.py # Definições de tipos e interfaces
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação do projeto
```

## Instalação

Para instalar as dependências do projeto, execute o seguinte comando:

```
pip install -r requirements.txt
```

## Uso

1. Execute o arquivo `src/app.py` para iniciar a aplicação.
2. Utilize a interface gráfica para inserir informações sobre as ferramentas.
3. Para usar a funcionalidade de leitura de QR codes, siga as instruções na interface.

## Funcionalidades

- Cadastro de ferramentas com informações como nome, código, categoria, localização, responsável, data de aquisição e situação.
- Leitura de QR codes para facilitar a entrada de dados.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.