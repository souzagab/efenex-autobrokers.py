"""
  'App'
  Centralizando as camadas de maneira estruturada
"""
from src.middleware.auth import user_logged_in
from src.views import login, register

def init():
    try:
        print("Bem vindo a Efenex Autobrokers\n")

        while not user_logged_in():
            user_register_input = input("Para continuar, é necessário login, já possui cadastro? (Sim/Não): ")
            user_registered = "S" in user_register_input

            if user_registered:
                login.run()
            else:
                register.run()


    except Exception as e:
        print("handle exception", e)

