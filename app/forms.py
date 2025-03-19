from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class QuizForm(FlaskForm):
    title = StringField('Quiz Title', validators=[DataRequired(), Length(min=2)])
    submit = SubmitField('Create Quiz')

class QuestionForm(FlaskForm):
    question = StringField('Question Text', validators=[DataRequired(), Length(min=10)])
    options = TextAreaField('Options (comma-separated)', validators=[DataRequired()])
    correct_answer = StringField('Correct Answer', validators=[DataRequired()])
    submit = SubmitField('Add Question')
