from flask import Blueprint, render_template, request
from data.add_product import ProductsForm
from os import path
from werkzeug.utils import secure_filename
from data.db_session import *
from data.product import Products
from data.users import User
from main import app

blueprint = Blueprint(
    'add_product',
    __name__,
    template_folder='templates'
)

UPLOAD_FOLDER = "db/product's image"
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@blueprint.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductsForm()
    if form.submit.data:
        db_sess = create_session()
        user_id = db_sess.query(User.id).filter(User.name == request.cookies.get('User')).first()[0]
        files = request.files
        filenames = []
        for index in range(1, 3):
            file = files[f'file{index}']
            print(index)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filenames.append(f"{form.title.data}_by_{user_id}_{filename}")
                file.save(path.join(app.config['UPLOAD_FOLDER'], f"{form.title.data}_by_{user_id}_{filename}"))
        product = Products()
        product.title = form.title.data
        product.description = form.description.data
        product.prise = form.prise.data
        product.files = str(':'.join([f for f in filenames]))
        product.user_id = user_id
        db_sess.add(product)
        db_sess.commit()
    return render_template('html_files/add_product.html', form=form)
