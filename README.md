<h1 align="center"> Efenex Auto-Brokers </h1>  
<p>  
</p>  
  
> Gerenciador de veiculos  
  
## Requerimentos / Setup  
- Python 3+  
- SQLite

  1. Instale os pacotes necessários
	`pip -r requirements.txt` 
	
## Utilização

1. Entre na pasta do projeto
2. Rode o arquivo `python main.py`
  
 ## Contexto
 O projeto se baseia em um programa para compra e venda de veículos, é autenticado , possibilitando o registro de novos usuários, e o cadastro de novos veículos.

## Funcionalidades
- **Gerenciamento de usuários**: 
	- Cadastro de novos usuários
	- Listar usuários cadastrados
	 
- **Gerenciamento de veículos**:
	- Cadastro de novos veículos
	- Listar todos veículos cadastrados
	- Exportar lista de veículos para um arquivo `.txt` 

## Futuras evoluções

 - [ ] Edição/Exclusão de veículos
 - [ ] Edição de usuários já cadastrados
 - [ ] Controle de vendas
 
## Estrutura

O projeto se estruturou baseando no padrão MVC, isolando comportamentos os comportamentos conforme o padrão, abaixo segue a representação em modo arvore, para facilitar a visualização.
    

    ├── app
    │   ├── app.py <- Central da aplicação
    │   ├── controllers 
    │   │   ├── sessions.py <- Controle de "sessões"
    │   │   ├── users.py <- Usuarios
    │   │   └── vehicles.py <- Veículos
    │   ├── middleware
    │   │   └── auth.py <- Módulo que controla se usuário está logado
    │   ├── models 
    │   │   ├── model.py <- Model base, isolando os comportamentos em comum
    │   │   ├── user.py <- Model representando o Usuário
    │   │   └── vehicle.py <- Model representando o Veículo
    │   └── views
    │       ├── forms <- "Componentes" que renderizam os formulários
    │       │   ├── form.py <- "Componente" Base
    │       │   ├── menu.py
    │       │   ├── user_form.py
    │       │   └── vehicle.py
    │       ├── helpers
    │       │   └── utils.py <- Isolando comportamentos em comum para as "views"
    │       ├── login.py <- "View" de login
    │       ├── menu.py <- "View" do menu principal
    │       ├── register.py <- "View" de registro 
    │       ├── users
    │       │   └── index.py <- "View" de lista de usuários
    │       └── vehicles
    │           ├── index.py <- "View" de lista de veículos
    │           └── new.py <- "View" do formulário de um novo veículo
    ├── bin
    │   └── setup.py <- "Setup" ( Cria tabelas, etc)
    ├── efenex.db
    ├── lib
    │   ├── settings.py <- Isola configurações
    │   └── utils.py <- Isola comportamentos da aplicação
    ├── main.py <- Main
    ├── requirements.txt 
    └── setup.py
