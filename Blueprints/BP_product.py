from flask import Blueprint, render_template, request
from data.add_product import ProductsForm
from os import path
from werkzeug.utils import secure_filename
from data.db_session import *
from data.product import Products
from data.users import User
from main import app

blueprint = Blueprint(
    'product',
    __name__,
    template_folder='templates'
)


@blueprint.route('/product/<id_p>')
def render_product(id_p):
    db_sess = create_session()
    product = db_sess.query(Products).filter(Products.id == id_p).first()
    return render_template('')
