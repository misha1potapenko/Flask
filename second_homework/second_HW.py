from flask import Flask, request, render_template, make_response, redirect

app = Flask(__name__)


# Задание
#
# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя,
# а также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти»,
# при нажатии на которую будет удалён cookie-файл
# с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['POST'])
def login():
    name = request.form['name']
    email = request.form['email']
    response = make_response(redirect('/user_hi'))
    response.set_cookie('user_name', name)
    response.set_cookie('user_email', email)
    return response


@app.route('/user_hi/')
def user_hi():
    user_name = request.cookies.get('user_name')
    if user_name:
        return render_template('user_hi.html', name='user_name')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
