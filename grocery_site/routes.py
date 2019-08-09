from flask import render_template, redirect
from grocery_site import app
from grocery_site.models import db, Products


@app.route("/")
def hello_world():
    return render_template("home.html")

# Leyla's routes


@app.route('/products', methods=['GET', 'POST'])
def products_to_list():
    product = list(Products.query.all())
    print(product)

    return render_template('products.html', product=product)

#next step is to list all product PHOTOS with shorter links in the database with each
#product. should just dump the database and redo it all. 

# product = [
#         {'name': 'Banana', 'price': '$10'},
#         {'name': 'Watermelon', 'price': '$15'},

#     ]

# item = Products("Banana", "$10", "https://bit.ly/2GQOGmb")
# item = Products("Durian", "$50", "https://images.unsplash.com/photo-1519544442-93857b48665e")
# item = Products("Grapefruit", "$89", "https://images.unsplash.com/photo-1563694042438-7fe6940a9bda")
# item = Products("Oranges", "$58.99", "https://bit.ly/2GSJTQX")
# item = Products("Dragonfruit", "$100", "https://images.unsplash.com/photo-1455753141069-7f1d73813b22")
# item = Products("Kiwano", "87", "https://bit.ly/2M9UJXm")
# item = Products("Ugli Fruit", "$120", "https://upload.wikimedia.org/wikipedia/commons/7/72/Ugli.jpg")
# item = Products("Miracle Fruit", "First Child", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/MiracleBerry.jpg/1024px-MiracleBerry.jpg")
# item = Products("Potato", "A Pinky Toe", "https://bit.ly/2ZJEJ1l")