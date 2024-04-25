import sqlalchemy
from data import db_session


class Products(db_session.SqlAlchemyBase):
    __tablename__ = 'products'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))  # id с привязкой к таблице users
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # название
    prise = sqlalchemy.Column(sqlalchemy.Integer)  # цена
    description = sqlalchemy.Column(sqlalchemy.String)  # описание
    files = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)  # файлы/фото
    users = sqlalchemy.orm.relationship('User')
