from flask_sqlalchemy import SQLAlchemy
from grocery_site import app

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    subject = db.Column(db.String(300), nullable=False)
    message = db.Column(db.String(500), nullable=False)

    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

    def __repr__(self):
        return "Your message about {} has been sent".format(self.subject)
