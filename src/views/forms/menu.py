from src.views.forms.form import FormBase


class MenuForm(FormBase):
    questions = [
        {
            'type': 'list',
            'name': 'option',
            'message': 'Escolha uma funcionalidade: ',
            'choices': [
                "1. Listar veículos",
                "2. Cadastrar um novo veículo",
                "3. Logout"
            ]
        }
    ]