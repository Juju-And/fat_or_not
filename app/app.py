from flask import request, render_template, redirect
from app import db, app
from app.models import User


@app.route("/")
def welcome():
    # Znajdź dane ostatniego dodanego do bazy i użyć funkcji do sprawdzania
    u = User.query.order_by(User.timestamp.desc()).first()
    bmi_message = {'underweight': 'Idź coś zjeść.',
                   'overweight': 'Schudnij grubasie!',
                   'ok': 'Waga w normie.'}
    context = {}
    if u:
        for key in bmi_message.keys():
            if key == User.check_bmi(u):
                context = {'bmi_info': bmi_message[key]}

        # context = {'bmi_info': User.check_bmi(u)}
    else:
        context = {'bmi_info': "Grubasy są wśród nas"}
    return render_template('welcome_page.html', **context)
    # return render_template('welcome_page.html')


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

# app.run()
