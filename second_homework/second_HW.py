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

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.files.get('name')
        email = request.files.get('email')
        responce = make_response(redirect('/greet/'))
        responce.set_cookie('user_name', name)
        responce.set_cookie('user_email', email)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
