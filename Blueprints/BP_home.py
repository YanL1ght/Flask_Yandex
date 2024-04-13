from flask import Blueprint, request, render_template
from simply_functions import cookie_op

blueprint = Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/', methods=["GET", 'POST'])
def home():
    visible_name, link = cookie_op()
    if request.method == 'GET':
        return render_template('/html_files/main.html', name=visible_name, link=link)
    elif request.method == 'POST':
        print(request.form['a_catalog'])
        print(request.form['a_catalog'])
