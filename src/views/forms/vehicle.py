from src.views.forms.form import FormBase

class VehicleForm(FormBase):
    questions = [
        {
            'type': "input",
            "name": "name",
            "message": "Nome:"
        },
        {
            'type': "input",
            "name": "model",
            "message": "Nome do Modelo:"
        },
        {
            'type': "input",
            "name": "plate",
            "message": "Placa:"
        },
        {
            'type': "list",
            "name": "type",
            "message": "Tipo:",
            'choices': ["SUV", "Utilitario"]
        },
        {
            'type': "list",
            "name": "fuel",
            "message": "Tipo de Combustivel:",
            'choices': ["Gasolina", "Alcool", "Flex"]
        },
        {
            'type': "input",
            "name": "year",
            "message": "Ano de fabricacao:"
        },
        {
            'type': "input",
            "name": "price",
            "message": "Preco:"
        }
    ]