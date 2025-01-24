# Desafio-Back-End---Larissa-de-Olvieira-

# Meu Projeto Django

Este projeto é uma API desenvolvida em Django que implementa autenticação de usuários com JWT e suporte a um banco de dados relacional PostgreSQL. A API permite a criação de usuários, consulta de saldo, adição de saldo à carteira, transferências entre usuários e listagem de transferências realizadas.

## Tecnologias Utilizadas

- Django
- Django REST Framework
- djangorestframework-simplejwt
- PostgreSQL

## Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:

- Python 3.8 ou superior
- PostgreSQL
- pip

## Configuração do Ambiente

1. Clone o repositório:

   ```
   git clone <URL_DO_REPOSITORIO>
   cd meu-projeto-django
   ```

2. Crie um ambiente virtual:

   ```
   python -m venv venv
   ```

3. Ative o ambiente virtual:

   - No Windows:

     ```
     venv\Scripts\activate
     ```

   - No macOS/Linux:

     ```
     source venv/bin/activate
     ```

4. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

5. Configure o banco de dados PostgreSQL:

   - Crie um banco de dados no PostgreSQL.
   - Atualize as configurações do banco de dados no arquivo `meu_projeto/settings.py` com as credenciais do seu banco de dados.

## Executando o Servidor

Para iniciar o servidor de desenvolvimento, execute:

```
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`.

## Popular o Banco de Dados com Dados Fictícios

Para popular o banco de dados com dados fictícios, você pode criar um script de gerenciamento ou usar o shell do Django. Um exemplo de como fazer isso via shell:

1. Abra o shell do Django:

   ```
   python manage.py shell
   ```

2. Execute os comandos para criar usuários e dados fictícios.

## Funcionalidades

- **Autenticação de usuários com JWT**: Os usuários podem se registrar e fazer login para obter um token JWT.
- **Criação de usuários**: Endpoint para registrar novos usuários.
- **Consulta de saldo**: Endpoint para consultar o saldo da carteira de um usuário.
- **Adição de saldo**: Endpoint para adicionar saldo à carteira de um usuário.
- **Transferências entre usuários**: Endpoint para realizar transferências entre usuários.
- **Listagem de transferências**: Endpoint para listar transferências realizadas por um usuário, com filtro opcional por período de data.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Faça um fork do repositório e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
