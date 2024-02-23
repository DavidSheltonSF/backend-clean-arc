# Sobre:

Uma API de estudo para o CRUD de dados de Usuários e seus Pets.

**Arquitetura:** Clean Architecture

**Framework:** Flask

**Padrão de Json (não aplicado 100%):** JSON:API

**Tecnologias:**

- Python
- pytest (efetuar testes)
- black (formatador)
- flake8 (apontar problemas com a pep8)
- pylint (apontar problemas com a pep8)
- pre-commit (executar as 4 ferramentas anteriores antes de cada commit)
- Sqlite
- Sqlalchemy
- git e github
- jwt (autentificação)
- werkzeug (converter senhas hash)


Este é um projeto backend que estou desenvolvi a partir da playlist de Clean Architecture com Python do canal Programador Lhama.


## Sobre a Arquitetura

Eu codei esse projeto para aprender **Clean Architecture**.

Aprendi que esse tipo de arquitetura possui alguns benefícios:

- Testabilidade: Eu posso testar partes da aplicação separadamente, como repositories, use cases e controllers. Isso facilita para encontrar erros e garantir que cada uma das partes funciona.

- Flexibilidade e Adaptabilidade: Um sistema feito pela Clean Architecture, não está preso a um banco de dados, uma API, ou um framework específico.

## Rotas

### *api/users*

**POST:**

Corpo da Requisição:
```
{
    "user_name": "Marcos",
    "password": "marcos123"
}
```

SUCESSO:
```
{
  "data": {
    "Type": "users",
    "attributes": {
      "user_name": "Marcos"
    },
    "id": 1
  }
}
```

**PUT:**

Corpo da Requisição:
```
{   

    "user_name": "Marcos Pietro",
    "password": "marcos123"
}
```

SUCESSO:
```
{
  "data": {
    "Type": "users",
    "attributes": {
      "user_name": "Marcos Pietro"
    },
    "id": 1
  }
}
```

**GET:**

Query params:
```
user_id: 1
user_name: "Marcos Pietro
```

SUCESSO:
```
{
  "data": [
    {
      "attributes": {
        "user_name": "Marcos Pietro"
      },
      "id": 1,
      "type": "user"
    }
  ]
}
```

**DELETE:**

Corpo da Requisição:
```
{   
    "user_id": 1,
}
```

SUCESSO:
```
{
  "data": {
    "attributes": {
      "user_name": "Marcos Pietro"
    },
    "id": 1,
    "type": "user"
  }
}
```

### *api/pets*

**POST:**

Corpo da Requisição:
```
{
    "pet_name": "Duque",
    "specie": "DOG",
    "age":5,
    "user_information": {
        "user_id": 1
    }
}
```

SUCESSO:
```
{
  "data": {
    "Type": "pets",
    "attributes": {
      "age": 5,
      "pet_name": "Duque",
      "specie": "DOG"
    },
    "id": 1,
    "relationships": {
      "owner": {
        "id": 1,
        "type": "users"
      }
    }
  }
}
```

**PUT:**

Corpo da Requisição:
```
{
    "pet_id": 1,
    "pet_name": "Duque II",
    "specie": "DOG",
    "age":5,
    "user_information": {
        "user_id": 1
    }
}
```

SUCESSO:
```
{
  "data": {
    "attributes": {
      "age": 5,
      "pet_name": "Duque II",
      "specie": "DOG"
    },
    "id": 1,
    "relationships": {
      "user_id": 1
    },
    "type": "pet"
  }
}
```

**GET:**

Query params:
```
user_id: 1
```

*Também é possível procurar por pet_id ou pet_id e user_id*

SUCESSO:
```
{
  "data": [
    {
      "attributes": {
        "age": 5,
        "pet_name": "Duque II"
      },
      "id": 1,
      "relationships": {
        "user_id": 1
      },
      "type": "pet"
    },
    {
      "attributes": {
        "age": 3,
        "pet_name": "Mel"
      },
      "id": 2,
      "relationships": {
        "user_id": 1
      },
      "type": "pet"
    }
  ]
}
```

**DELETE:**

Corpo da Requisição:
```
{   
    "pet_id": 2,
}
```

SUCESSO:
```
{
  "data": {
    "attributes": {
      "age": 3,
      "pet_name": "Mel",
      "specie": "CAT"
    },
    "id": 2,
    "relationships": {
      "user_id": 1
    },
    "type": "pet"
  }
}
```

## Testes

A ferramenta que uso para testar os componentes do projeto é o **pytest**

*Testando so repositórios:*
```
pytest src/infra/repo
```
<img src="./readmeImgs/testingRepo.png">

## Outras ferramentas

Também estou utilizando o repositório **black** para formatar os meus códigos e o repositório **flake8** para me apontar algumas. Ambos visam alinhar o código de acordo com a pep8

Para aplicar os duas ferramentas anteriores eu utilizo o **pre-commit**, que realiza algumas tarefinhas antes de cada commit, como verificar se os requisitos do black, flake8 e pytest foram atendidos, e adicionar as dependências no requirements.txt

Além disso também estou utilizando o **pylint** que me passa algumas dicas de acordo com a pep8.
<img src="./readmeImgs/pylintError.png">
