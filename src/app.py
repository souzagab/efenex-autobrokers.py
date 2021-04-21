"""
  'App'
  Centralizando as camadas de maneira estruturada
"""
from src.middleware.auth import user_logged_in, logout
from src.lib.utils import *
from src.views import login, register, menu
from src.views.helpers.utils import logo_text

def init():
    try:
        while True:
            while not user_logged_in():
                clear()
                print(logo_text("Efenex AutoBrokers"))
                print("\n\n")
                user_register_input = input("Para continuar, é necessário login, já possui cadastro? (Sim/Não): ")
                user_registered = "S" in user_register_input

                if user_registered:
                    clear()
                    login.run()
                else:
                    clear()
                    register.run()
            clear()
            menu_option = menu.run()

            if menu_option is 1:
                print("renderiza funcao 1")
                pass
            elif menu_option is 2:
                from src.views.vehicles.new import run as vehicles_new

                vehicles_new()
            elif menu_option is 3:
                logout()



    except Exception as e:
        print("handle exception", e)

