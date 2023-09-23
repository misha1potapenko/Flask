# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.
from pathlib import PurePath, Path
import logging

from flask import Flask, request, abort, redirect, url_for, flash

from flask import render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def html_index():
    return render_template('index.html')

@app.route('/hello_world/')
def hello():
    return f'Hello friend'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('download.html')


# Задание №3
# Создать страницу, на которой будет форма для ввода логина
# и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.
user = {
    "login": "Ivan",
    "password": "123"

}

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == user["login"] and password == user["password"]:
            return f"Привет {login}"
    return render_template('user_hi.html')


# Задание №4
# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

@app.route('/length/', methods=['GET', 'POST'])
def length():
    if request.method == 'POST':
        text = request.form.get('text')
        length_text = len(text.split())
        return f"{length_text}"
    return render_template('length.html')

# Задание №5
# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

@app.route('/calc/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        oper = request.form.get('operation')
        if oper == "add":
            return f"{num1 + num2}"
        if oper == "subtract":
            return f"{num1 - num2}"
        if oper == "multiply":
            return f"{num1 * num2}"
        if oper == "divide" and num2 != 0:
            return f"{num1 / num2}"
    return render_template('calc.html')


# Задание №6
# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.



logger = logging.getLogger(__name__)


@app.errorhandler(403)
def page_not_found(e):
    logger.warning(e)
    context = {
    'title': 'Доступ запрещен',
    'url': request.base_url,
    }
    return render_template('403.html', **context), 403

@app.route('/send/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        age = int(request.form.get('age'))
        if age < 18:
            abort(403)
        return f"Привет, вы вошли в систему"
    return render_template('send.html')


# Задание №7
# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат


@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('html_index'))


# Задание №8
# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

