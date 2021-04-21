from src.models.model import BaseModel
from peewee import * # TODO: otimizar import
from src.middleware.auth import user
class Vehicle(BaseModel):
    """ Classe que representa os veiculos """

    name = CharField()
    model = CharField()
    plate = CharField()
    type = CharField()
    fuel  = CharField()
    year = CharField()
    price = CharField()
