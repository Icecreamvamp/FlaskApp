#-*- utf-8 -*-
from flask import Flask, render_template, request, redirect
from pg_api import Database as pg
from forms import *
import sys

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("homepage.html")

@app.route("/books_page/")
def books_page():
    return render_template("boeken.html")

@app.route("/portfolio/")
def portfolio_page():
    return render_template("portfolio.html")

@app.route("/order_book/", methods=["GET","POST"])
def order_book():
    form = OrderForm()
    if request.method == "POST":
        naam = form.naam.data
        email = form.email.data
        straat = form.straat.data
        postcode = form.postcode.data
        telefoon = form.telefoon.data
        code = form.code.data
        pg().insert(
                "klanten",
                "('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(naam, email, telefoon, straat, postcode, code)
        )
        return redirect("/")
    return render_template("tinka.html", form=form)



if __name__ == "__main__":
    app.config["SECRET_KEY"] = "secret"
    app.config["SESSION_TYPE"] = "filesystem"
    app.run(debug=True)
