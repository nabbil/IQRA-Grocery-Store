from flask import render_template, redirect
from grocery_site import app
from grocery_site.models import db


@app.route("/")
def hello_world():
    return render_template("base.html")


@app.route("/contact")
def contact():
    return render_template(("contact.html"))


@app.route("/about")
def about():
    return render_template(("about.html"))
