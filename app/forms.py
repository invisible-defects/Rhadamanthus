from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    submit = SubmitField('Ваша лодка уже готова')