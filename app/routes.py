from flask import render_template, redirect, request, url_for
from flask_login import current_user, login_user, login_required
from urllib.parse import urlsplit
from app import app
from app.forms import LoginForm
from app.database import Quotes
from app.user import User
@app.route("/")
def about():
    return render_template("about.html", title_name="О нас")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')

    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == "1234":
            user = User(id=1)
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('/'))

    return render_template('login.html', title_name="Кто это пытается дополнить мой сайт?", form=form)


@app.route("/quotes")
@login_required
def quotes():

    return render_template("quotes.html", title_name="Цитаты",quotes=Quotes.select())