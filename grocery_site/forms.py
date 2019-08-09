from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from flask_wtf import FlaskForm


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = StringField("Message",validators=[DataRequired()])

    submit = SubmitField()

    def __repr__(self):
        return "{}".format(self.subject)
