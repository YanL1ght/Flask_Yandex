from flask import render_template, request, Blueprint

blueprint = Blueprint(
    'catalog',
    __name__,
    template_folder='templates'
)


@blueprint.route('/catalog', methods=["GET", 'POST'])
def search():
    search_words = request.args
    print(search_words)
    lst = [f'{i} p' for i in range(10)]
    return render_template('/html_files/catalog.html', items=lst)
