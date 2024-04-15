from flask import render_template, request, Blueprint
from data.db_session import create_session
from data.product import Products


blueprint = Blueprint(
    'catalog',
    __name__,
    template_folder='templates'
)


@blueprint.route('/catalog', methods=["GET", 'POST'])
def search():
    search_words = request.args.get('q')
    if not search_words:
        search_words = ''
    db_sess = create_session()
    data = db_sess.query(Products).filter(Products.title.like(f'%{search_words}%')).all()
    lst = {i: len(i.title) for i in data}
    return render_template('/html_files/catalog.html', items=lst)
