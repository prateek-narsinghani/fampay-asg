from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "Hello World"

@app.route("/home")
def home():
    return render_template('form.html', message='hello')

@app.route("/submit", methods=['POST'])
def submit():
    query = request.form['query']
    return f'Your search results for: {query}'