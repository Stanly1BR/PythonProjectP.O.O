from peewee import CharField, ForeignKeyField

from database import BaseModel
from src.poo.model.Endereco import Endereco


class Usuario(BaseModel):
    nome = CharField()
    email = CharField()
    senha = CharField()
    endereco = ForeignKeyField(Endereco, backref='usuario')

    class Meta:
        db_table = 'usuario'