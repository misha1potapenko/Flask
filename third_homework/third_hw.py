# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля
# "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
import flask_sqlalchemy as SQLAlchemy
from flask import Flask, request, render_template, make_response, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy()


if __name__ == '__main__':
    app.run(debug=True)
    