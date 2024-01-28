from flask import render_template, request, url_for
from app import app
from app.forms import SearchForm
from app.models import Video

@app.route("/", methods=['GET', 'POST'])
def index():
    form = SearchForm()
    page = request.args.get('page', 1, type=int)
    videos = Video.get_all_videos(page, form)
    next_url = url_for('index', page=videos.next_num) if videos.has_next else None
    prev_url = url_for('index', page=videos.prev_num) if videos.has_prev else None
    return render_template('index.html', videos=videos.items, form=form, 
                                        next_url=next_url, prev_url=prev_url)

@app.route("/home")
def home():
    return render_template('form.html', message='hello')

@app.route("/submit", methods=['POST'])
def submit():
    query = request.form['query']
    return f'Your search results for: {query}'

import app.fetch_data as fetch_data
