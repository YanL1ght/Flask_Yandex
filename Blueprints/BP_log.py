from flask import render_template, redirect, Blueprint
from data.login_form import LoginForm
from data.users import User
from data.db_session import *
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, logout_user


blueprint = Blueprint(
    'log',
    __name__,
    template_folder='templates'
)


@blueprint.route('/login', methods=['GET', 'POST'])  # вход
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and check_password_hash(user.hashed_password, form.password.data):
            red = redirect("/")
            login_user(user, remember=form.remember_me.data)
            return red
        return render_template('html_files/login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('html_files/login.html', title='Авторизация', form=form)


@blueprint.route('/logout')
@login_required
def logout():  # выход
    redi = redirect("/")
    logout_user()
    return redi
