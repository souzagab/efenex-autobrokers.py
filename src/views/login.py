from src.controllers.sessions import sign_in


def run():
    return login_prompt()


def login_prompt():
    print("======================")
    print("Logue-se")
    print("======================")
    username = input("Username: ")
    password = input("Password: ")
    print("======================")

    response = sign_in(username, password)

    if response["status"] == 200:
        print(response["message"]) # "alert"
    else:
        print("Erro")
        print(response["body"])

        user_register_input = input("Deseja se cadastrar? (Sim/Não): ")
        user_sign_up = "s" in user_register_input

        if user_sign_up:
            redirect_to_sign_up()


def redirect_to_sign_up():
    from src.views.register import run
    return run()