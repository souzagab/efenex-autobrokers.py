from src.lib.settings import db
from src.models.user import User

def init():
 db.connect()
 db.create_tables([User])