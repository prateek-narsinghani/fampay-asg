from flask import render_template, request, url_for
from app import app
from app.forms import SearchForm
from app.models import Video


@app.route("/", methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        pass
    elif request.args.get('order_by'):
        form = SearchForm(request.args)
    page = request.args.get('page', 1, type=int)
    videos = Video.get_videos(page, form)
    next_url = url_for('index',
                       page=videos.next_num,
                       search_query=form.search_query.data,
                       order_by=form.order_by.data,
                       search_by=form.search_by.data,
                       sort=form.sort.data) if videos.has_next else None
    prev_url = url_for('index',
                       page=videos.prev_num,
                       search_query=form.search_query.data,
                       order_by=form.order_by.data,
                       search_by=form.search_by.data,
                       sort=form.sort.data) if videos.has_prev else None
    return render_template('index.html',
                           videos=videos.items,
                           form=form,
                           next_url=next_url,
                           prev_url=prev_url)

import app.fetch_video_scheduler as fetch_video_scheduler
