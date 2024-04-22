from flask import Blueprint, render_template, redirect
from data.login_form import RegistForm
from data.db_session import *
from data.users import User
from data.cart import Cart
from flask_login import login_user

blueprint = Blueprint(
    'registration',
    __name__,
    template_folder='templates'
)


@blueprint.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegistForm()
    if form.validate_on_submit():
        db_sess = create_session()
        user_name = db_sess.query(User).filter(User.name == form.name.data).first()
        if not user_name:
            user = db_sess.query(User).filter(User.email == form.email.data).first()
            if not user:
                password = form.password.data
                if len(password) >= 8:
                    if password == form.password2.data:
                        red = redirect("/")

                        new_user = User()
                        new_user.name = form.name.data
                        new_user.email = form.email.data
                        new_user.set_password(password)

                        db_sess.add(new_user)
                        db_sess.commit()

                        cart = Cart()
                        cart.user_id = db_sess.query(User.id).filter(User.name == new_user.name).first()[0]
                        cart.products = ''
                        db_sess.add(cart)
                        db_sess.commit()

                        login_user(new_user, remember=form.remember_me.data)

                        return red
                    return render_template('html_files/registration.html',
                                           message="Пароли не совпадают",
                                           form=form)
                return render_template('html_files/registration.html',
                                       message="В пароле должно быть не менее 8 символов",
                                       form=form)
            return render_template('html_files/registration.html',
                                   message="Данный логин занят другим пользователем",
                                   form=form)
        return render_template('html_files/registration.html',
                               message="Данное имя занято другим пользователем",
                               form=form)
    return render_template('/html_files/registration.html', form=form)
