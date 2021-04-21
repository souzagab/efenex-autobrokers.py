from src.controllers.sessions import sign_up

def run():
    return sign_up_prompt()

def sign_up_prompt():
    print("======================")
    print(" Registre-se ")
    print("======================")
    username = input("Username: ")
    password = input("Password: ")
    print("======================")

    try:
        response = sign_up(username, password)

        if response["status"] == 201:
            print("Logado") # redirect
        else:
            print("Ocorreu um erro")
    except Exception as e:
        print("Ocorreu um erro: " , e)