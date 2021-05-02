import datetime

from peewee import *

db = SqliteDatabase("efenex.db")


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
