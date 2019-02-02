from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from app import db
from app.rad_db import User

class LoginForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    submit = SubmitField('Ваша лодка уже готова')

class MainForm(FlaskForm):
    subject = SelectField("Кто совершил действие?")
    action = StringField("Что было совершено?", validators=[DataRequired()])
    submit = SubmitField('Рассказать Радаманту')

    def __init__(self, *args, **kwargs):
        super(MainForm, self).__init__(*args, **kwargs)
        self.subject.choices = list(map(lambda f: (f.id, f.name + " " +f.surname), User.query.all()))