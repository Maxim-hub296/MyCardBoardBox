from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
@app.route("/")
def about():
    return render_template("about.html", title_name="О нас")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Пароль получен')
        print(form.password.data)
        return redirect('/')
    return render_template('login.html', title_name="Кто это пытается дополнить мой сайт?", form=form)