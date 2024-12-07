# SecretFriendAPI

**SecretFriendAPI** é uma aplicação web completa que permite o gerenciamento de grupos de amigo secreto e a realização do sorteio. A aplicação inclui tanto o **backend (API)** quanto o **frontend (interface de usuário)**, permitindo que você crie grupos, adicione participantes e realize o sorteio de maneira automatizada.

---

## Funcionalidades

### **Backend (API)**

- **Gerenciamento de Grupos**:
  - **GET** `/grupo`: Lista todos os grupos cadastrados.
  - **GET** `/grupo/<grupo_id>`: Retorna as informações de um grupo específico.
  - **POST** `/grupo`: Cria um novo grupo.
  - **DELETE** `/grupo/<grupo_id>`: Exclui um grupo.

- **Gerenciamento de Participantes**:
  - **GET** `/participante/<grupo_id>`: Lista todos os participantes de um grupo.
  - **POST** `/participante/<grupo_id>`: Adiciona um novo participante a um grupo.
  - **DELETE** `/participante/<participante_id>`: Exclui um participante de um grupo.

- **Sorteio de Amigo Secreto**:
  - **GET** `/sorteio/<grupo_id>`: Realiza o sorteio de amigo secreto para um grupo.

### **Frontend**

O frontend da aplicação é composto por **4 templates HTML** principais, onde os usuários podem interagir com a API de maneira visual:

- **index.html**: Tela inicial.
- **grupo.html**: Exibe a lista de grupos e permite criar novos grupos.
- **participante.html**: Mostra os participantes de um grupo e permite adicionar ou remover participantes.
- **sorteio.html**: Realiza o sorteio de amigo secreto, exibindo os resultados dos pares de amigos secretos.

---

## Tecnologias Usadas

- **Backend**: Python, Flask
- **Banco de Dados**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Controle de versão**: Git, GitHub
- **Outros**: Flask-CORS (para permitir CORS entre o frontend e o backend)

---

## Como Rodar o Projeto

### **Pré-requisitos**

Certifique-se de que possui os seguintes itens instalados:

- **Python 3.x**: [Download](https://www.python.org/downloads/)
- **PostgreSQL**: [Download](https://www.postgresql.org/download/)
- **Git**: [Download](https://git-scm.com/downloads)

### **Passo a Passo**

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/Aegdae/SecretFriendAPI.git
   cd SecretFriendAPI


2. **Crie e Ative um Ambiente Virtual**
   ```bash
   python -m venv venv
   source venv/bin/acrtive  #Para Linux
   venv\script\active  #Para Windows


3. **Instale as Dependências**
   ```bash
   pip install -r requirements.txt


4. **Configure o Banco de Dados**
   - Crie o banco de dados PostgreSQL:
   ```sql
   CREATE DATABASE secret_friend;
  - Atualeze as credencias de conexão no arquivo de configuração **config.py** (ou onde você configurou a conexão com o banco de dados).

5. **Inicie o Servidor Backend**
   ```bash
   python app.py

6. **Acesse o Frontend**
   - Abra o navegador e acesse a aplicação frontend em http://localhost:5000.
   - A interface permitirá que você interaja com a aplicação e realize as ações de gerenciamento de grupo, participantes e sorteio.
  


# Endpoints da SecretFriendAPI

Este documento descreve todos os **endpoints** disponíveis na aplicação **SecretFriendAPI**, tanto para o gerenciamento de grupos, participantes, quanto para realizar o sorteio de amigo secreto.

---

## **Gerenciamento de Grupos**

### **1. GET** `/grupo`
- **Descrição**: Lista todos os grupos cadastrados.
- **Resposta**:
    ```json
    [
      {"grupo_id": 1, "grupo_name": "Amigos da Escola"},
      {"grupo_id": 2, "grupo_name": "Natal 2024"}
    ]
    ```

### **2. GET** `/grupo/<grupo_id>`
- **Descrição**: Retorna as informações de um grupo específico.
- **Parâmetros**:
  - `grupo_id`: ID do grupo a ser consultado.
- **Resposta**:
    ```json
    {
      "grupo_id": 1,
      "grupo_name": "Amigos da Escola"
    }
    ```

### **3. POST** `/grupo`
- **Descrição**: Cria um novo grupo.
- **Corpo da Requisição**:
    ```json
    {
      "grupo_id": 3,
      "grupo_name": "Amigos do Trabalho"
    }
    ```
- **Resposta**:
  - `204 No Content` (Sem conteúdo de retorno).

### **4. DELETE** `/grupo/<grupo_id>`
- **Descrição**: Exclui um grupo específico.
- **Parâmetros**:
  - `grupo_id`: ID do grupo a ser excluído.
- **Resposta**:
  - `204 No Content` (Sem conteúdo de retorno).

---

## **Gerenciamento de Participantes**

### **1. GET** `/participante/<grupo_id>`
- **Descrição**: Lista todos os participantes de um grupo específico.
- **Parâmetros**:
  - `grupo_id`: ID do grupo.
- **Resposta**:
    ```json
    [
      {"part_id": 1, "part_name": "João", "grupo_id": 1},
      {"part_id": 2, "part_name": "Maria", "grupo_id": 1}
    ]
    ```

### **2. POST** `/participante/<grupo_id>`
- **Descrição**: Adiciona um participante a um grupo.
- **Parâmetros**:
  - `grupo_id`: ID do grupo.
- **Corpo da Requisição**:
    ```json
    {
      "part_id": 3,
      "part_name": "Carlos",
      "grupo_id": 1
    }
    ```
- **Resposta**:
  - `204 No Content` (Sem conteúdo de retorno).

### **3. DELETE** `/participante/<participante_id>`
- **Descrição**: Exclui um participante específico de um grupo.
- **Parâmetros**:
  - `participante_id`: ID do participante a ser excluído.
- **Resposta**:
  - `204 No Content` (Sem conteúdo de retorno).

---

## **Sorteio de Amigo Secreto**

### **1. GET** `/sorteio/<grupo_id>`
- **Descrição**: Realiza o sorteio de amigo secreto para um grupo.
- **Parâmetros**:
  - `grupo_id`: ID do grupo para o qual o sorteio será realizado.
- **Resposta**:
    ```json
    {
      "grupo_id": 1,
      "Amigo secreto": [
        {
          "parceiro_1": {"part_id": 1, "part_name": "João"},
          "parceiro_2": {"part_id": 2, "part_name": "Maria"}
        },
        {
          "parceiro_1": {"part_id": 2, "part_name": "Maria"},
          "parceiro_2": {"part_id": 1, "part_name": "João"}
        }
      ]
    }
    ```

---

## **Erros Comuns**

Aqui estão alguns erros que você pode encontrar ao interagir com a API:

### **1. Número Insuficiente de Participantes**
- **GET** `/sorteio/<grupo_id>`
- **Descrição**: Se houver menos de 2 participantes no grupo, o sorteio não será possível.
- **Resposta**:
    ```json
    {
      "Error": "Número insuficiente de participantes para o sorteio."
    }
    ```

### **2. Número Ímpar de Participantes**
- **GET** `/sorteio/<grupo_id>`
- **Descrição**: Se o número de participantes for ímpar, o sorteio não poderá ser realizado.
- **Resposta**:
    ```json
    {
      "Error": "Número ímpar de participantes. Não é possível formar todas as duplas."
    }
    ```

### **3. Campos Obrigatórios Faltando**
- **POST** `/grupo` ou **POST** `/participante/<grupo_id>`
- **Descrição**: Se faltar algum campo obrigatório, como `grupo_id`, `grupo_name`, `part_name`, ou `grupo_id`, o sistema retornará um erro.
- **Resposta**:
    ```json
    {
      "Error": "Campos 'grupo_id' e 'grupo_name' são obrigatórios."
    }
    ```

---

### **Licença**

Este projeto está licenciado sob a **MIT License**. Para mais detalhes, veja o arquivo [LICENSE](LICENSE).


### **Conclusão**

Agora você tem os **endpoints** completos documentados para a **SecretFriendAPI**. Eles cobrem todos os aspectos de gerenciamento de grupos, participantes e a realização do sorteio.
