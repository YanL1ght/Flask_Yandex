from flask import Flask, render_template, request, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key_for_web_prodject'


@app.route('/home')
def home():
    return render_template('/html_files/main.html')


@app.route('/search')
def search():
    search_words = request.args.get('q')
    print(search_words)
    return render_template('/html_files/search.html')


@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')

    return '''<h1>The language value is: {}</h1>'''.format(language)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
