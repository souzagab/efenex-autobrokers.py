from peewee import *

from app.models.model import BaseModel


class User(BaseModel):
    """ Classe que representa os usuarios """
    username = CharField(unique=True)
    password = CharField()
