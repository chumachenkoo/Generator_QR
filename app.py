from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qr.db'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from views import *

app.add_url_rule('/account', 'user_account', account.user_account)
app.add_url_rule('/login', 'get_login', authentication.get_login, methods=['GET'])
app.add_url_rule('/login', 'post_login', authentication.post_login, methods=['POST'])
app.add_url_rule('/', 'get_login', authentication.get_login, methods=['GET'])
app.add_url_rule('/', 'post_login', authentication.post_login, methods=['POST'])
app.add_url_rule('/logout', 'logout', authentication.logout)
app.add_url_rule('/registration', 'get_registration', registration.get_registration, methods=['GET'])
app.add_url_rule('/registration', 'post_registration', registration.post_registration, methods=['POST'])
app.add_url_rule('/generator', 'generator', generator.qr_generator, methods=['GET', 'POST'])