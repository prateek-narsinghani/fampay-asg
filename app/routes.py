import asyncio
from flask import render_template, request
from app import app
from app.models import Video
from config import Config

@app.route("/")
def index():
    videos = Video.get_all_videos()
    return render_template('index.html', videos=videos)

@app.route("/home")
def home():
    return render_template('form.html', message='hello')

@app.route("/submit", methods=['POST'])
def submit():
    query = request.form['query']
    return f'Your search results for: {query}'

import app.fetch_data as fetch_data



