from src.views.forms.form import FormBase


class UserForm(FormBase):
    questions = [
        {
            'type': "input",
            "name": "username",
            "message": "Username:"
        },
        {
            'type': "password",
            "name": "password",
            "message": "Password:"
        }
    ]
