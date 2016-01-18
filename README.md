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

# APIs

## Content Type ```application/json```

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
PUT /api/v1/cliente
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
PATCH /api/v1/cliente
```

Exemplo
*******

```
{    
    "first_name": "Novo",
    "last_name": "Nome"
}
```
