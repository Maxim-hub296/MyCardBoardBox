from flask import render_template, redirect, request, url_for
from flask_login import current_user, login_user, login_required
from app import app
from app.forms import LoginForm, AddQuotForm
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
def quotes():

    return render_template("quotes.html", title_name="Цитаты",quotes=Quotes.select())

@app.route("/add_quot", methods=['GET', 'POST'])
@login_required
def add_quotes():
    form = AddQuotForm()
    if form.validate_on_submit():
        text, author = form.quot.data, form.author.data
        Quotes.get_or_create(quot=text, author=author)
        return redirect('/quotes')
    return render_template('add_quot.html', title_name="добавление цитаты",form=form)

@app.route('/contact')
def contact():
    return render_template('contact.html', title_name='Обратная связь')
