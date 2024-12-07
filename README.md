SecretFriendAPI
SecretFriendAPI é uma aplicação backend desenvolvida com Python e Flask, que permite o gerenciamento de grupos de amigo secreto e o sorteio entre os participantes. A API oferece endpoints para criar e excluir grupos, adicionar e remover participantes, e realizar o sorteio do amigo secreto de forma automatizada.

Funcionalidades

Gerenciamento de Grupos:
  GET /grupo: Lista todos os grupos cadastrados.
  GET /grupo/<grupo_id>: Retorna as informações de um grupo específico.
  POST /grupo: Cria um novo grupo.
  DELETE /grupo/<grupo_id>: Exclui um grupo pelo seu ID.
  
Gerenciamento de Participantes:
  GET /participante/<grupo_id>: Lista todos os participantes de um grupo específico.
  POST /participante/<grupo_id>: Adiciona um novo participante ao grupo.
  DELETE /participante/<participante_id>: Exclui um participante de um grupo.

Sorteio de Amigo Secreto:
  GET /sorteio/<grupo_id>: Realiza o sorteio de amigo secreto para um grupo, retornando os pares de amigos secretos.

Tecnologias Usadas
Backend: Python, Flask
Banco de Dados: Utiliza um sistema de DAO (Data Access Object) para interagir com o banco de dados.
Banco de Dados Relacional: O código utiliza dois DAOs: GrupoDAO e ParticipanteDAO para gerenciar grupos e participantes.

Dependências:
Flask
Flask-CORS
Random (para embaralhar a lista de participantes durante o sorteio)


Como Rodar o Projeto

Pré-requisitos
Certifique-se de que possui os seguintes itens instalados:
Python 3.x: [Download](https://www.python.org/downloads/)
PostgreSQL ou outro banco de dados relacional (se estiver usando localmente, configure conforme o DAO).


Passo a Passo
  Clone o Repositório
    git clone https://github.com/Aegdae/SecretFriendAPI.git
    cd SecretFriendAPI

    
Crie e Ative um Ambiente Virtual
  python -m venv venv
  source venv/bin/activate  # Para Unix/Linux
  venv\Scripts\activate     # Para Windows

Instale as Dependências
  pip install -r requirements.txt

Configure o Banco de Dados
  Certifique-se de configurar o banco de dados corretamente no dao.py e entidade.py.

Inicie o Servidor
  python flaskapp.py

  
Acesse a API
  Acesse o servidor local em http://localhost:5000 e use ferramentas como Postman para testar os endpoints.

Endpoints Disponíveis
Gerenciamento de Grupos
GET /grupo
Descrição: Lista todos os grupos cadastrados.
Resposta:
  [
    {"grupo_id": 1, "grupo_name": "Amigos da Escola"},
    {"grupo_id": 2, "grupo_name": "Natal 2024"}
  ]
  
GET /grupo/<grupo_id>
Descrição: Retorna as informações de um grupo específico.
Resposta:
  {"grupo_id": 1, "grupo_name": "Amigos da Escola"}
  
POST /grupo
Descrição: Cria um novo grupo.
Corpo da Requisição:
  {
    "grupo_id": 1,
    "grupo_name": "Amigos do Trabalho"
  }
  Resposta: 204 No Content (Sem conteúdo de retorno)
  
DELETE /grupo/<grupo_id>
Descrição: Exclui um grupo específico.
Resposta: 204 No Content (Sem conteúdo de retorno)


Gerenciamento de Participantes
GET /participante/<grupo_id>
Descrição: Lista todos os participantes de um grupo específico.
Resposta:
  [
    {"part_id": 1, "part_name": "João", "grupo_id": 1},
    {"part_id": 2, "part_name": "Maria", "grupo_id": 1}
  ]

POST /participante/<grupo_id>
Descrição: Adiciona um participante a um grupo.
Corpo da Requisição:
  {
    "part_id": 1,
    "part_name": "Carlos",
    "grupo_id": 1
  }
  Resposta: 204 No Content (Sem conteúdo de retorno)


DELETE /participante/<participante_id>
Descrição: Exclui um participante pelo seu ID.
Resposta: 204 No Content (Sem conteúdo de retorno)


Sorteio de Amigo Secreto
GET /sorteio/<grupo_id>
Descrição: Realiza o sorteio de amigo secreto para um grupo.
Resposta:
  {
    "grupo_id": 1,
    "Amigo secreto": [
      {"parceiro_1": {"part_id": 1, "part_name": "João"}, "parceiro_2": {"part_id": 2, "part_name": "Maria"}},
      {"parceiro_1": {"part_id": 2, "part_name": "Maria"}, "parceiro_2": {"part_id": 1, "part_name": "João"}}
    ]
  }


Licença
Este projeto está licenciado sob a MIT License. Para mais detalhes, veja o arquivo LICENSE.
