from peewee import CharField

from database import BaseModel

class Livro(BaseModel):
    titulo = CharField()
    autor = CharField()
    ano = CharField()

    class Meta:
        db_table = 'livro'