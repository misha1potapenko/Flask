
from flask import Flask, render_template, request, url_for, flash, make_response, redirect
from flask_wtf import CSRFProtect

from models import db, User
from logging import getLogger as Logger
from registration_form import RegistrationForm

app = Flask(__name__)
logger = Logger(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.get('/')
def home():
    context = {'users': User.query.all()}
    return render_template('home.html', **context)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User(
            # Обработка данных из формы
            full_name=form.full_name.data,
            email=form.email.data,
            password=form.password.data,
        )
        user.set_password(user.password)
        db.session.add(user)
        db.session.commit()
        response = make_response(redirect(url_for('home')))
        flash('SignUp was successfully!', 'success')
        return response
    else:
        return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)