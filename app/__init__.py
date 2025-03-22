from secrets import token_hex
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Для доступа требуется авторизация"
login_manager.login_message_category = "warning"
app.secret_key = token_hex(32)

from app import routes
