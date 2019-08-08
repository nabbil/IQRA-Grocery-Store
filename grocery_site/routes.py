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
