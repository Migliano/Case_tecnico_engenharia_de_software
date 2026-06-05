# Sistema de Cadastro de Pessoas
Aplicação full stack para cadastro de pessoas com geração automática de login único.
Desenvolvida como case técnico

# Tecnologias
Backend

Python 3.14
Flask 3.1
Flask-SQLAlchemy 3.1
SQLite
flask-cors
validate-docbr (validação de CPF)
email-validator
pandas

Frontend

HTML5 + CSS3
JavaScript (Vanilla)
Bootstrap 5.3
Bootstrap Icons


# Estrutura do Projeto
```
Case_tecnico_engenharia_de_software/
├── backend/
│   ├── run.py                  ← inicia o servidor
│   ├── massa_dados.txt         ← registros iniciais
│   ├── requirements.txt        ← dependências do projeto
│   └── app/
│       ├── __init__.py         ← cria a aplicação (Application Factory)
│       ├── config.py           ← configurações (banco, chave secreta)
│       ├── extensions.py       ← instância do SQLAlchemy
│       ├── models.py           ← modelo da tabela de usuários
│       ├── commands.py         ← comandos CLI (criar/limpar banco)
│       ├── routes/
│       │   └── main.py         ← rotas HTTP (GET / e POST /cadastro)
│       ├── utils/
│       │   ├── login_generator.py  ← lógica de geração de login único
│       │   └── sanity_check.py     ← validações de dados
│       ├── templates/
│       │   └── index.html      ← interface do usuário
│       └── static/
│           ├── script.js       ← lógica de formulário e fetch
│           ├── ui.js           ← funções de interface (toggle, troca de tela)
│           └── style.css       ← identidade visual
└── README.md
```

# Como Rodar o Projeto
Pré-requisitos

Python 3.9+
pip

Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/Migliano/Case_tecnico_engenharia_de_software.git
cd Case_tecnico_engenharia_de_software
```

**2. Entre na pasta backend e ative o ambiente virtual**
```bash
cd backend
python -m venv venv
```

Windows
```bash
venv\Scripts\activate
```

Linux/Mac
```bash
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Crie o banco e popule com os dados iniciais**
```bash
flask --app run create_tables
```
Este comando cria a tabela cadastro_usuarios e insere automaticamente os 20 registros do arquivo massa_dados.txt.

**5. Suba o servidor**
```bash
python run.py
```

**6. Acesse a aplicação**

http://127.0.0.1:5000

# Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | / | Retorna a interface do usuário |
| POST | /cadastro | Recebe dados, valida, gera login e salva |

Exemplo de requisição (POST /cadastro)
```json
{
    "nome": "Ana Beatriz Ferreira",
    "cpf": "12345678909",
    "email": "ana@email.com",
    "data_nascimento": "1998-03-14",
    "cep": "01310100",
    "endereco": "Avenida Paulista"
}
```

Exemplo de resposta (200 OK)
```json
{
    "login": "anabeat"
}
```

Exemplo de resposta de erro (400 Bad Request)
```json
{
    "erro": "CPF invalido"
}
```

# Lógica de Geração de Login
O login é gerado automaticamente a partir do nome completo da pessoa, respeitando as regras:

Exatamente 7 caracteres
Apenas letras minúsculas (a-z)
Sem espaços ou números
Único — não pode se repetir

Estratégias de geração (em ordem de prioridade)
O sistema tenta cada estratégia até encontrar um login disponível:

Generator 1 — 7 primeiras letras do nome normalizado (sem espaços)

Ana Beatriz Ferreira → anabeat


Generator 2 — 4 primeiras + 3 últimas letras do nome normalizado

Ana Beatriz Ferreira → anaerra


Generator 3 — 5 primeiras + 2 últimas letras do nome normalizado

Ana Beatriz Ferreira → anabera


Generator 4 — Iniciais de cada palavra + primeiras letras do nome até completar 7

Ana Beatriz Ferreira → abfanab


Generator 5 (coringa) — Janelas deslizantes de 7 letras pelo nome normalizado

Percorre o nome inteiro gerando todas as combinações possíveis de 7 letras consecutivas
Praticamente elimina a chance de não encontrar um login disponível



Garantia de unicidade
Antes de gerar, o sistema consulta todos os logins existentes no banco. Se um candidato já existir, avança para o próximo. O sistema só salva quando encontra um login livre.

# Validações
Frontend (JavaScript)

Campos obrigatórios
Limite de caracteres por campo
Formato de CPF (11 dígitos numéricos + dígitos verificadores)
Formato de e-mail
Data de nascimento não pode ser futura

Backend (Python)
Segunda barreira de segurança — valida mesmo que o frontend seja bypassado (ex: via Postman).

Nome: obrigatório, sem acentos ou caracteres especiais
CPF: validação matemática dos dígitos verificadores via validate-docbr
E-mail: formato válido via email-validator
Data: formato YYYY-MM-DD, não pode ser futura
CEP: 8 dígitos numéricos


# Funcionalidades

Tela de boas-vindas antes do formulário
Preenchimento automático de endereço via ViaCEP
Login gerado exibido de forma oculta (*******) com botão para revelar
Botão de envio desativado após cadastro realizado
Feedback visual de erros diretamente na tela


# Comandos Úteis
```bash
# Criar tabelas e popular banco
flask --app run create_tables

# Limpar banco
flask --app run drop_tables
```

# Decisões Técnicas
SQLite — escolhido pela simplicidade de configuração local. Não requer servidor de banco de dados separado, facilitando a execução pelo avaliador.
Flask Application Factory — padrão create_app() que permite configurar a aplicação de forma modular e facilita testes.
Separação frontend/backend — o Flask serve o frontend via templates/ e static/, mantendo a separação de responsabilidades enquanto simplifica a execução (um servidor só).
CPF como String — armazenado como texto para preservar zeros à esquerda (ex: 001.234.567-89). O mesmo vale para o CEP.
Validação dupla — frontend para experiência do usuário, backend como barreira de segurança real. Quem conhece a API pode bypassar o JavaScript.

# Melhorias Futuras

Máscara de input para CPF e CEP no frontend
Deploy em nuvem
Autenticação para acesso ao sistema
