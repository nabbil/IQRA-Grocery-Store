from flask_sqlalchemy import SQLAlchemy
from grocery_site import app

db = SQLAlchemy(app)

# Leyla's Models

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.String(500))
    photo = db.Column(db.String)
    
    def __init__(self, name, price, photo):
        self.name = name
        self.price = price
        self.photo = photo
        
