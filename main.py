from flask import Flask, render_template, request, redirect, make_response
from flask_login import LoginManager, login_user, login_required, logout_user
from data.db_session import *
from data.users import User
from data.login_form import LoginForm, RegistForm
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key_for_web_prodject'

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/', methods=["GET", 'POST'])
def home():
    user_acc = request.cookies.get('User')
    visible_name = 'Вход'
    link = '/login'
    print(user_acc)
    if user_acc:
        visible_name = user_acc
        link = ''

    if request.method == 'GET':
        return render_template('/html_files/main.html', name=visible_name, link=link)
    elif request.method == 'POST':
        print(request.form['a_catalog'])
        print(request.form['a_catalog'])


@app.route('/catalog', methods=["GET", 'POST'])
def search():
    search_words = request.args
    print(search_words)
    lst = [f'{i} p' for i in range(10)]
    return render_template('/html_files/catalog.html', items=lst)


@login_manager.user_loader
def load_user(user_id):
    db_sess = create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and check_password_hash(user.hashed_password, form.password.data):
            red = redirect("/")
            login_user(user, remember=form.remember_me.data)
            red.set_cookie('User', str(user.name), max_age=60 * 60 * 24 * 30)
            return red
        return render_template('html_files/login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('html_files/login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    redi = redirect("/")
    redi.set_cookie('User', '', max_age=0)
    logout_user()
    return redi


@app.route("/registration", methods=['GET', 'POST'])
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

                        login_user(new_user, remember=form.remember_me.data)

                        db_sess.add(new_user)
                        db_sess.commit()

                        red.set_cookie('User', str(form.name.data), max_age=60 * 60 * 24 * 30)

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


@app.route('/add_product')
def add_product():
    return ''


if __name__ == '__main__':
    global_init('db/users.sqlite')
    app.run(port=8080, host='127.0.0.1')
