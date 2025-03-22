from flask import Flask
from app.views import AboutView

app = Flask(__name__)

app.add_url_rule("/", view_func=AboutView.as_view("about"))