from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, IntegerField,
                            SubmitField)
from wtforms.validators import DataRequired, equal_to, length
from flask_wtf.file import FileField
from wtforms import TextAreaField



class RegisterForm(FlaskForm):
    username = StringField("Enter Username", validators=[
        DataRequired()
    ])
    password = PasswordField("Enter Password", validators=[
        DataRequired(),
        length(min=6, max=24),
    ])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(),
        equal_to("password", message="პაროლები არ ემთხვევა")
    ])

    register = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField()
    password = PasswordField()

    login = SubmitField("Log In")

class BookForm(FlaskForm):
    image = FileField("Upload book poster")
    title = StringField("Enter Book Title")
    release_year = IntegerField("Enter Book Release Year")
    author = StringField("Enter Author")
    genre = StringField("Enter Genre")
    description = TextAreaField("Enter Description")

    submit = SubmitField("Add Book")

class CommentForm(FlaskForm):
    comment = TextAreaField("Comment")
    submit = SubmitField("Add Comment")