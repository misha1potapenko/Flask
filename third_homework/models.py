# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля
# "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f'User({self.full_name}, {self.email})'
