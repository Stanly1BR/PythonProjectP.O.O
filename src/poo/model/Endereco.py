from peewee import CharField

from database import BaseModel

class Endereco(BaseModel):
    cep = CharField()
    numero = CharField()

    class Meta:
        db_table = 'endereco'