from flask import Flask
from flask_login import LoginManager
from data.db_session import *
from data.users import User
from Blueprints import BP_home, BP_log, BP_registration, BP_catalog, BP_add_product, BP_product, BP_cart

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key_for_web_prodject'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = create_session()
    return db_sess.query(User).get(user_id)


if __name__ == '__main__':
    global_init('db/database.sqlite')

    app.register_blueprint(BP_home.blueprint)
    app.register_blueprint(BP_log.blueprint)
    app.register_blueprint(BP_registration.blueprint)
    app.register_blueprint(BP_catalog.blueprint)
    app.register_blueprint(BP_add_product.blueprint)
    app.register_blueprint(BP_product.blueprint)
    app.register_blueprint(BP_cart.blueprint)

    app.run(port=8080, host='127.0.0.1')
