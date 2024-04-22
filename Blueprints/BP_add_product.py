from flask import Blueprint, render_template, request, redirect
from data.add_product import ProductsForm
from os import path
from flask_login import current_user
from werkzeug.utils import secure_filename
from data.db_session import *
from data.product import Products
from data.users import User
from server import app

blueprint = Blueprint(
    'add_product',
    __name__,
    template_folder='templates'
)

UPLOAD_FOLDER = "static/img/product's_image"
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'webp']
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@blueprint.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if current_user.is_authenticated:
        form = ProductsForm()
        if form.submit.data:
            db_sess = create_session()
            user_id = db_sess.query(User.id).filter(User.name == request.cookies.get('User')).first()[0]
            files = request.files.getlist("file")
            if len(files) > 5:
                return render_template('html_files/add_product.html', form=form,
                                       message='Количество файлов не должно быть больше 5-ти')
            elif len(files) < 2:
                return render_template('html_files/add_product.html', form=form,
                                       message='Количество файлов должно быть минимум 2')
            else:
                filenames = []
                for file in files:
                    if file and allowed_file(file.filename):
                        filename = '_'.join(secure_filename(file.filename).split())
                        data = '_'.join(form.title.data.split())
                        save_filename = f"{data}_by_{user_id}_{filename}"
                        filenames.append(save_filename)
                        file.save(path.join(app.config['UPLOAD_FOLDER'], save_filename))
            product = Products(
                title=form.title.data,
                description=form.description.data,
                prise=form.prise.data,
                files=str(':'.join(filenames)),
                user_id=user_id
            )
            db_sess.add(product)
            db_sess.commit()
        return render_template('html_files/add_product.html', form=form)
    else:
        return redirect('/login')
