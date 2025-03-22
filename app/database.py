from peewee import SqliteDatabase, Model, CharField


db = SqliteDatabase('data')

class BaseModel(Model):

    class Meta:
        database = db


class Quotes(BaseModel):
    """Модель таблицы с цитатами"""
    quot = CharField(unique=True)
    author = CharField()

def create_tables():
    db.create_tables([Quotes])
