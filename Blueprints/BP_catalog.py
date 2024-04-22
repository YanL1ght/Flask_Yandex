from flask import render_template, request, Blueprint, redirect
from data.db_session import create_session
from data.product import Products


blueprint = Blueprint(
    'catalog',
    __name__,
    template_folder='templates'
)


@blueprint.route('/catalog', methods=["GET", 'POST'])
def search():
    if request.method == 'GET':
        search_words = request.args.get('q')
        db_sess = create_session()
        if not search_words:
            data = db_sess.query(Products).all()
        else:
            search_words = " ".join(search_words.split('+'))
            data = db_sess.query(Products).filter(Products.title.like(f'{search_words}')).all()
        lst = {i: (len(i.title), len(i.description)) for i in data}
        return render_template('/html_files/catalog.html', items=lst)

    if request.method == 'POST':
        return redirect(f'/catalog?q={"+".join(request.form["search_input"].split())}')

