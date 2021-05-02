from app.models.vehicle import Vehicle


def index():
    vehicles = Vehicle.select()
    return vehicles

def create(params):
    vehicle = Vehicle(**params)

    if vehicle.save():
        return dict(status=201, body=vehicle, message="Veiculo Registrado!")
    else:
        return dict(status=422, body=vehicle)


def export():
    vehicles = Vehicle.select()
    with open("vehicles.txt", "w") as file:
        for vehicle in vehicles:
            file.write(f""""
                ---------------------------------
                    Nome: { vehicle.name }
                    Modelo: { vehicle.model }
                    Tipo: { vehicle.type }
                    Combustivel: { vehicle.fuel }
                    Ano: { vehicle.year }
                    
                    R$ { vehicle.price }
                ---------------------------------
                """)
