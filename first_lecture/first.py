from flask import Flask

from flask import render_template
app = Flask(__name__)


@app.route('/index/')
def html_index():
    return render_template('index.html')


@app.route('/index/index.html')
def html_index_html():
    return render_template('index.html')

@app.route('/index/for_man.html')
def html_index_man():
    return render_template('for_man.html')


@app.route('/index/for_woman.html')
def html_index_woman():
    return render_template('for_woman.html')

if __name__ == '__main__':
    app.run(debug=True)
