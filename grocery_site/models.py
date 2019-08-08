from flask_sqlalchemy import SQLAlchemy
from grocery_site import app

db = SQLAlchemy(app)

# Leyla's Models

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.String(500))
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
