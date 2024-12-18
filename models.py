from peewee import *

database = PostgresqlDatabase('postgresql://postgres:1234@localhost:5432/postgres')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Users(BaseModel):
    age = SmallIntegerField(null=True)
    first_name = UnknownField(null=True)  # ARRAY
    last_name = UnknownField(null=True)  # ARRAY
    tg_id = BigIntegerField()
    username = UnknownField(null=True)  # ARRAY

    class Meta:
        table_name = 'Users'
        primary_key = False

