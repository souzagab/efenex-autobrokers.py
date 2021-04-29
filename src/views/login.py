from src.controllers.sessions import sign_in
from src.views.forms.user_form import UserForm
from src.lib.utils import clear

def run():
    return login_prompt()


def login_prompt():
    print("======================")
    print("Logue-se")
    print("======================\n")

    user = UserForm()
    params = user.render()


    response = sign_in(params)

    # import code;
    # code.interact(local=dict(globals(), **locals()))

    if response["status"] == 200:
        print(response["message"]) # "alert"
    else:
        clear()

        print("Ocorreu um Erro! \n")
        print(response["body"])

        user_register_input = input("Deseja se cadastrar? (Sim/Não): ")
        user_sign_up = "s" in user_register_input

        if user_sign_up:
            clear()
            redirect_to_sign_up()


def redirect_to_sign_up():
    from src.views.register import run
    return run()