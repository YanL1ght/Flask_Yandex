from flask import Blueprint, render_template, request, redirect
from data.db_session import *
from flask_login import current_user
from data.product import Products
from data.users import User
from data.cart import Cart

blueprint = Blueprint(
    'product',
    __name__,
    template_folder='templates'
)


@blueprint.route('/product/<id_p>', methods=['GET', 'POST'])
def render_product(id_p):
    db_sess = create_session()
    product = db_sess.query(Products).filter(Products.id == id_p).first()
    if request.method == 'GET':
        if not product:
            return 'такого нету'
        params = {  # словарь из параметров
            "title": product.title,
            'user': db_sess.query(User).filter(User.id == product.user_id).first().name,
            'price': product.prise,
            'description': product.description,
            'files': product.files.split(':')
        }
        return render_template('html_files/product.html', **params)

    if request.method == 'POST':
        if current_user.is_authenticated:
            cart = db_sess.query(Cart).get(current_user.id)
            if cart.products:
                cart.products = cart.products + ';' + str(product.id)
            else:
                cart.products = str(product.id)
            db_sess.add(cart)
            db_sess.commit()
            return redirect(f'/product/{id_p}')
        else:
            return redirect('/login')
