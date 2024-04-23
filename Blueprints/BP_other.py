from flask import Blueprint, render_template


blueprint = Blueprint(
    'other',
    __name__,
    template_folder='templates'
)


@blueprint.route('/support')
def support():
    return render_template('html_files/base.html') + '''
            <br>
            <br>
            <br>
            <h2>У вас технические шоколадки?</h2>
            <h3>Обращайтесь на почту notsupport@uxodi.ti</h3>
    '''


@blueprint.route('/info')
def info():
    return render_template('html_files/base.html') + '''
        <br>
        <br>
        <br>
        <h2>Тут ничего нет</h2>
    '''