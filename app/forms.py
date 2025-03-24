from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class AddQuotForm(FlaskForm):
    quot = StringField('Введите текст цитаты', validators=[DataRequired()])
    author = StringField("Введите автора цитаты", validators=[DataRequired()])
    submit = SubmitField('Сохранить')

class AddCommentaryForm(FlaskForm):
    nickname = StringField('Введите ваше имя', validators=[DataRequired()])
    commentary = StringField('Введите ваш комментарий', validators=[DataRequired()])
    submit = SubmitField('Добавить')