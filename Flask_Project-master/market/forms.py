from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Такой Логин уже существует')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email уже существует!')

    username = StringField(label='Логин:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Пароль:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Подтвердите Пароль:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Создать Аккаунт')


class LoginForm(FlaskForm):
    username = StringField(label='Логин:', validators=[DataRequired()])
    password = PasswordField(label='Пароль:', validators=[DataRequired()])
    submit = SubmitField(label='Войти')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Купить Вещь!')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Продать Вещь!')
