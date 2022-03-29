from flask import Flask, render_template, request
#   from flask_sqlalchemy import SQLAlchemy
from flask_app.filter import *
from flask import jsonify

import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:21436587@localhost/sessions'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/registrations', methods=['GET', 'POST'])
def registrations():
    data = []
    if request.method == 'POST' and 'party' in request.form or 'name' in request.form:
        party = request.form['party']
        name = request.form['name']
        rows = filterRegistration(party, name)
        for row in rows:
            data.append(list(row))
    return render_template('registrations.html', data=json.dumps(data))


@app.route('/sessions', methods=['GET', 'POST'])
def session():
    data = {'parties': getRegisteredParties()}
    if request.method == 'POST' and 'party' in request.form:
        party = request.form['party']
        name = request.form['name']
        data['table'] = filterSession(party, name)
    return render_template('sessions.html', data=data)


@app.route('/graphics')
def graphics():
    return render_template('graphics.html')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
