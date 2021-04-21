from src.middleware.auth import user
from src.views.forms.menu import MenuForm

def run():
    return menu()

def menu():
    form = MenuForm()

    print("============================")
    print("============================")
    choice = form.render()
    print("============================")
    print("============================")

    return int(list(choice["option"])[0])
