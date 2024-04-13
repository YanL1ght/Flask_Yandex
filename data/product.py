import sqlalchemy
from data import db_session


class Products(db_session.SqlAlchemyBase):
    __tablename__ = 'products'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    prise = sqlalchemy.Column(sqlalchemy.Integer)
    description = sqlalchemy.Column(sqlalchemy.String)
    files = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    users = sqlalchemy.orm.relationship('User')
