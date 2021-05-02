
from app.controllers.vehicles import *
from app.views.forms.vehicle import VehicleForm


def run():
    return vehicle_form()

def vehicle_form():
    print("======================")
    print(" Novo Veiculo")
    print("======================\n")
    form = VehicleForm()
    params = form.render()

    response = create(params)

    if response["status"] == 200:
        print(response["message"])
    else:
        print("Erro")
        print(response["body"])
