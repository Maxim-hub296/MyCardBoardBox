from flask import render_template
from app import app

@app.route("/")
def about():
    return render_template("about.html", title_name="О нас")

