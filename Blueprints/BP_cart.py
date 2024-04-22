from flask import Blueprint, render_template, redirect
from data.db_session import *
from flask_login import current_user
from data.product import Products
from data.cart import Cart

blueprint = Blueprint(
    'cart',
    __name__,
    template_folder='templates'
)


@blueprint.route('/cart')
def cart():
    if current_user.is_authenticated:
        db_sess = create_session()
        data_cart = db_sess.query(Cart).get(current_user.id)
        data_prod = db_sess.query(Products).filter(Products.id.in_(data_cart.products.split(';')))
        lst = [{data_product: (len(data_product.title), len(data_product.description))} for data_product in data_prod]
        # создаётся список параметров(словарей), как-то так ¯\_(ツ)_/¯
        return render_template('html_files/cart.html', lst=lst)
    else:
        return redirect('/login')
