import sqlalchemy
from data import db_session
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db_session.SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # имя
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)  # почта
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # захэшированный пароль

    product = sqlalchemy.orm.relationship("Products", back_populates='users')
    cart = sqlalchemy.orm.relationship("Cart", back_populates='users')

    def set_password(self, password):  # присвоить пароль, захэштровав его
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):  # проверить захэшированный пароль
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):  # для debug'а
        return '<User {}, email {}, password {}, xz {}>'.format(
            self.name, self.email, generate_password_hash(self.hashed_password), check_password_hash(
                self.hashed_password, self.hashed_password))
