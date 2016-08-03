from flask.ext.wtf import Form 
from wtforms import StringField, TextField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from app import User

class LoginForm(Form):
	email = StringField('Email', validators=[Required(), Length(1,64), Email()])
	Password = PasswordField('Password', validators=[Required()])
	Submit = SubmitField('Log in')

class Registration(Form):
	email = StringField('Email', validators=[Required(), Length(1,64), Email()])
	username = StringFiel('username', validators=[Required(), Length(1,64)])
	password = PasswordField('password', validators=[Required(), EqualTo('password2')])
	password2 = PasswordField('Confirm Password', validators=[Required()])
	submit = SubmitField('Register')

	def validate(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already exists')

	def validate_username(self, field):
		if User.query.filter_by(username=username).first():
			raise ValidationError('Username already exists')


