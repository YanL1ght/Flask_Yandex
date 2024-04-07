from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from data.db_session import *
from data.users import User
from data.login_form import LoginForm
from werkzeug.security import check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key_for_web_prodject'

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/', methods=["GET", 'POST'])
def home():
    if request.method == 'GET':
        return render_template('/html_files/main.html')
    elif request.method == 'POST':
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
        print(db_sess.query(User).filter(User.email == form.email.data).first())
        print(form.password.data)
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        print(check_password_hash(user.hashed_password, form.password.data))
        print()
        print(user.hashed_password)
        print(form.password.data)
        if user and check_password_hash(user.hashed_password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('html_files/login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('html_files/login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    global_init('db/users.sqlite')
    db_ses = create_session()
    userr = User()
    userr.name = 'User2'
    userr.email = 'emaill@email.com'
    userr.set_password('33333333')
    db_ses.add(userr)
    db_ses.commit()

    app.run(port=8080, host='127.0.0.1')
