from flask import Blueprint, render_template

blueprint = Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/')
def home():
    return render_template('/html_files/main.html')
