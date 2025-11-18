Documentação do Sistema de Controle de Ferramentas
Descrição
Este sistema permite o cadastro, consulta e gerenciamento de ferramentas utilizadas pela empresa. A interface gráfica foi desenvolvida com Tkinter, utilizando banco de dados SQLite. O sistema suporta leitura de QR Code para facilitar o preenchimento dos dados e busca automática das informações da ferramenta.

Funcionalidades
Cadastro de Ferramentas:
Preencha os campos e clique em "Salvar" para registrar uma nova ferramenta.

Leitura de QR Code:
Clique em "Ler QR Code" para capturar o código via webcam. O campo "Código" será preenchido automaticamente e os dados da ferramenta serão buscados.

Consulta de Ferramentas:
Clique em "Consultar Ferramentas" para visualizar uma lista de todas as ferramentas cadastradas, com nome, código, responsável e situação.

Busca pelo Código:
Digite ou leia o código da ferramenta e clique em "Buscar pelo Código" para preencher todos os campos com as informações cadastradas.

Como Usar
Instalação dos Requisitos

Execute no terminal:

pip install opencv-python pyzbar
Execução

Navegue até a pasta do arquivo app.py:

cd controle-ferramentas\src
Execute o sistema:

python [app.py](http://_vscodecontentref_/0)
Interface

A janela ocupará toda a tela.
Preencha os campos ou utilize o QR Code para buscar/cadastrar ferramentas.
Utilize os botões para salvar, consultar ou buscar ferramentas.
Estrutura dos Dados
Cada ferramenta possui os seguintes campos:

Nome
Código (único, pode ser lido via QR Code)
Categoria
Localização
Responsável
Data de Aquisição
Situação
Observações
O banco de dados é criado automaticamente no arquivo ferramentas.db.
Evite duplicidade de códigos, pois o campo é único.
O sistema foi projetado para uso em Windows, mas pode ser adaptado para outros sistemas.
Dúvidas ou Melhorias
Caso queira adicionar novas funcionalidades, melhorar a interface ou integrar com outros sistemas, entre em contato com o desenvolvedor ou consulte a documentação do Tkinter e SQLite.

Nome
Código (único, pode ser lido via QR Code)
Categoria
Localização
Responsável
Data de Aquisição
Situação
Observações
O banco de dados é criado automaticamente no arquivo ferramentas.db.
Evite duplicidade de códigos, pois o campo é único.
O sistema foi projetado para uso em Windows, mas pode ser adaptado para outros sistemas.
Dúvidas ou Melhorias
Caso queira adicionar novas funcionalidades, melhorar a interface ou integrar com outros sistemas, entre em contato com o desenvolvedor ou consulte a documentação do Tkinter e SQLite.

Desenvolvido por:
Daniel Batista
19 de agosto de 2025



