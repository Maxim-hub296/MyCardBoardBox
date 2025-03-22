from secrets import token_hex

from flask import Flask

app = Flask(__name__)
app.secret_key = token_hex(32)

from app import routes
