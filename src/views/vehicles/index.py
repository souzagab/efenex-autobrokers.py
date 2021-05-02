from src.lib.utils import clear
from src.controllers.vehicles import index


def run():
    render_index()


def render_index():
    clear()
    vehicles = index()
    print("""
    ==============================
        VEICULOS CADASTRADOS
    ==============================
    \n\n
    """)
    if len(vehicles) > 0:
        for vehicle in vehicles:
            print(vehicle_card(vehicle))

    else:
        print("Nao existem veiculos cadastrados")

    input("\n ..Aperte enter para voltar ao menu")


def vehicle_card(vehicle):
    return f""""
    ---------------------------------
        Nome: { vehicle.name }
        Modelo: { vehicle.model }
        Tipo: { vehicle.type }
        Combustivel: { vehicle.fuel }
        Ano: { vehicle.year }
        
        R$ { vehicle.price }
    ---------------------------------
    """