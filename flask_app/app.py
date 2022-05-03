from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import filter
#   from flask import jsonify

import json

labels = [
    'Въздържали се', 'за', 'против'
]

values = [
    4, 20, 2
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C"]


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
    if request.method == 'POST' and 'party' in request.form:
        party = request.form['party']
        name = request.form['name']
        data = filter.filter_registration(party, name)
    return render_template('registrations.html', data=data)


@app.route('/sessions', methods=['GET', 'POST'])
def session():
    data = {'parties': filter.get_registered_parties()}
    if request.method == 'POST' and 'party' in request.form:
        party = request.form['party']
        name = request.form['name']
        data['table'] = filter.filter_session(party, name)
    return render_template('sessions.html', data=data)


@app.route('/graphics')
def graphics():
    return render_template('graphics.html', max=17000, set=zip(values, labels, colors))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
