from app.controllers.sessions import sign_up
from app.views.forms.user_form import UserForm
def run():
    return sign_up_prompt()

def sign_up_prompt():
    print("======================")
    print(" Registre-se ")
    print("======================")
    user_form = UserForm()
    params = user_form.render()
    print("======================")

    try:
        response = sign_up(params)

        if response["status"] == 201:
            print("Logado") # redirect
        else:
            print("Ocorreu um erro")
    except Exception as e:
        print("Ocorreu um erro: " , e)