from flask import request


def cookie_op():
    user_acc = request.cookies.get('User')
    visible_name = 'Вход'
    link = '/login'
    if user_acc:
        visible_name = user_acc
        link = ''
    return visible_name, link
