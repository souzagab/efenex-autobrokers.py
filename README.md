<h1 align="center"> Efenex Auto-Brokers </h1>  
<p>  
</p>  
  
> Gerenciador de veiculos  
  
## Requerimentos / Setup  
- Python 3+  
  
`pip3 -r requirements.txt`  
  
 ## Contexto
 - Funcionalidades
 
### Estrutura

    

    ├── app
    │   ├── app.py
    │   ├── controllers
    │   │   ├── sessions.py
    │   │   ├── users.py
    │   │   └── vehicles.py
    │   ├── middleware
    │   │   └── auth.py
    │   ├── models
    │   │   ├── model.py
    │   │   ├── user.py
    │   │   └── vehicle.py
    │   └── views
    │       ├── forms
    │       │   ├── form.py
    │       │   ├── menu.py
    │       │   ├── user_form.py
    │       │   └── vehicle.py
    │       ├── helpers
    │       │   └── utils.py
    │       ├── login.py
    │       ├── menu.py
    │       ├── register.py
    │       ├── users
    │       │   └── index.py
    │       └── vehicles
    │           ├── index.py
    │           └── new.py
    ├── bin
    │   └── setup.py
    ├── efenex.db
    ├── lib
    │   ├── settings.py
    │   └── utils.py
    ├── main.py
    ├── requirements.txt
    └── setup.py
