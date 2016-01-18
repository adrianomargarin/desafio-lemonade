# desafio-lemonade

# Setup

```
git clone https://github.com/adrianomargarin/desafio-lemonade.git
cd desafio-lemonade
virtualenv env
source env/bin/activate
pip install -r deploy/requirements.txt
cd ~/path/to/project/src
./manage.py migrate
```

# Testes

```
cd ~/path/to/project/src
REUSE_DB=1 coverage run --source='.' ./manage.py test ; coverage report --show-missing
```

# Server

```
./manage.py runserver 8000
```

Acessar  ```http://127.0.0.1:8000```

# Cadastro de cliente

```
http://127.0.0.1:8000/clientes/registro/
````

# Login

```
http://127.0.0.1:8000/login
```

# Admin

```
http://127.0.0.1:8000/admin
```

Usuário: ```admin```
Senha: ```admin```

# APIs Cliente

## Content Type 

```
application/json
```

## Autenticação 

```
from base64 import b64encode
user_pass = b64encode(username + ':' + 'senha').decode('ascii')
'Basic %s' % user_pass
```

Registro de cliente (Sem autenticação)
======================================

Endpoint
********

```
POST /api/v1/cliente
```

Exemplo
*******

```
{    
    "first_name": "Adriano",
    "last_name": "Margarin",
    "username": "adrianomargarin",
    "email": "adriano.margarin@gmail.com",
    "cpf": "01078740089",
    "cnh_type": ["A", "B"],
    "password": "123456"
}
```

Edição completa de um cliente (Com autenticação)
================================================

Endpoint 
********

```
PUT /api/v1/cliente/:id-customer
```

Exemplo
*******

```
{    
    "first_name": "Novo",
    "last_name": "Nome",
    "username": "adrianomargarin",
    "email": "adriano.margarin@gmail.com",
    "cpf": "01078740089",
    "cnh_type": ["A", "B"],
    "password": "123456"
}
```

Edição parcial de um cliente (Com autenticação)
===============================================

Endpoint 
********

```
PATCH /api/v1/cliente/:id-customer
```

Exemplo
*******

```
{    
    "first_name": "Novo",
    "last_name": "Nome"
}
```

Consultar dados de um cliente (Com autenticação)
================================================

Endpoint 
********

```
GET /api/v1/cliente/:id-customer
```

Resposta
********

```
{
    "id": 2,
    "first_name": "Adriano",
    "last_name": "Margarin",
    "username": "adrianomargarin",
    "email": "adriano.margarin@gmail.com",
    "cpf": "01078740089",
    "cnh_type": ["A","C"]
}
```

Excluir um cliente (Com autenticação)
=====================================

Endpoint
********

```
DELETE /api/v1/cliente/:id-customer
```

Resposta
********

```
{
    "detail":"Cliente excluído com sucesso."
}
```

# APIs Admin

Cadastrar veículo na frota (Com autenticação)
=============================================

Endpoint
********

```
POST /api/v1/frota
```

Exemplo
*******

```
{
    "vehicle_name": "Gol",
    "category": "car",
    "description": "Gol 1.0"
}
```

Editação completa de um veículo da frota (Com autenticação)
===========================================================

Endpoint
********

```
PUT /api/v1/frota/:id-vehicle
```

Exemplo
*******

```
{
    "vehicle_name": "Gol",
    "category": "car",
    "description": "Gol 2.0"
}
```

Editação parcial de um veículo da frota (Com autenticação)
==========================================================

Endpoint
********

```
PATCH /api/v1/frota/:id-vehicle
```

Exemplo
*******

```
{
    "description": "Gol 3.0"
}
```

Consultar um veículo da frota (Com autenticação)
================================================

Endpoint
********

```
GET /api/v1/frota/:id-vehicle
```

Resposta
********

```
{
    "category": "Carro",
    "description": "Gol 3.0",
    "id": 1,
    "is_rented": false,
    "vehicle_name": "Gol"
}
```

Excluir um veículo da frota (Com autenticação)
==============================================

Endpoint
********

```
DELETE /api/v1/frota/:id-vehicle
```

Resposta
********

```
{
    "detail": "Veículo excluído com sucesso."
}
```

