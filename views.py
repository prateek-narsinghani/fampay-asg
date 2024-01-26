import asyncio
from flask import render_template, request
from app import app
from config import Config

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

import fetch_data



