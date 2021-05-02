from app.models.user import User
from app.models.vehicle import Vehicle
from lib.settings import db


def init():
 db.connect()
 db.create_tables([User, Vehicle])