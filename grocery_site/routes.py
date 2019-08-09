from flask import render_template, redirect, url_for
from grocery_site import app
from grocery_site.models import db
from grocery_site.forms import ContactForm
from grocery_site.models import User


@app.route("/")
def hello_world():
    return render_template("base.html")


@app.route("/contact", methods=["GET", "POST"])
def SendMessage():
    form = ContactForm()
    if form.validate_on_submit():
        print("Your message about {} has been sent".format(form.subject.data))
        user = User(form.name.data, form.email.data,
                    form.subject.data, form.message.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("hello_world"))
    else:
        print("Message Has Not Been Sent")
        print(form.errors)
    return render_template("contact.html", form=form)


@app.route("/about")
def about():
    return render_template("about.html")
