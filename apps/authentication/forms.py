# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, IntegerField
from wtforms.validators import Email, DataRequired

# login and registration


class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])

class CreatePostForm(FlaskForm):
    language = SelectField('Programming Language',
                            choices=[('C++'),('Python'),('HTML'),('CSS'),('Java'),('Javascript')],
                            id= 'language_create',
                            validators = [DataRequired()])
    contributers_wanted = IntegerField('Contributers Wanted',
                            validators = [DataRequired()])
    completion_percentage = IntegerField('Completion Percentage',
                            validators = [DataRequired()])
