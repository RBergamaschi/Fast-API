# Fitness API

Uma API REST desenvolvida com **FastAPI** para gerenciar atividades físicas dos usuários. Permite **criação**, **listagem**, **atualização**, **deleção** e **resumo estatístico** das atividades registradas.

---

## Tecnologias Utilizadas:

- Python 3.12+
- FastAPI
- SQLite (via SQLAlchemy)
- Pydantic
- Ruff
- Taskipy
- Pytest
- Poetry
- Pyenv
- pipx

---

## Como executar o projeto:

### 1. Clonar o projeto no repositório:

    git clone https://github.com/RBergamaschi/Fast-API.git

### 2. Instalar as dependências:

    1. Pyenv: Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1", no power shell, cmd, etc

    2. pip install pipx
    3. pipx install poetry
    4. pipx ensurepath -> para colocar as variáveis de ambiente do pipx nas variáveis de ambiente do sistema
    5. poetry add fastapi
    6. poetry add --group dev ruff
    7. poettry add --group dev taskipy
    8. poetry add --group dev pytest pytest-cov

## Configurando as dependências(no pyproject.toml):

    1. Ruff:
        [tool.ruff]
        line-length = 79
        extend-exclude = ['migrations']

        [tool.ruff.lint]
        preview = true
        select = ['I', 'F', 'E', 'W', 'PL', 'PL']

        [tool.ruff.format]
        preview = true
        quote-style = 'single'
    2. Taskipy:
        [tool.taskipy.tasks]
        run = 'fastapi dev fast_zero\app.py'
        pre_test = 'task lint'
        test = 'pytest --cov=fast_zero -vv'
        lint = 'ruff check . && ruff check . --diff'
        format = 'ruff check . --fix && ruff format .'
    3. Pytest:
        [tool.pytest.ini_options]
        pythonpath="."
### Iniciando o projeto:
    1. poetry env activate
    2. poetry run task run -> ja que configuramos o taskipy e falamos que o run seria o comando para iniciar o fastapi
### Documentação Automática:
    Swagger: http://127.0.0.1:8000/docs
    Redoc: http://127.0.0.1:8000/redoc

### EndPoits:

    1. GET('/')
        Messagem de boas vindas.

    2. POST('/atividades/')
        Cria uma nova atividade física.
        exemplo(JSON):
            {
                "nome": "Corrida",
                "duracao": 30,
                "data": "2025-06-15",
                "distancia": 5.0,
                "calorias": 250.0,
                "username": "joao"
            }

    3. GET('/atividades/')
        Lista todas as atividades com filtros opicionais.
        Parâmetros de quarry(filtros):
            1. Username
            2. Nome da atividade
            3. Data
    
    4. PATCH('/atividades/{id_atividade}')
        Atualiza parcialmente uma atividade(somente os campos enviados, e so é permitido atualizar o nome da atividade, a duração, as calorias queimadas e a distância)
        exemplo(JSON):
            {
                "duracao": 45
            }
    
    5.DELETE('atividades/{id_atividade}')
        Remove uma atividade pelo ID

    6. GET('/atividades/somatorio/{username}')
        Retorna o total de atividades, soma de minutos, média de duração e calorias do usuário.


### Validações Aplicadas:

    1.Nome: mínimo 1 caractere.
    2.Duração: deve ser maior que 0.
    3.Calorias e distância: não podem ser negativas.
    4.Data: não pode ser no passado.
    5.Nenhum campo obrigatório pode estar vazio ou inválido.

