from src.middleware.auth import user
from src.views.forms.menu import MenuForm

def run():
    return menu()

def menu():
    form = MenuForm()

    print("============================")
    # print(f"|     {user.username}     |")
    print("============================")
    choice = form.render()


    return int(list(choice["option"])[0])
