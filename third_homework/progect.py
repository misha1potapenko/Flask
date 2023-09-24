from flask import Flask, render_template
from models import db, User
from logging import getLogger as Logger

app = Flask(__name__)
logger = Logger(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.get('/')
def home():
    context = {'users': User.query.all()}
    return render_template('home.html', **context)

    