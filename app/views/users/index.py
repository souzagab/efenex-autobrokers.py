from app.controllers.users import index as get_index
from lib.utils import clear


def run():
    render_index()


def render_index():
    users = get_index()
    clear()
    print("""
        ======================================
            LISTA DE USUARIOS CADASTRADOS
        ======================================
    \n\n
    """)
    for user in users:
        print(f"Usuario: { user.username }  | Cadastrado em: { user.created_at }")

    input("\n ..Aperte enter para voltar ao menu")