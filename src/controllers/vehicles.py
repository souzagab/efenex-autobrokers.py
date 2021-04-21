from src.models.vehicle import Vehicle
import src.middleware.auth as auth

def create(params):
    vehicle = Vehicle(**params)

    if vehicle.save():
        return dict(status=201, body=vehicle, message="Veiculo Registrado!")
    else:
        return dict(status=422, body=vehicle)
