"""
  'App'
  Centralizando as camadas de maneira estruturada
"""
from app.middleware.auth import user_logged_in, logout
from app.views import login, register, menu
from app.views.helpers.utils import logo_text
from lib.utils import *


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
                clear()

                from app.views.vehicles.index import run as vehicles_index

                vehicles_index()

            elif menu_option is 2:
                clear()

                from app.views.vehicles.new import run as vehicles_new

                vehicles_new()

            elif menu_option is 3:
                clear()
                from app.views.users.index import run as users_index

                users_index()

            elif menu_option is 4:
                clear()

                from app.controllers.vehicles import export as export_vehicles

                export_vehicles()

                print("Abra vehicles.txt")

                input("\n Aperte enter pra continuar")
            elif menu_option is 5:
                logout()
                break



    except Exception as e:
        print("handle exception", e)

