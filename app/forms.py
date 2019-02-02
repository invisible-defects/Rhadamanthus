from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    submit = SubmitField('Ваша лодка уже готова')

class MainForm(FlaskForm):
    subject = SelectField("Кто совершил действие?", validators=[DataRequired()])
    action = StringField("Что было совершено?", validators=[DataRequired()])
    submit = SubmitField('Рассказать Радаманту')

    def __init__(self, *args, **kwargs):
        super(MainForm, self).__init__(*args, **kwargs)
        self.subject.choices = [("Я", "Я"), ("Артем", "Артем"), ("Даня", "Даня")]