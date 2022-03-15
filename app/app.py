from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/deputies')
def deputies():
    return render_template('deputies.html')


@app.route('/sessions')
def session():
    return render_template('sessions.html')


@app.route('/graphics')
def graphics():
    return render_template('graphics.html')


if __name__ == "__main__":
    app.run(debug=True)
