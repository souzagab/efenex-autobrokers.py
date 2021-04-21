from src.lib.settings import db

from src.models.user import User
from src.models.vehicle import Vehicle

def init():
 db.connect()
 db.create_tables([User, Vehicle])