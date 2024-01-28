from config import Config
import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import datetime
from app import app, db


class Video(db.Model):
    id: so.Mapped[str] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(index=True)
    description: so.Mapped[str]
    thumbnail: so.Mapped[str]
    published_at: so.Mapped[datetime]
    channel: so.Mapped[str] = so.mapped_column(index=True)

    def __repr__(self):
        return '<Title: {} Channel:{}>'.format(self.title, self.channel)

    @staticmethod
    def get_all_videos(page, form):
        query = Video._get_query(form)
        videos = db.paginate(query,
                             page=page,
                             per_page=Config.get_post_per_page(),
                             error_out=False)
        return videos

    @staticmethod
    def _get_query(form):
        query = sa.select(Video)
        search_query = form.search_query.data
        words = search_query.split(" ") if search_query != None and search_query != "None" else []
        for word in words:
            query = query.filter(Video.title.ilike(f'%{word}%'))
        return query.order_by(Video._get_video_ordering(form))

    @staticmethod
    def _get_video_ordering(form):
        if form.sort.data == 'asc':
            return Video.published_at.asc()
        else:
            return Video.published_at.desc()
