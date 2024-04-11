import sqlalchemy
from data import db_session
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db_session.SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return '<User {}, email {}, password {}, xz {}>'.format(
            self.name, self.email, generate_password_hash(self.hashed_password), check_password_hash(self.hashed_password, self.hashed_password))
