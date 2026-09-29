# API de Eventos Acadêmicos

API RESTful desenvolvida com FastAPI para o gerenciamento de eventos acadêmicos
(palestras, workshops, minicursos, seminários e competições) e de seus participantes.

Os dados são armazenados em memória (listas Python), sem uso de banco de dados.

## Tecnologias

- Python
- FastAPI
- Pydantic

## Arquitetura

O projeto separa as responsabilidades em três arquivos, seguindo a ideia do MVC:

```
api-eventos/
├── main.py
├── models.py
├── services.py
├── routers.py
└── requirements.txt
```

- **models.py** (Model): define e valida os dados da aplicação, usando Pydantic.
- **services.py** (Service): contém as regras de negócio, como verificar se ainda
  existem vagas antes de confirmar uma inscrição.
- **routers.py** (Controller): define as rotas, recebe as requisições HTTP e
  devolve as respostas, sempre delegando o processamento para o services.py.
- **main.py**: cria a aplicação FastAPI e conecta as rotas.

## Instalação

1. Clone o repositório e entre na pasta do projeto.
2. Crie e ative um ambiente virtual:

```
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux ou macOS
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

## Execução

```
uvicorn main:app --reload
```

A API fica disponível em `http://127.0.0.1:8000`.

A documentação interativa (Swagger) fica em `http://127.0.0.1:8000/docs`.

## Principais rotas

### Eventos

| Método | Rota                                        | Descrição                             |
|--------|-----------------------------------------------|----------------------------------------|
| POST   | /eventos                                       | Cadastra um evento                     |
| GET    | /eventos                                       | Lista os eventos cadastrados           |
| GET    | /eventos/{id}                                  | Consulta um evento específico          |
| PUT    | /eventos/{id}                                  | Atualiza um evento existente           |
| DELETE | /eventos/{id}                                  | Remove um evento existente             |
| POST   | /eventos/{evento_id}/inscricoes/{participante_id} | Inscreve um participante em um evento |
| GET    | /eventos/{evento_id}/inscricoes                | Lista os participantes inscritos       |

### Participantes

| Método | Rota                    | Descrição                            |
|--------|--------------------------|----------------------------------------|
| POST   | /participantes           | Cadastra um participante              |
| GET    | /participantes           | Lista os participantes cadastrados    |
| GET    | /participantes/{id}      | Consulta um participante específico   |
| PUT    | /participantes/{id}      | Atualiza um participante existente    |
| DELETE | /participantes/{id}      | Remove um participante existente      |

## Exemplos de uso

### Cadastrar um evento

`POST /eventos`

```json
{
  "titulo": "Semana de Tecnologia",
  "descricao": "Evento sobre inovação e novas tecnologias",
  "data": "2026-11-10",
  "horario": "19:00:00",
  "local": "Auditório 1",
  "capacidade": 50,
  "categoria": "Palestra"
}
```

Resposta (201 Created):

```json
{
  "id": 1,
  "titulo": "Semana de Tecnologia",
  "descricao": "Evento sobre inovação e novas tecnologias",
  "data": "2026-11-10",
  "horario": "19:00:00",
  "local": "Auditório 1",
  "capacidade": 50,
  "categoria": "Palestra"
}
```

### Cadastrar um participante

`POST /participantes`

```json
{
  "nome": "Ana Souza",
  "email": "ana@exemplo.com",
  "curso": "Engenharia de Software"
}
```

### Inscrever um participante em um evento

`POST /eventos/1/inscricoes/1`

Resposta (201 Created):

```json
{
  "evento_id": 1,
  "participante_id": 1
}
```

### Exemplos de erro

Evento não encontrado (404):

```json
{
  "detail": "Evento não encontrado."
}
```

Participante já inscrito no evento (400):

```json
{
  "detail": "Participante já está inscrito neste evento."
}
```

Evento sem vagas disponíveis (400):

```json
{
  "detail": "Não existem vagas disponíveis para este evento."
}
```

Dados inválidos, como título vazio ou e-mail em formato incorreto (422):

```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "titulo"],
      "msg": "String should have at least 1 character"
    }
  ]
}
```

## Repositório

Link do repositório no GitHub: https://github.com/Joaosassaki/backend
