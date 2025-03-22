import flask
from flask import render_template
from flask.views import MethodView


class AboutView(MethodView):
    """ Класс представления страницы "О нас" """
    def get(self):
        """ Метод обрабатывающий GET-запрос. Возвращает шаблон страницы about.html """
        return render_template('about.html', title_name="О сайте")