from flask import Flask, request, render_template, redirect, send_file
from app import db
from app.models.user import User

app = Flask(__name__)


@app.route("/")
def welcome():
    context = User.check_bmi(u)
    return render_template('welcome_page.html', **context)


@app.route("/add", methods=["GET"])
def fill_form():
    return render_template("form.html")


@app.route("/add", methods=["POST"])
def add_to_db():
    weight = request.form["weight"]
    height = request.form["height"]

    u = User(weight=weight, height=height)
    db.session.add(u)
    db.session.commit()
    return redirect('/')


@app.route("/list")
def show_list():
    return render_template('record_list.html')


app.run()