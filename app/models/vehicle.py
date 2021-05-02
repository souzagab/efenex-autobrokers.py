from peewee import *  # TODO: otimizar import

from app.models.model import BaseModel


class Vehicle(BaseModel):
    """ Classe que representa os veiculos """

    name = CharField()
    model = CharField()
    plate = CharField()
    type = CharField()
    fuel  = CharField()
    year = CharField()
    price = CharField()
