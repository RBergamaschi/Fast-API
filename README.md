# 🏋️‍♀️ Fitness API com FastAPI

Uma API REST para gerenciamento de atividades físicas, desenvolvida com **FastAPI** e **SQLAlchemy**. A aplicação permite registrar atividades como corridas, caminhadas e exercícios diversos, com suporte a validações, relatórios e filtros por usuário, nome e data.

---

## 📌 Sumário

- [📷 Visão Geral](#-visão-geral)
- [🚀 Execução](#-execução)
- [📋 Endpoints da API](#-endpoints-da-api)
- [✅ Validações Aplicadas](#-validações-aplicadas)
- [📋 Documentação](#-documentação)
- [🔧 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [🗂 Estrutura de Pastas (sugestiva)](#-estrutura-de-pastas-sugestiva)
- [📚 Justificativas Técnicas](#-justificativas-técnicas)
- [👤 Autor](#-autor)

---

## 📷 Visão Geral

Este projeto backend fornece uma interface robusta para rastrear atividades físicas dos usuários com os seguintes recursos:

- Cadastro e controle de atividades
- Filtros por data, nome e usuário
- Atualização parcial (PATCH)
- Estatísticas por usuário (duração, calorias, etc.)
- Documentação Swagger e Redoc gerada automaticamente

---

## 🚀 Execução

### Pré-requisitos

- Python 3.12
- [Poetry](https://python-poetry.org/)
- [Pyenv](https://github.com/pyenv-win/pyenv-win)
- [Pipx](https://pypa.github.io/pipx/)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/RBergamaschi/Fast-API.git
cd Fast-API

# Instale pyenv (PowerShell)
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

# Instale Poetry via Pipx
pip install pipx
pipx install poetry
pipx ensurepath -> para colocar as variáveis de ambiente do pipx nas variáveis de ambiente do sistema
poetry add fastapi
poetry add --group dev ruff
poettry add --group dev taskipy
poetry add --group dev pytest pytest-cov
```
### ⚙️ Configurando o ambiente e as dependências(no pyproject.toml)
```
requires-python = ">=3.12,<4"

Ruff:
[tool.ruff]
line-length = 79
extend-exclude = ['migrations']

[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PL']

[tool.ruff.format]
preview = true
quote-style = 'single'

Taskipy:
[tool.taskipy.tasks]
run = 'fastapi dev fast_zero\app.py'
pre_test = 'task lint'
test = 'pytest --cov=fast_zero -vv'
lint = 'ruff check . && ruff check . --diff'
format = 'ruff check . --fix && ruff format .'

Pytest:
[tool.pytest.ini_options]
pythonpath="."
```
# Iniciando o poetry e o fastapi
```
poetry env activate
poetry run task run
```

# 📋 Endpoints da API
🔸 GET /
Mensagem de boas-vindas.

🔸 POST /atividades/
Cria uma nova atividade física.

```📦 Exemplo:
{
  "nome": "Corrida",
  "duracao": 30,
  "data": "2025-06-15",
  "distancia": 5.0,
  "calorias": 250.0,
  "username": "joao"
}
```
🔸 GET /atividades/
Lista todas as atividades. Filtros opcionais:

- username
- nome_atividade
- data

🔸 PATCH /atividades/{id_atividade}
Atualiza apenas os campos enviados. Campos permitidos:
- nome
- duração
- calorias
- distância

```📦 Exemplo:
{
  "duracao": 45
}
```
🔸 DELETE /atividades/{id_atividade}
Remove uma atividade pelo ID.

🔸 GET /atividades/somatorio/{username}
Retorna estatísticas do usuário:

- Total de atividades
- Total de minutos
- Média de duração
- Total de calorias

# ✅ Validações Aplicadas

- 📛 Nome: mínimo 1 caractere.

- ⏱ Duração: maior que 0.

- 🔥 Calorias: não negativas.

- 🛣 Distância: não negativa.

- 📅 Data: não pode estar no passado.

- 🚫 Nenhum campo obrigatório pode estar vazio ou inválido.

# 📋 Documentação 

- Swagger: 127.0.0.1:8000/docs

- Redoc: 127.0.0.1:8000/redoc

# 🔧 Tecnologias Utilizadas

- 🐍 Python 3.12

- 🚀 FastAPI

- 🛢 SQLAlchemy + SQLite

- 📦 Poetry

- 📐 Pydantic

- 🧪 Pytest + Coverage

- 🛠 Ruff (lint)

- 📌 Taskipy

- 📍 Pyenv + Pipx

# 🗂 Estrutura de Pastas (sugestiva)
```bash
fast_zero/
  ├── app.py                   # Inicialização da aplicação
  ├── database.py              # Configuração do banco e sessão
  ├── models.py                # Definições ORM
  ├── crud.py                  # Operações com banco            
  ├── schemas_atividades.py    # Schemas (entrada e saída)
fast_zero/routers
    ├── atividades.py          # Rotas da API
```
# 📚 Justificativas Técnicas
FastAPI oferece docs automáticas e alta performance

SQLite + SQLAlchemy simplificam persistência

Taskipy otimiza comandos de execução/testes

Ruff mantém o código limpo e padronizado

O projeto é estruturado para facilitar expansão e manutenção futura

# 👤 Autor
Desenvolvido por Rodrigo Torres Bergamaschi

Curso: Engenharia de Computação

Contato: [rodrigotberga21@gmail.com]

Repositório: github.com/RBergamaschi/Fast-API
