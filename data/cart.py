import sqlalchemy
from data import db_session


class Cart(db_session.SqlAlchemyBase):
    __tablename__ = 'cart'

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), primary_key=True)
    products = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    users = sqlalchemy.orm.relationship('User')
