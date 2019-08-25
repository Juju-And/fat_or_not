from flask import request, render_template, redirect
from app import db, app
from app.models import User


def bmi_message(bmi_info):
    messages = {'underweight': 'Idź coś zjeść!',
                'overweight': 'Schudnij grubasie!',
                'normal': 'Waga w normie'}
    return messages[bmi_info]


@app.route("/")
def welcome():
    u = User.query.order_by(User.timestamp.desc()).first()
    if u:
        context = {'bmi_info': bmi_message(User.check_bmi(u))}
    else:
        context = {'bmi_info': "Grubasy są wśród nas"}
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
    list_of_ten = []
    users = User.query.order_by(User.timestamp.desc()).limit(10)
    for el in users:
        list_of_ten.append({
            'height': el.height,
            'weight': el.weight,
            'bmi': el.calculate_bmi()
        })

    sum_bmi = 0
    for el in list_of_ten:
        sum_bmi += el['bmi']
    avg_bmi = round(sum_bmi / len(list_of_ten), 2)

    context = {'list_of_ten': list_of_ten,
               'avg_bmi': avg_bmi}
    return render_template('record_list.html', **context)
